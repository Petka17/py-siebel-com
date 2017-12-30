from utils import vstr
from utils import vshort
from utils import vint
from utils import vstrarr
from utils import check_error


class SiebelBusObject(object):
    def __init__(self, bo, sa):
        self._bo = bo
        self._sa = sa

    @check_error
    def getBusComp(self, name):
        return SiebelBusComp(self._bo.GetBusComp(vstr(name), vshort(0)),
                             self._sa)

    @check_error
    def name(self):
        return self._bo.name(vshort(0))


class SiebelBusComp(object):
    def __init__(self, bc, sa):
        self._bc = bc
        self._sa = sa

    @check_error
    def activateField(self, field):
        self._bc.ActivateField(vstr(field), vshort(0))

    @check_error
    def activateMultipleFields(self, fields):
        self._bc.ActivateMultipleFields(fields._ps, vshort(0))

    @check_error
    def associate(self, mode):
        self._bc.Associate(vint(mode), vshort(0))

    @check_error
    def busObject(self):
        return SiebelBusObject(self.BusObject(vshort(0)). self._sa)

    @check_error
    def clearToQuery(self):
        self._bc.ClearToQuery(vshort(0))

    @check_error
    def deactivateFields(self):
        self._bc.DeactivateFields(vshort(0))

    @check_error
    def deleteRecord(self):
        self._bc.DeleteRecord(vshort(0))

    @check_error
    def executeQuery(self, mode):
        self._bc.ExecuteQuery(vint(mode), vshort(0))

    @check_error
    def executeQuery2(self, mode, ignore):
        self._bc.ExecuteQuery2(vint(mode), vint(ignore), vshort(0))

    @check_error
    def firstRecord(self):
        return self._bc.FirstRecord(vshort(0))

    @check_error
    def getAssocBusComp(self):
        return SiebelBusComp(self._bc.GetAssocBusComp(vshort(0)), self._sa)

    @check_error
    def getFieldValue(self, field):
        return self._bc.GetFieldValue(vstr(field), vshort(0))

    @check_error
    def getFormattedFieldValue(self, field):
        return self._bc.GetFormattedFieldValue(vstr(field), vshort(0))

    @check_error
    def getMVGBusComp(self, FieldName):
        return SiebelBusComp(self._bc.GetMVGBusComp(FieldName, vshort(0)),
                             self._sa)

    @check_error
    def getMultipleFieldValues(self, fields, values):
        return self._bc.GetMultipleFieldValues(fields._ps,
                                               values._ps,
                                               vshort(0))

    @check_error
    def getNamedSearch(self, name):
        return self._bc.GetNamedSearch(vstr(name), vshort(0))

    @check_error
    def getPicklistBusComp(self, FieldName):
        return SiebelBusComp(self._bc.GetPicklistBusComp(FieldName, vshort(0)),
                             self._sa)

    @check_error
    def getSearchExpr(self):
        return self._bc.GetSearchExpr(vshort(0))

    @check_error
    def getSearchSpec(self, field):
        return self._bc.GetSearchSpec(vstr(field), vshort(0))

    @check_error
    def getSortSpec(self):
        return self._bc.GetSortSpec(vshort(0))

    @check_error
    def getUserProperty(self, prop):
        return self._bc.GetUserProperty(vstr(prop), vshort(0))

    @check_error
    def getViewMode(self):
        return self._bc.GetViewMode(vshort(0))

    @check_error
    def invokeMethod(self, name, *margs):
        return self._bc.InvokeMethod(vstr(name),
                                     vstrarr(list(margs)),
                                     vshort(0))

    @check_error
    def lastRecord(self):
        self._bc.LastRecord(vshort(0))

    @check_error
    def newRecord(self, mode):
        self._bc.NewRecord(vint(mode), vshort(0))

    @check_error
    def nextRecord(self):
        self._bc.NextRecord(vshort(0))

    @check_error
    def parentBusComp(self):
        return SiebelBusObject(self._bc.ParentBusComp(vshort(0)), self.sa)

    @check_error
    def pick(self):
        self._bc.Pick(vshort(0))

    @check_error
    def previousRecord(self):
        self._bc.PreviousRecord(vshort(0))

    @check_error
    def refineQuery(self):
        self._bc.RefineQuery(vshort(0))

    @check_error
    def setFieldValue(self, field, value):
        self._bc.SetFieldValue(vstr(field), vstr(value), vshort(0))

    @check_error
    def setFormattedFieldValue(self, field, value):
        self._bc.SetFormattedFieldValue(vstr(field), vstr(value), vshort(0))

    @check_error
    def setMultipleFieldValues(self, values):
        self._bc.SetMultipleFieldValues(values._ps, vshort(0))

    @check_error
    def setNamedSearch(self, name, search):
        self._bc.SetNamedSearch(vstr(name), vstr(search), vshort(0))

    @check_error
    def setSearchExpr(self, expr):
        self._bc.SetSearchExpr(vstr(expr), vshort(0))

    @check_error
    def setSearchSpec(self, field, value):
        self._bc.SetSearchSpec(vstr(field), vstr(value), vshort(0))

    @check_error
    def setSortSpec(self, spec):
        self._bc.SetSortSpec(vstr(spec), vshort(0))

    @check_error
    def setUserProperty(self, name, value):
        self._bc.SetUserProperty(vstr(name), vstr(value), vshort(0))

    @check_error
    def setViewMode(self, mode):
        self._bc.SetViewMode(mode, vshort(0))

    @check_error
    def undoRecord(self):
        self._bc.UndoRecord(vshort(0))

    @check_error
    def writeRecord(self):
        self._bc.WriteRecord(vshort(0))

    @check_error
    def name(self):
        return self._bc.name(vshort(0))

    def setAdminMode(self, mode):
        self.invokeMethod('SetAdminMode', 'TRUE' if mode else 'FALSE')
