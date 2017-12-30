import win32com.client as wc
import pythoncom as pc

from exception import SiebelError


def vshort(i):
    return wc.VARIANT(pc.VT_BYREF | pc.VT_I2, i)


def vint(i):
    return wc.VARIANT(pc.VT_I4, i)


def vstr(str):
    return wc.VARIANT(pc.VT_BSTR, str)


def vstrarr(list):
    return wc.VARIANT(pc.VT_BYREF | pc.VT_ARRAY | pc.VT_BSTR, list)


def check_error(orig_func):
    def new_func(*args, **kwargs):
        err = ''
        result = orig_func(*args, **kwargs)

        try:
            err = args[0]._sa.GetLastErrText
        except:
            pass

        if err != '':
            raise SiebelError(err)

        return result

    return new_func
