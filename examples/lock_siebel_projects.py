import argparse
import os

from siebelcom import SiebelApplication
from siebelcom import SiebelError


def create_dir(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as e:
            print 'Error occur while creating folders'
            print e
            return False

    if not os.access(path, os.W_OK):
        print 'Working is read only'
        return False

    return True


def __main__():
    parser = argparse.ArgumentParser(prog='Lock Siebel Projects')
    parser.add_argument('client_folder', help='Folder for Siebel Client')
    parser.add_argument('srf_path', help='Path to srf')
    parser.add_argument('tns', help='TNS connection string')
    parser.add_argument('login', help='User for lock project')
    parser.add_argument('password', help='Password for user')
    parser.add_argument('repo', help='Repo name')
    parser.add_argument('working_dir', help='Folder with project.txt file')
    args = parser.parse_args()

    execute(args.client_folder, args.srf_path, args.tns,
            args.login, args.password, args.repo, args.working_dir)


def execute(client_folder, srf_path, tns, login, password, repo, working_dir):
    working_dir = os.path.abspath(working_dir)

    # Start: Get Projects
    projects_file = os.path.join(working_dir, 'projects.txt')

    if not os.path.exists(projects_file):
        print 'There is not projects.txt file found in working dir'
        exit(1)

    with open(projects_file, 'r') as f:
        content = f.readlines()

    projects = [x.strip() for x in content]
    # End: Get Projects

    # Start: Setup Siebel Client
    tns_path = os.path.abspath(os.path.join(working_dir, 'tns'))
    create_dir(tns_path)
    os.environ['TNS_ADMIN'] = tns_path

    with open(os.path.join(tns_path, 'tnsnames.ora'), 'w') as f:
        f.write('SBL = %s' % tns)

    tmpl_cfg_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 'client.tmpl.cfg')
    cfg_file = os.path.join(working_dir, 'client.cfg')

    with open(tmpl_cfg_file, 'r') as tmpl:
        with open(cfg_file, 'w') as cfg:
            for line in tmpl.readlines():
                line = line.replace('[SRF_PATH]', srf_path)
                line = line.replace('[SIEBEL_CLIENT_PATH]', client_folder)
                line = line.replace('[SIEBEL_REPO_NAME]', repo)
                cfg.write(line)
    # End: Setup Siebel Client

    # Main Part
    sa = SiebelApplication("%s, ServerDataSrc" % cfg_file)

    try:
        sa.login(login, password)
    except SiebelError as e:
        print 'Login Error: %s' % e.message
        exit(1)

    bo = sa.getBusObject('Repository Unrestricted')
    bc = bo.getBusComp('Repository Project Unrestricted')

    bc.activateField('Name')
    bc.activateField('Repository Id')
    bc.activateField('Locked')
    bc.activateField('Locked By Id')
    bc.activateField('Locked Date')
    bc.activateField('Language Locked')

    for project in projects:
        print 'Procesing project %s' % project

        bc.clearToQuery()
        bc.setSearchExpr("[Name] = '%s' AND [Repository Id] = '%s'" %
                         (project, sa.repositoryId()))
        bc.executeQuery(1)

        if not bc.firstRecord():
            print 'Create new record'
            bc.newRecord(1)
            bc.setFieldValue('Name', project)
            bc.setFieldValue('Repository Id', sa.repositoryId())

        bc.setFieldValue('Locked', 'Y')
        bc.setFieldValue('Locked By Id', sa.loginId())
        bc.setFieldValue('Locked Date', sa.evalExpr('Timestamp()'))
        bc.setFieldValue('Language Locked', sa.evalExpr('Language()'))
        bc.writeRecord()


if __name__ == '__main__':
    __main__()
