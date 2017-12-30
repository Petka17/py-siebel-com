from utils import vstr
from utils import vshort
from utils import check_error


class SiebelService(object):
    def __init__(self, bs, sa):
        self._bs = bs
        self._sa = sa

    @check_error
    def getFirstProperty(self):
        return self._bs.GetFirstProperty(vshort(0))

    @check_error
    def getNextProperty(self):
        return self._bs.GetNextProperty(vshort(0))

    @check_error
    def getProperty(self, name):
        return self._bs.GetProperty(name, vshort(0))

    @check_error
    def invokeMethod(self, method, inputs, outputs):
        self._bs.InvokeMethod(vstr(method), inputs._ps, outputs._ps, vshort(0))

    @check_error
    def propertyExists(self, name):
        return self._bs.PropertyExists(vstr(name), vshort(0))

    @check_error
    def removeProperty(self, name):
        self._bs.RemoveProperty(vstr(name), vshort(0))

    @check_error
    def setProperty(self, name, value):
        self._bs.SetProperty(vstr(name), vstr(value), vshort(0))

    @check_error
    def name(self):
        return self._bs.name(vshort(0))
