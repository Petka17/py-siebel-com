from utils import vstr
from utils import vshort
from utils import vint
from utils import check_error


class SiebelPropertySet(object):
    def __init__(self, ps, sa):
        self._ps = ps
        self._sa = sa

    @check_error
    def addChild(self, child):
        self._ps.AddChild(child._ps, vshort(0))

    @check_error
    def copy(self):
        return SiebelPropertySet(self._ps.Copy(vshort(0)), self._sa)

    @check_error
    def getChild(self, index):
        return SiebelPropertySet(self._ps.GetChild(vint(index), vshort(0)),
                                 self._sa)

    @check_error
    def getChildCount(self):
        return self._ps.GetChildCount(vshort(0))

    @check_error
    def getFirstProperty(self):
        return self._ps.GetFirstProperty(vshort(0))

    @check_error
    def getNextProperty(self):
        return self._ps.GetNextProperty(vshort(0))

    @check_error
    def getProperty(self, name):
        return self._ps.GetProperty(vstr(name), vshort(0))

    @check_error
    def getPropertyCount(self):
        return self._ps.GetPropertyCount(vshort(0))

    @check_error
    def getType(self):
        return self._ps.GetType(vshort(0))

    @check_error
    def getValue(self):
        return self._ps.GetValue(vshort(0))

    @check_error
    def insertChildAt(self, child, index):
        self._ps.InsertChildAt(child._ps, vint(index), vshort(0))

    @check_error
    def propertyExists(self, name):
        return self._ps.PropertyExists(vstr(name), vshort(0))

    @check_error
    def removeChild(self, index):
        self._ps.RemoveChild(vint(index), vshort(0))

    @check_error
    def removeProperty(self, name):
        self._ps.RemoveProperty(vstr(name), vshort(0))

    @check_error
    def reset(self):
        self._ps.Reset(vshort(0))

    @check_error
    def setProperty(self, name, value):
        self._ps.SetProperty(vstr(name), vstr(value), vshort(0))

    @check_error
    def setType(self, value):
        self._ps.SetType(vstr(value), vshort(0))

    @check_error
    def setValue(self, value):
        self._ps.SetValue(vstr(value), vshort(0))

    def toStr(self):
        return self._toStr(0, 0)

    def _toStr(self, level, child_num):
        indent = ''
        for i in range(0, level):
            indent = indent + "- "
        indent = indent + "> "

        text = ""

        if level < 100:
            if level > 0:
                text = text + indent + \
                    "Child property set #%i at level %i:\n" % (
                        child_num + 1, level)

            text = text + indent + "Value = " + self.getValue() + '\n'
            text = text + indent + "Type = " + self.getType() + '\n'

            prop = self.getFirstProperty()
            while (prop is not None and prop != ""):
                text += indent + "" + prop + " = " + \
                    self.getProperty(prop) + '\n'
                prop = self.getNextProperty()

            for i in range(0, self.getChildCount()):
                text = text + self.getChild(i)._toStr(level + 1, i)

        return text
