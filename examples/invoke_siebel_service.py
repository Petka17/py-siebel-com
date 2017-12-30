import os

from libs.SiebelCOM import SiebelApplication
from libs.SiebelCOM import SiebelError

TNS_ADMIN = 'c:\\temp\\env'
SIEBEL_CFG = 'c:\\Siebel\\15\\Client\\bin\\enu\\fins.cfg, ServerDataSrc'


def __main__():
    os.environ['TNS_ADMIN'] = TNS_ADMIN

    sa = SiebelApplication(SIEBEL_CFG)

    try:
        sa.login('USER', 'PASSWORD')
    except SiebelError as e:
        print 'Login Error: %s' % e.message
        exit(1)

    bs = sa.getService('Workflow Utilities')
    inp = sa.newPropertySet()
    out = sa.newPropertySet()

    inp.setProperty('root_lvl_prop', 'test')
    inp.addChild(sa.newPropertySet())
    inp.setType('TTTTT')
    inp.setValue('ValVal')

    bs.invokeMethod('Echo', inp, out)

    print out.toStr()


if __name__ == '__main__':
    __main__()
