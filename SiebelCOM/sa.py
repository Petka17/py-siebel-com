import win32com.client as wc

from utils import vstr
from utils import vshort
from utils import vstrarr
from utils import check_error

from bc import SiebelBusObject
from ps import SiebelPropertySet
from bs import SiebelService

PROGID = 'SiebelDataServer.ApplicationObject'


class SiebelApplication(object):
    def __init__(self, conf):
        self._sa = wc.Dispatch(PROGID)
        self._sa.LoadObjects(vstr(conf), vshort(0))

    def getLastErrText(self):
        return self._sa.GetLastErrText

    @check_error
    def getBusObject(self, name):
        return SiebelBusObject(self._sa.GetBusObject(vstr(name), vshort(0)),
                               self._sa)

    @check_error
    def getProfileAttr(self, name):
        return self._sa.GetProfileAttr(vstr(name), vshort(0))

    @check_error
    def getService(self, name):
        return SiebelService(self._sa.GetService(vstr(name), vshort(0)),
                             self._sa)

    @check_error
    def getSharedGlobal(self, name):
        return self._sa.GetSharedGlobal(vstr(name), vshort(0))

    @check_error
    def invokeMethod(self, methodName, *methodArgs):
        return self._sa.InvokeMethod(vstr(methodName),
                                     vstrarr(list(methodArgs)),
                                     vshort(0))

    @check_error
    def currencyCode(self):
        return self._sa.CurrencyCode(vshort(0))

    @check_error
    def login(self, login, password):
        self._sa.Login(vstr(login), vstr(password), vshort(0))

    @check_error
    def loginId(self):
        return self._sa.LoginId(vshort(0))

    @check_error
    def loginName(self):
        return self._sa.LoginName(vshort(0))

    @check_error
    def newPropertySet(self):
        return SiebelPropertySet(self._sa.NewPropertySet(vshort(0)), self._sa)

    @check_error
    def positionId(self):
        return self._sa.PositionId(vshort(0))

    @check_error
    def positionName(self):
        return self._sa.PositionName(vshort(0))

    @check_error
    def setPositionId(self, value):
        self._sa.SetPositionId(vstr(value), vshort(0))

    @check_error
    def setPositionName(self, value):
        self._sa.SetPositionName(vstr(value), vshort(0))

    @check_error
    def setProfileAttr(self, name, value):
        self._sa.SetProfileAttr(vstr(name), vstr(value), vshort(0))

    @check_error
    def setSharedGlobal(self, name, value):
        self._sa.SetSharedGlobal(vstr(name), vstr(value), vshort(0))

    @check_error
    def trace(self, msg):
        self._sa.Trace(vstr(msg), vshort(0))

    @check_error
    def traceOff(self):
        self._sa.TraceOff(vshort(0))

    @check_error
    def traceOn(self, file_name, category, source):
        self._sa.TraceOn(vstr(file_name), vstr(
            category), vstr(source), vshort(0))

    def evalExpr(self, expr):
        bo = self.getBusObject('Employee')
        bc = bo.getBusComp('Employee')
        return bc.invokeMethod('EvalExpr', expr)

    def repositoryId(self):
        return self.evalExpr("RepositoryId()")
