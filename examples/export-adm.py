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
    working_dir = 'c:\\temp'

    srf_path = 'c:\\Siebel\\15\\Client\\objects\\enu\\siebel_sia.srf'
    client_folder = 'c:\\Siebel\\15\\Client'
    repo = 'Siebel Repository'

    tns = """
    (DESCRIPTION=
        (ADDRESS_LIST=
            (ADDRESS=
                (PROTOCOL=TCP)
                (HOST=db-server)
                (PORT=1521)
            )
        )
        (CONNECT_DATA=
            (SERVER=DEDICATED)
            (SERVICE_NAME=SIEBELDB)
        )
    )"""
    login = 'USER'
    password = 'PASSWORD'

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

    # Main Part
    sa = SiebelApplication("%s, ServerDataSrc" % cfg_file)

    try:
        print 'Login...'
        sa.login(login, password)
    except SiebelError as e:
        print 'Login Error: %s' % e.message
        exit(1)

    print 'Login Success'

    inp = sa.newPropertySet()
    out = sa.newPropertySet()
    exportBS = sa.getService('EAI Siebel Adapter')
    convertBS = sa.getService('EAI XML Converter')

    inp.setProperty('OutputIntObjectName', 'UDA List Of Values')
    inp.setProperty('PrimaryRowId', '1-23KDS')

    print 'Execute Query'
    exportBS.invokeMethod('Query', inp, out)
    print out.toStr()

    print 'Convert'
    out.setProperty('Tags on Separate Lines', 'FALSE')
    out.setProperty('UseSiebelMessageEnvelope', 'FALSE')
    convertBS.invokeMethod('IntObjHierToXMLDoc', out, out)
    print out.getValue()


if __name__ == '__main__':
    __main__()
