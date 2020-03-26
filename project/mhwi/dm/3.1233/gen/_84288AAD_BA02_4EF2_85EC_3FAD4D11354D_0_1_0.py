# -*- coding: mbcs -*-
typelib_path = 'D:\\see\\my\\dev\\dm\\dmpy2.1142\\dm\\dm.dll'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from comtypes import BSTR
from ctypes import HRESULT
from comtypes.automation import VARIANT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
from comtypes.automation import VARIANT


class Idmsoft(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Idmsoft Interface'
    _iid_ = GUID('{F3F54BC2-D6D1-4A85-B943-16287ECEA64C}')
    _idlflags_ = ['dual', 'oleautomation']
Idmsoft._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'method Ver')], HRESULT, 'Ver',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(2), helpstring(u'method SetPath')], HRESULT, 'SetPath',
              ( ['in'], BSTR, 'path' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(3), helpstring(u'method Ocr')], HRESULT, 'Ocr',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(4), helpstring(u'method FindStr')], HRESULT, 'FindStr',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(5), helpstring(u'method GetResultCount')], HRESULT, 'GetResultCount',
              ( ['in'], BSTR, 'str' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(6), helpstring(u'method GetResultPos')], HRESULT, 'GetResultPos',
              ( ['in'], BSTR, 'str' ),
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(7), helpstring(u'method StrStr')], HRESULT, 'StrStr',
              ( ['in'], BSTR, 's' ),
              ( ['in'], BSTR, 'str' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(8), helpstring(u'method SendCommand')], HRESULT, 'SendCommand',
              ( ['in'], BSTR, 'cmd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(9), helpstring(u'method UseDict')], HRESULT, 'UseDict',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(10), helpstring(u'method GetBasePath')], HRESULT, 'GetBasePath',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(11), helpstring(u'method SetDictPwd')], HRESULT, 'SetDictPwd',
              ( ['in'], BSTR, 'pwd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(12), helpstring(u'method OcrInFile')], HRESULT, 'OcrInFile',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'pic_name' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(13), helpstring(u'method Capture')], HRESULT, 'Capture',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(14), helpstring(u'method KeyPress')], HRESULT, 'KeyPress',
              ( ['in'], c_int, 'vk' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(15), helpstring(u'method KeyDown')], HRESULT, 'KeyDown',
              ( ['in'], c_int, 'vk' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(16), helpstring(u'method KeyUp')], HRESULT, 'KeyUp',
              ( ['in'], c_int, 'vk' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(17), helpstring(u'method LeftClick')], HRESULT, 'LeftClick',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(18), helpstring(u'method RightClick')], HRESULT, 'RightClick',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(19), helpstring(u'method MiddleClick')], HRESULT, 'MiddleClick',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(20), helpstring(u'method LeftDoubleClick')], HRESULT, 'LeftDoubleClick',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(21), helpstring(u'method LeftDown')], HRESULT, 'LeftDown',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(22), helpstring(u'method LeftUp')], HRESULT, 'LeftUp',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(23), helpstring(u'method RightDown')], HRESULT, 'RightDown',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(24), helpstring(u'method RightUp')], HRESULT, 'RightUp',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(25), helpstring(u'method MoveTo')], HRESULT, 'MoveTo',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(26), helpstring(u'method MoveR')], HRESULT, 'MoveR',
              ( ['in'], c_int, 'rx' ),
              ( ['in'], c_int, 'ry' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(27), helpstring(u'method GetColor')], HRESULT, 'GetColor',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(28), helpstring(u'method GetColorBGR')], HRESULT, 'GetColorBGR',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(29), helpstring(u'method RGB2BGR')], HRESULT, 'RGB2BGR',
              ( ['in'], BSTR, 'rgb_color' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(30), helpstring(u'method BGR2RGB')], HRESULT, 'BGR2RGB',
              ( ['in'], BSTR, 'bgr_color' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(31), helpstring(u'method UnBindWindow')], HRESULT, 'UnBindWindow',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(32), helpstring(u'method CmpColor')], HRESULT, 'CmpColor',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(33), helpstring(u'method ClientToScreen')], HRESULT, 'ClientToScreen',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in', 'out'], POINTER(VARIANT), 'x' ),
              ( ['in', 'out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(34), helpstring(u'method ScreenToClient')], HRESULT, 'ScreenToClient',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in', 'out'], POINTER(VARIANT), 'x' ),
              ( ['in', 'out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(35), helpstring(u'method ShowScrMsg')], HRESULT, 'ShowScrMsg',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'msg' ),
              ( ['in'], BSTR, 'color' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(36), helpstring(u'method SetMinRowGap')], HRESULT, 'SetMinRowGap',
              ( ['in'], c_int, 'row_gap' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(37), helpstring(u'method SetMinColGap')], HRESULT, 'SetMinColGap',
              ( ['in'], c_int, 'col_gap' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(38), helpstring(u'method FindColor')], HRESULT, 'FindColor',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(39), helpstring(u'method FindColorEx')], HRESULT, 'FindColorEx',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(40), helpstring(u'method SetWordLineHeight')], HRESULT, 'SetWordLineHeight',
              ( ['in'], c_int, 'line_height' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(41), helpstring(u'method SetWordGap')], HRESULT, 'SetWordGap',
              ( ['in'], c_int, 'word_gap' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(42), helpstring(u'method SetRowGapNoDict')], HRESULT, 'SetRowGapNoDict',
              ( ['in'], c_int, 'row_gap' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(43), helpstring(u'method SetColGapNoDict')], HRESULT, 'SetColGapNoDict',
              ( ['in'], c_int, 'col_gap' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(44), helpstring(u'method SetWordLineHeightNoDict')], HRESULT, 'SetWordLineHeightNoDict',
              ( ['in'], c_int, 'line_height' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(45), helpstring(u'method SetWordGapNoDict')], HRESULT, 'SetWordGapNoDict',
              ( ['in'], c_int, 'word_gap' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(46), helpstring(u'method GetWordResultCount')], HRESULT, 'GetWordResultCount',
              ( ['in'], BSTR, 'str' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(47), helpstring(u'method GetWordResultPos')], HRESULT, 'GetWordResultPos',
              ( ['in'], BSTR, 'str' ),
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(48), helpstring(u'method GetWordResultStr')], HRESULT, 'GetWordResultStr',
              ( ['in'], BSTR, 'str' ),
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(49), helpstring(u'method GetWords')], HRESULT, 'GetWords',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(50), helpstring(u'method GetWordsNoDict')], HRESULT, 'GetWordsNoDict',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(51), helpstring(u'method SetShowErrorMsg')], HRESULT, 'SetShowErrorMsg',
              ( ['in'], c_int, 'show' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(52), helpstring(u'method GetClientSize')], HRESULT, 'GetClientSize',
              ( ['in'], c_int, 'hwnd' ),
              ( ['out'], POINTER(VARIANT), 'width' ),
              ( ['out'], POINTER(VARIANT), 'height' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(53), helpstring(u'method MoveWindow')], HRESULT, 'MoveWindow',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(54), helpstring(u'method GetColorHSV')], HRESULT, 'GetColorHSV',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(55), helpstring(u'method GetAveRGB')], HRESULT, 'GetAveRGB',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(56), helpstring(u'method GetAveHSV')], HRESULT, 'GetAveHSV',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(57), helpstring(u'method GetForegroundWindow')], HRESULT, 'GetForegroundWindow',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(58), helpstring(u'method GetForegroundFocus')], HRESULT, 'GetForegroundFocus',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(59), helpstring(u'method GetMousePointWindow')], HRESULT, 'GetMousePointWindow',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(60), helpstring(u'method GetPointWindow')], HRESULT, 'GetPointWindow',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(61), helpstring(u'method EnumWindow')], HRESULT, 'EnumWindow',
              ( ['in'], c_int, 'parent' ),
              ( ['in'], BSTR, 'title' ),
              ( ['in'], BSTR, 'class_name' ),
              ( ['in'], c_int, 'filter' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(62), helpstring(u'method GetWindowState')], HRESULT, 'GetWindowState',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'flag' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(63), helpstring(u'method GetWindow')], HRESULT, 'GetWindow',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'flag' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(64), helpstring(u'method GetSpecialWindow')], HRESULT, 'GetSpecialWindow',
              ( ['in'], c_int, 'flag' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(65), helpstring(u'method SetWindowText')], HRESULT, 'SetWindowText',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'text' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(66), helpstring(u'method SetWindowSize')], HRESULT, 'SetWindowSize',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], c_int, 'height' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(67), helpstring(u'method GetWindowRect')], HRESULT, 'GetWindowRect',
              ( ['in'], c_int, 'hwnd' ),
              ( ['out'], POINTER(VARIANT), 'x1' ),
              ( ['out'], POINTER(VARIANT), 'y1' ),
              ( ['out'], POINTER(VARIANT), 'x2' ),
              ( ['out'], POINTER(VARIANT), 'y2' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(68), helpstring(u'method GetWindowTitle')], HRESULT, 'GetWindowTitle',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(69), helpstring(u'method GetWindowClass')], HRESULT, 'GetWindowClass',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(70), helpstring(u'method SetWindowState')], HRESULT, 'SetWindowState',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'flag' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(71), helpstring(u'method CreateFoobarRect')], HRESULT, 'CreateFoobarRect',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], c_int, 'w' ),
              ( ['in'], c_int, 'h' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(72), helpstring(u'method CreateFoobarRoundRect')], HRESULT, 'CreateFoobarRoundRect',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], c_int, 'w' ),
              ( ['in'], c_int, 'h' ),
              ( ['in'], c_int, 'rw' ),
              ( ['in'], c_int, 'rh' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(73), helpstring(u'method CreateFoobarEllipse')], HRESULT, 'CreateFoobarEllipse',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], c_int, 'w' ),
              ( ['in'], c_int, 'h' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(74), helpstring(u'method CreateFoobarCustom')], HRESULT, 'CreateFoobarCustom',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], BSTR, 'pic' ),
              ( ['in'], BSTR, 'trans_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(75), helpstring(u'method FoobarFillRect')], HRESULT, 'FoobarFillRect',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(76), helpstring(u'method FoobarDrawText')], HRESULT, 'FoobarDrawText',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], c_int, 'w' ),
              ( ['in'], c_int, 'h' ),
              ( ['in'], BSTR, 'text' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_int, 'align' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(77), helpstring(u'method FoobarDrawPic')], HRESULT, 'FoobarDrawPic',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], BSTR, 'pic' ),
              ( ['in'], BSTR, 'trans_color' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(78), helpstring(u'method FoobarUpdate')], HRESULT, 'FoobarUpdate',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(79), helpstring(u'method FoobarLock')], HRESULT, 'FoobarLock',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(80), helpstring(u'method FoobarUnlock')], HRESULT, 'FoobarUnlock',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(81), helpstring(u'method FoobarSetFont')], HRESULT, 'FoobarSetFont',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'font_name' ),
              ( ['in'], c_int, 'size' ),
              ( ['in'], c_int, 'flag' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(82), helpstring(u'method FoobarTextRect')], HRESULT, 'FoobarTextRect',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], c_int, 'w' ),
              ( ['in'], c_int, 'h' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(83), helpstring(u'method FoobarPrintText')], HRESULT, 'FoobarPrintText',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'text' ),
              ( ['in'], BSTR, 'color' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(84), helpstring(u'method FoobarClearText')], HRESULT, 'FoobarClearText',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(85), helpstring(u'method FoobarTextLineGap')], HRESULT, 'FoobarTextLineGap',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'gap' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(86), helpstring(u'method Play')], HRESULT, 'Play',
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(87), helpstring(u'method FaqCapture')], HRESULT, 'FaqCapture',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], c_int, 'quality' ),
              ( ['in'], c_int, 'delay' ),
              ( ['in'], c_int, 'time' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(88), helpstring(u'method FaqRelease')], HRESULT, 'FaqRelease',
              ( ['in'], c_int, 'handle' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(89), helpstring(u'method FaqSend')], HRESULT, 'FaqSend',
              ( ['in'], BSTR, 'server' ),
              ( ['in'], c_int, 'handle' ),
              ( ['in'], c_int, 'request_type' ),
              ( ['in'], c_int, 'time_out' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(90), helpstring(u'method Beep')], HRESULT, 'Beep',
              ( ['in'], c_int, 'fre' ),
              ( ['in'], c_int, 'delay' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(91), helpstring(u'method FoobarClose')], HRESULT, 'FoobarClose',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(92), helpstring(u'method MoveDD')], HRESULT, 'MoveDD',
              ( ['in'], c_int, 'dx' ),
              ( ['in'], c_int, 'dy' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(93), helpstring(u'method FaqGetSize')], HRESULT, 'FaqGetSize',
              ( ['in'], c_int, 'handle' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(94), helpstring(u'method LoadPic')], HRESULT, 'LoadPic',
              ( ['in'], BSTR, 'pic_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(95), helpstring(u'method FreePic')], HRESULT, 'FreePic',
              ( ['in'], BSTR, 'pic_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(96), helpstring(u'method GetScreenData')], HRESULT, 'GetScreenData',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(97), helpstring(u'method FreeScreenData')], HRESULT, 'FreeScreenData',
              ( ['in'], c_int, 'handle' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(98), helpstring(u'method WheelUp')], HRESULT, 'WheelUp',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(99), helpstring(u'method WheelDown')], HRESULT, 'WheelDown',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(100), helpstring(u'method SetMouseDelay')], HRESULT, 'SetMouseDelay',
              ( ['in'], BSTR, 'type' ),
              ( ['in'], c_int, 'delay' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(101), helpstring(u'method SetKeypadDelay')], HRESULT, 'SetKeypadDelay',
              ( ['in'], BSTR, 'type' ),
              ( ['in'], c_int, 'delay' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(102), helpstring(u'method GetEnv')], HRESULT, 'GetEnv',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'name' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(103), helpstring(u'method SetEnv')], HRESULT, 'SetEnv',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'name' ),
              ( ['in'], BSTR, 'value' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(104), helpstring(u'method SendString')], HRESULT, 'SendString',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'str' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(105), helpstring(u'method DelEnv')], HRESULT, 'DelEnv',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(106), helpstring(u'method GetPath')], HRESULT, 'GetPath',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(107), helpstring(u'method SetDict')], HRESULT, 'SetDict',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'dict_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(108), helpstring(u'method FindPic')], HRESULT, 'FindPic',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'pic_name' ),
              ( ['in'], BSTR, 'delta_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(109), helpstring(u'method FindPicEx')], HRESULT, 'FindPicEx',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'pic_name' ),
              ( ['in'], BSTR, 'delta_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(110), helpstring(u'method SetClientSize')], HRESULT, 'SetClientSize',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], c_int, 'height' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(111), helpstring(u'method ReadInt')], HRESULT, 'ReadInt',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr' ),
              ( ['in'], c_int, 'type' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(112), helpstring(u'method ReadFloat')], HRESULT, 'ReadFloat',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr' ),
              ( ['retval', 'out'], POINTER(c_float), 'ret' )),
    COMMETHOD([dispid(113), helpstring(u'method ReadDouble')], HRESULT, 'ReadDouble',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr' ),
              ( ['retval', 'out'], POINTER(c_double), 'ret' )),
    COMMETHOD([dispid(114), helpstring(u'method FindInt')], HRESULT, 'FindInt',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr_range' ),
              ( ['in'], c_int, 'int_value_min' ),
              ( ['in'], c_int, 'int_value_max' ),
              ( ['in'], c_int, 'type' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(115), helpstring(u'method FindFloat')], HRESULT, 'FindFloat',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr_range' ),
              ( ['in'], c_float, 'float_value_min' ),
              ( ['in'], c_float, 'float_value_max' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(116), helpstring(u'method FindDouble')], HRESULT, 'FindDouble',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr_range' ),
              ( ['in'], c_double, 'double_value_min' ),
              ( ['in'], c_double, 'double_value_max' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(117), helpstring(u'method FindString')], HRESULT, 'FindString',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr_range' ),
              ( ['in'], BSTR, 'string_value' ),
              ( ['in'], c_int, 'type' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(118), helpstring(u'method GetModuleBaseAddr')], HRESULT, 'GetModuleBaseAddr',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'module_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(119), helpstring(u'method MoveToEx')], HRESULT, 'MoveToEx',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], c_int, 'w' ),
              ( ['in'], c_int, 'h' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(120), helpstring(u'method MatchPicName')], HRESULT, 'MatchPicName',
              ( ['in'], BSTR, 'pic_name' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(121), helpstring(u'method AddDict')], HRESULT, 'AddDict',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'dict_info' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(122), helpstring(u'method EnterCri')], HRESULT, 'EnterCri',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(123), helpstring(u'method LeaveCri')], HRESULT, 'LeaveCri',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(124), helpstring(u'method WriteInt')], HRESULT, 'WriteInt',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr' ),
              ( ['in'], c_int, 'type' ),
              ( ['in'], c_int, 'v' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(125), helpstring(u'method WriteFloat')], HRESULT, 'WriteFloat',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr' ),
              ( ['in'], c_float, 'v' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(126), helpstring(u'method WriteDouble')], HRESULT, 'WriteDouble',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr' ),
              ( ['in'], c_double, 'v' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(127), helpstring(u'method WriteString')], HRESULT, 'WriteString',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr' ),
              ( ['in'], c_int, 'type' ),
              ( ['in'], BSTR, 'v' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(128), helpstring(u'method AsmAdd')], HRESULT, 'AsmAdd',
              ( ['in'], BSTR, 'asm_ins' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(129), helpstring(u'method AsmClear')], HRESULT, 'AsmClear',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(130), helpstring(u'method AsmCall')], HRESULT, 'AsmCall',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'mode' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(131), helpstring(u'method FindMultiColor')], HRESULT, 'FindMultiColor',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'first_color' ),
              ( ['in'], BSTR, 'offset_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(132), helpstring(u'method FindMultiColorEx')], HRESULT, 'FindMultiColorEx',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'first_color' ),
              ( ['in'], BSTR, 'offset_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(133), helpstring(u'method AsmCode')], HRESULT, 'AsmCode',
              ( ['in'], c_int, 'base_addr' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(134), helpstring(u'method Assemble')], HRESULT, 'Assemble',
              ( ['in'], BSTR, 'asm_code' ),
              ( ['in'], c_int, 'base_addr' ),
              ( ['in'], c_int, 'is_upper' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(135), helpstring(u'method SetWindowTransparent')], HRESULT, 'SetWindowTransparent',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'v' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(136), helpstring(u'method ReadData')], HRESULT, 'ReadData',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr' ),
              ( ['in'], c_int, 'len' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(137), helpstring(u'method WriteData')], HRESULT, 'WriteData',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr' ),
              ( ['in'], BSTR, 'data' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(138), helpstring(u'method FindData')], HRESULT, 'FindData',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr_range' ),
              ( ['in'], BSTR, 'data' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(139), helpstring(u'method SetPicPwd')], HRESULT, 'SetPicPwd',
              ( ['in'], BSTR, 'pwd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(140), helpstring(u'method Log')], HRESULT, 'Log',
              ( ['in'], BSTR, 'info' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(141), helpstring(u'method FindStrE')], HRESULT, 'FindStrE',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(142), helpstring(u'method FindColorE')], HRESULT, 'FindColorE',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(143), helpstring(u'method FindPicE')], HRESULT, 'FindPicE',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'pic_name' ),
              ( ['in'], BSTR, 'delta_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(144), helpstring(u'method FindMultiColorE')], HRESULT, 'FindMultiColorE',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'first_color' ),
              ( ['in'], BSTR, 'offset_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(145), helpstring(u'method SetExactOcr')], HRESULT, 'SetExactOcr',
              ( ['in'], c_int, 'exact_ocr' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(146), helpstring(u'method ReadString')], HRESULT, 'ReadString',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr' ),
              ( ['in'], c_int, 'type' ),
              ( ['in'], c_int, 'len' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(147), helpstring(u'method FoobarTextPrintDir')], HRESULT, 'FoobarTextPrintDir',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(148), helpstring(u'method OcrEx')], HRESULT, 'OcrEx',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(149), helpstring(u'method SetDisplayInput')], HRESULT, 'SetDisplayInput',
              ( ['in'], BSTR, 'mode' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(150), helpstring(u'method GetTime')], HRESULT, 'GetTime',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(151), helpstring(u'method GetScreenWidth')], HRESULT, 'GetScreenWidth',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(152), helpstring(u'method GetScreenHeight')], HRESULT, 'GetScreenHeight',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(153), helpstring(u'method BindWindowEx')], HRESULT, 'BindWindowEx',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'display' ),
              ( ['in'], BSTR, 'mouse' ),
              ( ['in'], BSTR, 'keypad' ),
              ( ['in'], BSTR, 'public_desc' ),
              ( ['in'], c_int, 'mode' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(154), helpstring(u'method GetDiskSerial')], HRESULT, 'GetDiskSerial',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(155), helpstring(u'method Md5')], HRESULT, 'Md5',
              ( ['in'], BSTR, 'str' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(156), helpstring(u'method GetMac')], HRESULT, 'GetMac',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(157), helpstring(u'method ActiveInputMethod')], HRESULT, 'ActiveInputMethod',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'id' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(158), helpstring(u'method CheckInputMethod')], HRESULT, 'CheckInputMethod',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'id' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(159), helpstring(u'method FindInputMethod')], HRESULT, 'FindInputMethod',
              ( ['in'], BSTR, 'id' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(160), helpstring(u'method GetCursorPos')], HRESULT, 'GetCursorPos',
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(161), helpstring(u'method BindWindow')], HRESULT, 'BindWindow',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'display' ),
              ( ['in'], BSTR, 'mouse' ),
              ( ['in'], BSTR, 'keypad' ),
              ( ['in'], c_int, 'mode' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(162), helpstring(u'method FindWindow')], HRESULT, 'FindWindow',
              ( ['in'], BSTR, 'class_name' ),
              ( ['in'], BSTR, 'title_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(163), helpstring(u'method GetScreenDepth')], HRESULT, 'GetScreenDepth',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(164), helpstring(u'method SetScreen')], HRESULT, 'SetScreen',
              ( ['in'], c_int, 'width' ),
              ( ['in'], c_int, 'height' ),
              ( ['in'], c_int, 'depth' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(165), helpstring(u'method ExitOs')], HRESULT, 'ExitOs',
              ( ['in'], c_int, 'type' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(166), helpstring(u'method GetDir')], HRESULT, 'GetDir',
              ( ['in'], c_int, 'type' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(167), helpstring(u'method GetOsType')], HRESULT, 'GetOsType',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(168), helpstring(u'method FindWindowEx')], HRESULT, 'FindWindowEx',
              ( ['in'], c_int, 'parent' ),
              ( ['in'], BSTR, 'class_name' ),
              ( ['in'], BSTR, 'title_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(169), helpstring(u'method SetExportDict')], HRESULT, 'SetExportDict',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'dict_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(170), helpstring(u'method GetCursorShape')], HRESULT, 'GetCursorShape',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(171), helpstring(u'method DownCpu')], HRESULT, 'DownCpu',
              ( ['in'], c_int, 'rate' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(172), helpstring(u'method GetCursorSpot')], HRESULT, 'GetCursorSpot',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(173), helpstring(u'method SendString2')], HRESULT, 'SendString2',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'str' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(174), helpstring(u'method FaqPost')], HRESULT, 'FaqPost',
              ( ['in'], BSTR, 'server' ),
              ( ['in'], c_int, 'handle' ),
              ( ['in'], c_int, 'request_type' ),
              ( ['in'], c_int, 'time_out' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(175), helpstring(u'method FaqFetch')], HRESULT, 'FaqFetch',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(176), helpstring(u'method FetchWord')], HRESULT, 'FetchWord',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], BSTR, 'word' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(177), helpstring(u'method CaptureJpg')], HRESULT, 'CaptureJpg',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'file' ),
              ( ['in'], c_int, 'quality' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(178), helpstring(u'method FindStrWithFont')], HRESULT, 'FindStrWithFont',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], BSTR, 'font_name' ),
              ( ['in'], c_int, 'font_size' ),
              ( ['in'], c_int, 'flag' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(179), helpstring(u'method FindStrWithFontE')], HRESULT, 'FindStrWithFontE',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], BSTR, 'font_name' ),
              ( ['in'], c_int, 'font_size' ),
              ( ['in'], c_int, 'flag' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(180), helpstring(u'method FindStrWithFontEx')], HRESULT, 'FindStrWithFontEx',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], BSTR, 'font_name' ),
              ( ['in'], c_int, 'font_size' ),
              ( ['in'], c_int, 'flag' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(181), helpstring(u'method GetDictInfo')], HRESULT, 'GetDictInfo',
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'font_name' ),
              ( ['in'], c_int, 'font_size' ),
              ( ['in'], c_int, 'flag' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(182), helpstring(u'method SaveDict')], HRESULT, 'SaveDict',
              ( ['in'], c_int, 'index' ),
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(183), helpstring(u'method GetWindowProcessId')], HRESULT, 'GetWindowProcessId',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(184), helpstring(u'method GetWindowProcessPath')], HRESULT, 'GetWindowProcessPath',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(185), helpstring(u'method LockInput')], HRESULT, 'LockInput',
              ( ['in'], c_int, 'lock' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(186), helpstring(u'method GetPicSize')], HRESULT, 'GetPicSize',
              ( ['in'], BSTR, 'pic_name' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(187), helpstring(u'method GetID')], HRESULT, 'GetID',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(188), helpstring(u'method CapturePng')], HRESULT, 'CapturePng',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(189), helpstring(u'method CaptureGif')], HRESULT, 'CaptureGif',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'file' ),
              ( ['in'], c_int, 'delay' ),
              ( ['in'], c_int, 'time' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(190), helpstring(u'method ImageToBmp')], HRESULT, 'ImageToBmp',
              ( ['in'], BSTR, 'pic_name' ),
              ( ['in'], BSTR, 'bmp_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(191), helpstring(u'method FindStrFast')], HRESULT, 'FindStrFast',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(192), helpstring(u'method FindStrFastEx')], HRESULT, 'FindStrFastEx',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(193), helpstring(u'method FindStrFastE')], HRESULT, 'FindStrFastE',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(194), helpstring(u'method EnableDisplayDebug')], HRESULT, 'EnableDisplayDebug',
              ( ['in'], c_int, 'enable_debug' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(195), helpstring(u'method CapturePre')], HRESULT, 'CapturePre',
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(196), helpstring(u'method RegEx')], HRESULT, 'RegEx',
              ( ['in'], BSTR, 'code' ),
              ( ['in'], BSTR, 'Ver' ),
              ( ['in'], BSTR, 'ip' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(197), helpstring(u'method GetMachineCode')], HRESULT, 'GetMachineCode',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(198), helpstring(u'method SetClipboard')], HRESULT, 'SetClipboard',
              ( ['in'], BSTR, 'data' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(199), helpstring(u'method GetClipboard')], HRESULT, 'GetClipboard',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(200), helpstring(u'method GetNowDict')], HRESULT, 'GetNowDict',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(201), helpstring(u'method Is64Bit')], HRESULT, 'Is64Bit',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(202), helpstring(u'method GetColorNum')], HRESULT, 'GetColorNum',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(203), helpstring(u'method EnumWindowByProcess')], HRESULT, 'EnumWindowByProcess',
              ( ['in'], BSTR, 'process_name' ),
              ( ['in'], BSTR, 'title' ),
              ( ['in'], BSTR, 'class_name' ),
              ( ['in'], c_int, 'filter' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(204), helpstring(u'method GetDictCount')], HRESULT, 'GetDictCount',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(205), helpstring(u'method GetLastError')], HRESULT, 'GetLastError',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(206), helpstring(u'method GetNetTime')], HRESULT, 'GetNetTime',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(207), helpstring(u'method EnableGetColorByCapture')], HRESULT, 'EnableGetColorByCapture',
              ( ['in'], c_int, 'en' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(208), helpstring(u'method CheckUAC')], HRESULT, 'CheckUAC',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(209), helpstring(u'method SetUAC')], HRESULT, 'SetUAC',
              ( ['in'], c_int, 'uac' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(210), helpstring(u'method DisableFontSmooth')], HRESULT, 'DisableFontSmooth',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(211), helpstring(u'method CheckFontSmooth')], HRESULT, 'CheckFontSmooth',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(212), helpstring(u'method SetDisplayAcceler')], HRESULT, 'SetDisplayAcceler',
              ( ['in'], c_int, 'level' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(213), helpstring(u'method FindWindowByProcess')], HRESULT, 'FindWindowByProcess',
              ( ['in'], BSTR, 'process_name' ),
              ( ['in'], BSTR, 'class_name' ),
              ( ['in'], BSTR, 'title_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(214), helpstring(u'method FindWindowByProcessId')], HRESULT, 'FindWindowByProcessId',
              ( ['in'], c_int, 'process_id' ),
              ( ['in'], BSTR, 'class_name' ),
              ( ['in'], BSTR, 'title_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(215), helpstring(u'method ReadIni')], HRESULT, 'ReadIni',
              ( ['in'], BSTR, 'section' ),
              ( ['in'], BSTR, 'key' ),
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(216), helpstring(u'method WriteIni')], HRESULT, 'WriteIni',
              ( ['in'], BSTR, 'section' ),
              ( ['in'], BSTR, 'key' ),
              ( ['in'], BSTR, 'v' ),
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(217), helpstring(u'method RunApp')], HRESULT, 'RunApp',
              ( ['in'], BSTR, 'path' ),
              ( ['in'], c_int, 'mode' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(218), helpstring(u'method Delay')], HRESULT, 'delay',
              ( ['in'], c_int, 'mis' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(219), helpstring(u'method FindWindowSuper')], HRESULT, 'FindWindowSuper',
              ( ['in'], BSTR, 'spec1' ),
              ( ['in'], c_int, 'flag1' ),
              ( ['in'], c_int, 'type1' ),
              ( ['in'], BSTR, 'spec2' ),
              ( ['in'], c_int, 'flag2' ),
              ( ['in'], c_int, 'type2' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(220), helpstring(u'method ExcludePos')], HRESULT, 'ExcludePos',
              ( ['in'], BSTR, 'all_pos' ),
              ( ['in'], c_int, 'type' ),
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(221), helpstring(u'method FindNearestPos')], HRESULT, 'FindNearestPos',
              ( ['in'], BSTR, 'all_pos' ),
              ( ['in'], c_int, 'type' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(222), helpstring(u'method SortPosDistance')], HRESULT, 'SortPosDistance',
              ( ['in'], BSTR, 'all_pos' ),
              ( ['in'], c_int, 'type' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(223), helpstring(u'method FindPicMem')], HRESULT, 'FindPicMem',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'pic_info' ),
              ( ['in'], BSTR, 'delta_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(224), helpstring(u'method FindPicMemEx')], HRESULT, 'FindPicMemEx',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'pic_info' ),
              ( ['in'], BSTR, 'delta_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(225), helpstring(u'method FindPicMemE')], HRESULT, 'FindPicMemE',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'pic_info' ),
              ( ['in'], BSTR, 'delta_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(226), helpstring(u'method AppendPicAddr')], HRESULT, 'AppendPicAddr',
              ( ['in'], BSTR, 'pic_info' ),
              ( ['in'], c_int, 'addr' ),
              ( ['in'], c_int, 'size' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(227), helpstring(u'method WriteFile')], HRESULT, 'WriteFile',
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'content' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(228), helpstring(u'method Stop')], HRESULT, 'Stop',
              ( ['in'], c_int, 'id' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(229), helpstring(u'method SetDictMem')], HRESULT, 'SetDictMem',
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_int, 'addr' ),
              ( ['in'], c_int, 'size' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(230), helpstring(u'method GetNetTimeSafe')], HRESULT, 'GetNetTimeSafe',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(231), helpstring(u'method ForceUnBindWindow')], HRESULT, 'ForceUnBindWindow',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(232), helpstring(u'method ReadIniPwd')], HRESULT, 'ReadIniPwd',
              ( ['in'], BSTR, 'section' ),
              ( ['in'], BSTR, 'key' ),
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'pwd' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(233), helpstring(u'method WriteIniPwd')], HRESULT, 'WriteIniPwd',
              ( ['in'], BSTR, 'section' ),
              ( ['in'], BSTR, 'key' ),
              ( ['in'], BSTR, 'v' ),
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'pwd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(234), helpstring(u'method DecodeFile')], HRESULT, 'DecodeFile',
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'pwd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(235), helpstring(u'method KeyDownChar')], HRESULT, 'KeyDownChar',
              ( ['in'], BSTR, 'key_str' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(236), helpstring(u'method KeyUpChar')], HRESULT, 'KeyUpChar',
              ( ['in'], BSTR, 'key_str' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(237), helpstring(u'method KeyPressChar')], HRESULT, 'KeyPressChar',
              ( ['in'], BSTR, 'key_str' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(238), helpstring(u'method KeyPressStr')], HRESULT, 'KeyPressStr',
              ( ['in'], BSTR, 'key_str' ),
              ( ['in'], c_int, 'delay' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(239), helpstring(u'method EnableKeypadPatch')], HRESULT, 'EnableKeypadPatch',
              ( ['in'], c_int, 'en' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(240), helpstring(u'method EnableKeypadSync')], HRESULT, 'EnableKeypadSync',
              ( ['in'], c_int, 'en' ),
              ( ['in'], c_int, 'time_out' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(241), helpstring(u'method EnableMouseSync')], HRESULT, 'EnableMouseSync',
              ( ['in'], c_int, 'en' ),
              ( ['in'], c_int, 'time_out' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(242), helpstring(u'method DmGuard')], HRESULT, 'DmGuard',
              ( ['in'], c_int, 'en' ),
              ( ['in'], BSTR, 'type' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(243), helpstring(u'method FaqCaptureFromFile')], HRESULT, 'FaqCaptureFromFile',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'file' ),
              ( ['in'], c_int, 'quality' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(244), helpstring(u'method FindIntEx')], HRESULT, 'FindIntEx',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr_range' ),
              ( ['in'], c_int, 'int_value_min' ),
              ( ['in'], c_int, 'int_value_max' ),
              ( ['in'], c_int, 'type' ),
              ( ['in'], c_int, 'step' ),
              ( ['in'], c_int, 'multi_thread' ),
              ( ['in'], c_int, 'mode' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(245), helpstring(u'method FindFloatEx')], HRESULT, 'FindFloatEx',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr_range' ),
              ( ['in'], c_float, 'float_value_min' ),
              ( ['in'], c_float, 'float_value_max' ),
              ( ['in'], c_int, 'step' ),
              ( ['in'], c_int, 'multi_thread' ),
              ( ['in'], c_int, 'mode' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(246), helpstring(u'method FindDoubleEx')], HRESULT, 'FindDoubleEx',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr_range' ),
              ( ['in'], c_double, 'double_value_min' ),
              ( ['in'], c_double, 'double_value_max' ),
              ( ['in'], c_int, 'step' ),
              ( ['in'], c_int, 'multi_thread' ),
              ( ['in'], c_int, 'mode' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(247), helpstring(u'method FindStringEx')], HRESULT, 'FindStringEx',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr_range' ),
              ( ['in'], BSTR, 'string_value' ),
              ( ['in'], c_int, 'type' ),
              ( ['in'], c_int, 'step' ),
              ( ['in'], c_int, 'multi_thread' ),
              ( ['in'], c_int, 'mode' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(248), helpstring(u'method FindDataEx')], HRESULT, 'FindDataEx',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'addr_range' ),
              ( ['in'], BSTR, 'data' ),
              ( ['in'], c_int, 'step' ),
              ( ['in'], c_int, 'multi_thread' ),
              ( ['in'], c_int, 'mode' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(249), helpstring(u'method EnableRealMouse')], HRESULT, 'EnableRealMouse',
              ( ['in'], c_int, 'en' ),
              ( ['in'], c_int, 'mousedelay' ),
              ( ['in'], c_int, 'mousestep' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(250), helpstring(u'method EnableRealKeypad')], HRESULT, 'EnableRealKeypad',
              ( ['in'], c_int, 'en' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(251), helpstring(u'method SendStringIme')], HRESULT, 'SendStringIme',
              ( ['in'], BSTR, 'str' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(252), helpstring(u'method FoobarDrawLine')], HRESULT, 'FoobarDrawLine',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_int, 'style' ),
              ( ['in'], c_int, 'width' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(253), helpstring(u'method FindStrEx')], HRESULT, 'FindStrEx',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(254), helpstring(u'method IsBind')], HRESULT, 'IsBind',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(255), helpstring(u'method SetDisplayDelay')], HRESULT, 'SetDisplayDelay',
              ( ['in'], c_int, 't' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(256), helpstring(u'method GetDmCount')], HRESULT, 'GetDmCount',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(257), helpstring(u'method DisableScreenSave')], HRESULT, 'DisableScreenSave',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(258), helpstring(u'method DisablePowerSave')], HRESULT, 'DisablePowerSave',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(259), helpstring(u'method SetMemoryHwndAsProcessId')], HRESULT, 'SetMemoryHwndAsProcessId',
              ( ['in'], c_int, 'en' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(260), helpstring(u'method FindShape')], HRESULT, 'FindShape',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'offset_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(261), helpstring(u'method FindShapeE')], HRESULT, 'FindShapeE',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'offset_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(262), helpstring(u'method FindShapeEx')], HRESULT, 'FindShapeEx',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'offset_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(263), helpstring(u'method FindStrS')], HRESULT, 'FindStrS',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(264), helpstring(u'method FindStrExS')], HRESULT, 'FindStrExS',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(265), helpstring(u'method FindStrFastS')], HRESULT, 'FindStrFastS',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(266), helpstring(u'method FindStrFastExS')], HRESULT, 'FindStrFastExS',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'str' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(267), helpstring(u'method FindPicS')], HRESULT, 'FindPicS',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'pic_name' ),
              ( ['in'], BSTR, 'delta_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['out'], POINTER(VARIANT), 'x' ),
              ( ['out'], POINTER(VARIANT), 'y' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(268), helpstring(u'method FindPicExS')], HRESULT, 'FindPicExS',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'pic_name' ),
              ( ['in'], BSTR, 'delta_color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['in'], c_int, 'dir' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(269), helpstring(u'method ClearDict')], HRESULT, 'ClearDict',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(270), helpstring(u'method GetMachineCodeNoMac')], HRESULT, 'GetMachineCodeNoMac',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(271), helpstring(u'method GetClientRect')], HRESULT, 'GetClientRect',
              ( ['in'], c_int, 'hwnd' ),
              ( ['out'], POINTER(VARIANT), 'x1' ),
              ( ['out'], POINTER(VARIANT), 'y1' ),
              ( ['out'], POINTER(VARIANT), 'x2' ),
              ( ['out'], POINTER(VARIANT), 'y2' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(272), helpstring(u'method EnableFakeActive')], HRESULT, 'EnableFakeActive',
              ( ['in'], c_int, 'en' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(273), helpstring(u'method GetScreenDataBmp')], HRESULT, 'GetScreenDataBmp',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['out'], POINTER(VARIANT), 'data' ),
              ( ['out'], POINTER(VARIANT), 'size' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(274), helpstring(u'method EncodeFile')], HRESULT, 'EncodeFile',
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'pwd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(275), helpstring(u'method GetCursorShapeEx')], HRESULT, 'GetCursorShapeEx',
              ( ['in'], c_int, 'type' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(276), helpstring(u'method FaqCancel')], HRESULT, 'FaqCancel',
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(277), helpstring(u'method IntToData')], HRESULT, 'IntToData',
              ( ['in'], c_int, 'int_value' ),
              ( ['in'], c_int, 'type' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(278), helpstring(u'method FloatToData')], HRESULT, 'FloatToData',
              ( ['in'], c_float, 'float_value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(279), helpstring(u'method DoubleToData')], HRESULT, 'DoubleToData',
              ( ['in'], c_double, 'double_value' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(280), helpstring(u'method StringToData')], HRESULT, 'StringToData',
              ( ['in'], BSTR, 'string_value' ),
              ( ['in'], c_int, 'type' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(281), helpstring(u'method SetMemoryFindResultToFile')], HRESULT, 'SetMemoryFindResultToFile',
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(282), helpstring(u'method EnableBind')], HRESULT, 'EnableBind',
              ( ['in'], c_int, 'en' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(283), helpstring(u'method SetSimMode')], HRESULT, 'SetSimMode',
              ( ['in'], c_int, 'mode' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(284), helpstring(u'method LockMouseRect')], HRESULT, 'LockMouseRect',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(285), helpstring(u'method SendPaste')], HRESULT, 'SendPaste',
              ( ['in'], c_int, 'hwnd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(286), helpstring(u'method IsDisplayDead')], HRESULT, 'IsDisplayDead',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], c_int, 't' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(287), helpstring(u'method GetKeyState')], HRESULT, 'GetKeyState',
              ( ['in'], c_int, 'vk' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(288), helpstring(u'method CopyFile')], HRESULT, 'CopyFile',
              ( ['in'], BSTR, 'src_file' ),
              ( ['in'], BSTR, 'dst_file' ),
              ( ['in'], c_int, 'over' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(289), helpstring(u'method IsFileExist')], HRESULT, 'IsFileExist',
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(290), helpstring(u'method DeleteFile')], HRESULT, 'DeleteFile',
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(291), helpstring(u'method MoveFile')], HRESULT, 'MoveFile',
              ( ['in'], BSTR, 'src_file' ),
              ( ['in'], BSTR, 'dst_file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(292), helpstring(u'method CreateFolder')], HRESULT, 'CreateFolder',
              ( ['in'], BSTR, 'folder_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(293), helpstring(u'method DeleteFolder')], HRESULT, 'DeleteFolder',
              ( ['in'], BSTR, 'folder_name' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(294), helpstring(u'method GetFileLength')], HRESULT, 'GetFileLength',
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(295), helpstring(u'method ReadFile')], HRESULT, 'ReadFile',
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(296), helpstring(u'method WaitKey')], HRESULT, 'WaitKey',
              ( ['in'], c_int, 'key_code' ),
              ( ['in'], c_int, 'time_out' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(297), helpstring(u'method DeleteIni')], HRESULT, 'DeleteIni',
              ( ['in'], BSTR, 'section' ),
              ( ['in'], BSTR, 'key' ),
              ( ['in'], BSTR, 'file' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(298), helpstring(u'method DeleteIniPwd')], HRESULT, 'DeleteIniPwd',
              ( ['in'], BSTR, 'section' ),
              ( ['in'], BSTR, 'key' ),
              ( ['in'], BSTR, 'file' ),
              ( ['in'], BSTR, 'pwd' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(299), helpstring(u'method EnableSpeedDx')], HRESULT, 'EnableSpeedDx',
              ( ['in'], c_int, 'en' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(300), helpstring(u'method EnableIme')], HRESULT, 'EnableIme',
              ( ['in'], c_int, 'en' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(301), helpstring(u'method Reg')], HRESULT, 'Reg',
              ( ['in'], BSTR, 'code' ),
              ( ['in'], BSTR, 'Ver' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(302), helpstring(u'method SelectFile')], HRESULT, 'SelectFile',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(303), helpstring(u'method SelectDirectory')], HRESULT, 'SelectDirectory',
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(304), helpstring(u'method LockDisplay')], HRESULT, 'LockDisplay',
              ( ['in'], c_int, 'lock' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(305), helpstring(u'method FoobarSetSave')], HRESULT, 'FoobarSetSave',
              ( ['in'], c_int, 'hwnd' ),
              ( ['in'], BSTR, 'file' ),
              ( ['in'], c_int, 'en' ),
              ( ['in'], BSTR, 'header' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(306), helpstring(u'method EnumWindowSuper')], HRESULT, 'EnumWindowSuper',
              ( ['in'], BSTR, 'spec1' ),
              ( ['in'], c_int, 'flag1' ),
              ( ['in'], c_int, 'type1' ),
              ( ['in'], BSTR, 'spec2' ),
              ( ['in'], c_int, 'flag2' ),
              ( ['in'], c_int, 'type2' ),
              ( ['in'], c_int, 'sort' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
    COMMETHOD([dispid(307), helpstring(u'method DownloadFile')], HRESULT, 'DownloadFile',
              ( ['in'], BSTR, 'url' ),
              ( ['in'], BSTR, 'save_file' ),
              ( ['in'], c_int, 'timeout' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(308), helpstring(u'method EnableKeypadMsg')], HRESULT, 'EnableKeypadMsg',
              ( ['in'], c_int, 'en' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(309), helpstring(u'method EnableMouseMsg')], HRESULT, 'EnableMouseMsg',
              ( ['in'], c_int, 'en' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(310), helpstring(u'method RegNoMac')], HRESULT, 'RegNoMac',
              ( ['in'], BSTR, 'code' ),
              ( ['in'], BSTR, 'Ver' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(311), helpstring(u'method RegExNoMac')], HRESULT, 'RegExNoMac',
              ( ['in'], BSTR, 'code' ),
              ( ['in'], BSTR, 'Ver' ),
              ( ['in'], BSTR, 'ip' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(312), helpstring(u'method SetEnumWindowDelay')], HRESULT, 'SetEnumWindowDelay',
              ( ['in'], c_int, 'delay' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(313), helpstring(u'method FindMulColor')], HRESULT, 'FindMulColor',
              ( ['in'], c_int, 'x1' ),
              ( ['in'], c_int, 'y1' ),
              ( ['in'], c_int, 'x2' ),
              ( ['in'], c_int, 'y2' ),
              ( ['in'], BSTR, 'color' ),
              ( ['in'], c_double, 'sim' ),
              ( ['retval', 'out'], POINTER(c_int), 'ret' )),
    COMMETHOD([dispid(314), helpstring(u'method GetDict')], HRESULT, 'GetDict',
              ( ['in'], c_int, 'index' ),
              ( ['in'], c_int, 'font_index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'ret' )),
]
################################################################
## code template for Idmsoft implementation
##class Idmsoft_Impl(object):
##    def ClearDict(self, index):
##        u'method ClearDict'
##        #return ret
##
##    def FindDataEx(self, hwnd, addr_range, data, step, multi_thread, mode):
##        u'method FindDataEx'
##        #return ret
##
##    def RightUp(self):
##        u'method RightUp'
##        #return ret
##
##    def GetForegroundWindow(self):
##        u'method GetForegroundWindow'
##        #return ret
##
##    def FloatToData(self, float_value):
##        u'method FloatToData'
##        #return ret
##
##    def FindColor(self, x1, y1, x2, y2, color, sim, dir):
##        u'method FindColor'
##        #return x, y, ret
##
##    def SetDictPwd(self, pwd):
##        u'method SetDictPwd'
##        #return ret
##
##    def FreePic(self, pic_name):
##        u'method FreePic'
##        #return ret
##
##    def EnableKeypadPatch(self, en):
##        u'method EnableKeypadPatch'
##        #return ret
##
##    def FaqCancel(self):
##        u'method FaqCancel'
##        #return ret
##
##    def FreeScreenData(self, handle):
##        u'method FreeScreenData'
##        #return ret
##
##    def FindStrEx(self, x1, y1, x2, y2, str, color, sim):
##        u'method FindStrEx'
##        #return ret
##
##    def CapturePng(self, x1, y1, x2, y2, file):
##        u'method CapturePng'
##        #return ret
##
##    def CheckInputMethod(self, hwnd, id):
##        u'method CheckInputMethod'
##        #return ret
##
##    def CreateFoobarCustom(self, hwnd, x, y, pic, trans_color, sim):
##        u'method CreateFoobarCustom'
##        #return ret
##
##    def SetSimMode(self, mode):
##        u'method SetSimMode'
##        #return ret
##
##    def Ocr(self, x1, y1, x2, y2, color, sim):
##        u'method Ocr'
##        #return ret
##
##    def GetWindowTitle(self, hwnd):
##        u'method GetWindowTitle'
##        #return ret
##
##    def FindStrWithFont(self, x1, y1, x2, y2, str, color, sim, font_name, font_size, flag):
##        u'method FindStrWithFont'
##        #return x, y, ret
##
##    def CaptureJpg(self, x1, y1, x2, y2, file, quality):
##        u'method CaptureJpg'
##        #return ret
##
##    def SetPicPwd(self, pwd):
##        u'method SetPicPwd'
##        #return ret
##
##    def MoveTo(self, x, y):
##        u'method MoveTo'
##        #return ret
##
##    def GetModuleBaseAddr(self, hwnd, module_name):
##        u'method GetModuleBaseAddr'
##        #return ret
##
##    def FoobarClearText(self, hwnd):
##        u'method FoobarClearText'
##        #return ret
##
##    def GetWordResultCount(self, str):
##        u'method GetWordResultCount'
##        #return ret
##
##    def GetTime(self):
##        u'method GetTime'
##        #return ret
##
##    def ClientToScreen(self, hwnd):
##        u'method ClientToScreen'
##        #return x, y, ret
##
##    def GetWindowProcessId(self, hwnd):
##        u'method GetWindowProcessId'
##        #return ret
##
##    def GetDir(self, type):
##        u'method GetDir'
##        #return ret
##
##    def AppendPicAddr(self, pic_info, addr, size):
##        u'method AppendPicAddr'
##        #return ret
##
##    def GetWindowProcessPath(self, hwnd):
##        u'method GetWindowProcessPath'
##        #return ret
##
##    def AsmAdd(self, asm_ins):
##        u'method AsmAdd'
##        #return ret
##
##    def SetEnumWindowDelay(self, delay):
##        u'method SetEnumWindowDelay'
##        #return ret
##
##    def DeleteIniPwd(self, section, key, file, pwd):
##        u'method DeleteIniPwd'
##        #return ret
##
##    def SetEnv(self, index, name, value):
##        u'method SetEnv'
##        #return ret
##
##    def FindWindowEx(self, parent, class_name, title_name):
##        u'method FindWindowEx'
##        #return ret
##
##    def SetDict(self, index, dict_name):
##        u'method SetDict'
##        #return ret
##
##    def DisablePowerSave(self):
##        u'method DisablePowerSave'
##        #return ret
##
##    def DelEnv(self, index, name):
##        u'method DelEnv'
##        #return ret
##
##    def SetUAC(self, uac):
##        u'method SetUAC'
##        #return ret
##
##    def GetScreenData(self, x1, y1, x2, y2):
##        u'method GetScreenData'
##        #return ret
##
##    def GetScreenHeight(self):
##        u'method GetScreenHeight'
##        #return ret
##
##    def FindMultiColor(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
##        u'method FindMultiColor'
##        #return x, y, ret
##
##    def AsmClear(self):
##        u'method AsmClear'
##        #return ret
##
##    def SetWordLineHeightNoDict(self, line_height):
##        u'method SetWordLineHeightNoDict'
##        #return ret
##
##    def GetDict(self, index, font_index):
##        u'method GetDict'
##        #return ret
##
##    def FindPicMemE(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
##        u'method FindPicMemE'
##        #return ret
##
##    def FindWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2):
##        u'method FindWindowSuper'
##        #return ret
##
##    def SetWordGap(self, word_gap):
##        u'method SetWordGap'
##        #return ret
##
##    def ExitOs(self, type):
##        u'method ExitOs'
##        #return ret
##
##    def SetWindowSize(self, hwnd, width, height):
##        u'method SetWindowSize'
##        #return ret
##
##    def GetWordResultPos(self, str, index):
##        u'method GetWordResultPos'
##        #return x, y, ret
##
##    def GetPicSize(self, pic_name):
##        u'method GetPicSize'
##        #return ret
##
##    def GetAveRGB(self, x1, y1, x2, y2):
##        u'method GetAveRGB'
##        #return ret
##
##    def FindString(self, hwnd, addr_range, string_value, type):
##        u'method FindString'
##        #return ret
##
##    def GetResultCount(self, str):
##        u'method GetResultCount'
##        #return ret
##
##    def LeftDoubleClick(self):
##        u'method LeftDoubleClick'
##        #return ret
##
##    def AsmCode(self, base_addr):
##        u'method AsmCode'
##        #return ret
##
##    def GetAveHSV(self, x1, y1, x2, y2):
##        u'method GetAveHSV'
##        #return ret
##
##    def MoveDD(self, dx, dy):
##        u'method MoveDD'
##        #return ret
##
##    def GetForegroundFocus(self):
##        u'method GetForegroundFocus'
##        #return ret
##
##    def KeyDownChar(self, key_str):
##        u'method KeyDownChar'
##        #return ret
##
##    def FindStrFast(self, x1, y1, x2, y2, str, color, sim):
##        u'method FindStrFast'
##        #return x, y, ret
##
##    def GetResultPos(self, str, index):
##        u'method GetResultPos'
##        #return x, y, ret
##
##    def CopyFile(self, src_file, dst_file, over):
##        u'method CopyFile'
##        #return ret
##
##    def FindStrFastE(self, x1, y1, x2, y2, str, color, sim):
##        u'method FindStrFastE'
##        #return ret
##
##    def GetCursorSpot(self):
##        u'method GetCursorSpot'
##        #return ret
##
##    def GetClientRect(self, hwnd):
##        u'method GetClientRect'
##        #return x1, y1, x2, y2, ret
##
##    def FaqGetSize(self, handle):
##        u'method FaqGetSize'
##        #return ret
##
##    def EnableKeypadMsg(self, en):
##        u'method EnableKeypadMsg'
##        #return ret
##
##    def SetWindowText(self, hwnd, text):
##        u'method SetWindowText'
##        #return ret
##
##    def RegExNoMac(self, code, Ver, ip):
##        u'method RegExNoMac'
##        #return ret
##
##    def EnumWindow(self, parent, title, class_name, filter):
##        u'method EnumWindow'
##        #return ret
##
##    def FaqFetch(self):
##        u'method FaqFetch'
##        #return ret
##
##    def FindIntEx(self, hwnd, addr_range, int_value_min, int_value_max, type, step, multi_thread, mode):
##        u'method FindIntEx'
##        #return ret
##
##    def FindStrFastS(self, x1, y1, x2, y2, str, color, sim):
##        u'method FindStrFastS'
##        #return x, y, ret
##
##    def FindData(self, hwnd, addr_range, data):
##        u'method FindData'
##        #return ret
##
##    def GetKeyState(self, vk):
##        u'method GetKeyState'
##        #return ret
##
##    def ReadString(self, hwnd, addr, type, len):
##        u'method ReadString'
##        #return ret
##
##    def WriteFloat(self, hwnd, addr, v):
##        u'method WriteFloat'
##        #return ret
##
##    def FindShape(self, x1, y1, x2, y2, offset_color, sim, dir):
##        u'method FindShape'
##        #return x, y, ret
##
##    def EnumWindowByProcess(self, process_name, title, class_name, filter):
##        u'method EnumWindowByProcess'
##        #return ret
##
##    def Capture(self, x1, y1, x2, y2, file):
##        u'method Capture'
##        #return ret
##
##    def SetMinColGap(self, col_gap):
##        u'method SetMinColGap'
##        #return ret
##
##    def GetDictInfo(self, str, font_name, font_size, flag):
##        u'method GetDictInfo'
##        #return ret
##
##    def FindStrWithFontEx(self, x1, y1, x2, y2, str, color, sim, font_name, font_size, flag):
##        u'method FindStrWithFontEx'
##        #return ret
##
##    def ReadFile(self, file):
##        u'method ReadFile'
##        #return ret
##
##    def FaqCaptureFromFile(self, x1, y1, x2, y2, file, quality):
##        u'method FaqCaptureFromFile'
##        #return ret
##
##    def ShowScrMsg(self, x1, y1, x2, y2, msg, color):
##        u'method ShowScrMsg'
##        #return ret
##
##    def KeyDown(self, vk):
##        u'method KeyDown'
##        #return ret
##
##    def FindDoubleEx(self, hwnd, addr_range, double_value_min, double_value_max, step, multi_thread, mode):
##        u'method FindDoubleEx'
##        #return ret
##
##    def Beep(self, fre, delay):
##        u'method Beep'
##        #return ret
##
##    def FaqPost(self, server, handle, request_type, time_out):
##        u'method FaqPost'
##        #return ret
##
##    def FoobarUnlock(self, hwnd):
##        u'method FoobarUnlock'
##        #return ret
##
##    def SendStringIme(self, str):
##        u'method SendStringIme'
##        #return ret
##
##    def WaitKey(self, key_code, time_out):
##        u'method WaitKey'
##        #return ret
##
##    def BGR2RGB(self, bgr_color):
##        u'method BGR2RGB'
##        #return ret
##
##    def FindMultiColorE(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
##        u'method FindMultiColorE'
##        #return ret
##
##    def SetKeypadDelay(self, type, delay):
##        u'method SetKeypadDelay'
##        #return ret
##
##    def StringToData(self, string_value, type):
##        u'method StringToData'
##        #return ret
##
##    def Reg(self, code, Ver):
##        u'method Reg'
##        #return ret
##
##    def LeftClick(self):
##        u'method LeftClick'
##        #return ret
##
##    def GetColorNum(self, x1, y1, x2, y2, color, sim):
##        u'method GetColorNum'
##        #return ret
##
##    def SetWordLineHeight(self, line_height):
##        u'method SetWordLineHeight'
##        #return ret
##
##    def GetMac(self):
##        u'method GetMac'
##        #return ret
##
##    def WriteString(self, hwnd, addr, type, v):
##        u'method WriteString'
##        #return ret
##
##    def GetNetTime(self):
##        u'method GetNetTime'
##        #return ret
##
##    def FindInt(self, hwnd, addr_range, int_value_min, int_value_max, type):
##        u'method FindInt'
##        #return ret
##
##    def ReadData(self, hwnd, addr, len):
##        u'method ReadData'
##        #return ret
##
##    def EnableBind(self, en):
##        u'method EnableBind'
##        #return ret
##
##    def GetClientSize(self, hwnd):
##        u'method GetClientSize'
##        #return width, height, ret
##
##    def SendString2(self, hwnd, str):
##        u'method SendString2'
##        #return ret
##
##    def Is64Bit(self):
##        u'method Is64Bit'
##        #return ret
##
##    def GetWindow(self, hwnd, flag):
##        u'method GetWindow'
##        #return ret
##
##    def AsmCall(self, hwnd, mode):
##        u'method AsmCall'
##        #return ret
##
##    def FindFloatEx(self, hwnd, addr_range, float_value_min, float_value_max, step, multi_thread, mode):
##        u'method FindFloatEx'
##        #return ret
##
##    def LockDisplay(self, lock):
##        u'method LockDisplay'
##        #return ret
##
##    def ReadIni(self, section, key, file):
##        u'method ReadIni'
##        #return ret
##
##    def FoobarTextLineGap(self, hwnd, gap):
##        u'method FoobarTextLineGap'
##        #return ret
##
##    def DisableFontSmooth(self):
##        u'method DisableFontSmooth'
##        #return ret
##
##    def EnableFakeActive(self, en):
##        u'method EnableFakeActive'
##        #return ret
##
##    def GetDiskSerial(self):
##        u'method GetDiskSerial'
##        #return ret
##
##    def EnableGetColorByCapture(self, en):
##        u'method EnableGetColorByCapture'
##        #return ret
##
##    def CreateFolder(self, folder_name):
##        u'method CreateFolder'
##        #return ret
##
##    def WriteDouble(self, hwnd, addr, v):
##        u'method WriteDouble'
##        #return ret
##
##    def FindStringEx(self, hwnd, addr_range, string_value, type, step, multi_thread, mode):
##        u'method FindStringEx'
##        #return ret
##
##    def GetOsType(self):
##        u'method GetOsType'
##        #return ret
##
##    def KeyUpChar(self, key_str):
##        u'method KeyUpChar'
##        #return ret
##
##    def FindStrExS(self, x1, y1, x2, y2, str, color, sim):
##        u'method FindStrExS'
##        #return ret
##
##    def DisableScreenSave(self):
##        u'method DisableScreenSave'
##        #return ret
##
##    def ReadDouble(self, hwnd, addr):
##        u'method ReadDouble'
##        #return ret
##
##    def FindPicMem(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
##        u'method FindPicMem'
##        #return x, y, ret
##
##    def OcrInFile(self, x1, y1, x2, y2, pic_name, color, sim):
##        u'method OcrInFile'
##        #return ret
##
##    def SendString(self, hwnd, str):
##        u'method SendString'
##        #return ret
##
##    def FindStrFastExS(self, x1, y1, x2, y2, str, color, sim):
##        u'method FindStrFastExS'
##        #return ret
##
##    def DecodeFile(self, file, pwd):
##        u'method DecodeFile'
##        #return ret
##
##    def EnableMouseMsg(self, en):
##        u'method EnableMouseMsg'
##        #return ret
##
##    def GetPointWindow(self, x, y):
##        u'method GetPointWindow'
##        #return ret
##
##    def FaqSend(self, server, handle, request_type, time_out):
##        u'method FaqSend'
##        #return ret
##
##    def AddDict(self, index, dict_info):
##        u'method AddDict'
##        #return ret
##
##    def FoobarDrawText(self, hwnd, x, y, w, h, text, color, align):
##        u'method FoobarDrawText'
##        #return ret
##
##    def CreateFoobarEllipse(self, hwnd, x, y, w, h):
##        u'method CreateFoobarEllipse'
##        #return ret
##
##    def GetCursorShapeEx(self, type):
##        u'method GetCursorShapeEx'
##        #return ret
##
##    def GetMachineCodeNoMac(self):
##        u'method GetMachineCodeNoMac'
##        #return ret
##
##    def ActiveInputMethod(self, hwnd, id):
##        u'method ActiveInputMethod'
##        #return ret
##
##    def SetWordGapNoDict(self, word_gap):
##        u'method SetWordGapNoDict'
##        #return ret
##
##    def FindStrFastEx(self, x1, y1, x2, y2, str, color, sim):
##        u'method FindStrFastEx'
##        #return ret
##
##    def LoadPic(self, pic_name):
##        u'method LoadPic'
##        #return ret
##
##    def SetExactOcr(self, exact_ocr):
##        u'method SetExactOcr'
##        #return ret
##
##    def GetMachineCode(self):
##        u'method GetMachineCode'
##        #return ret
##
##    def FindStrS(self, x1, y1, x2, y2, str, color, sim):
##        u'method FindStrS'
##        #return x, y, ret
##
##    def GetDmCount(self):
##        u'method GetDmCount'
##        #return ret
##
##    def LeftUp(self):
##        u'method LeftUp'
##        #return ret
##
##    def FindInputMethod(self, id):
##        u'method FindInputMethod'
##        #return ret
##
##    def RightClick(self):
##        u'method RightClick'
##        #return ret
##
##    def SendPaste(self, hwnd):
##        u'method SendPaste'
##        #return ret
##
##    def EncodeFile(self, file, pwd):
##        u'method EncodeFile'
##        #return ret
##
##    def FindShapeEx(self, x1, y1, x2, y2, offset_color, sim, dir):
##        u'method FindShapeEx'
##        #return ret
##
##    def ReadIniPwd(self, section, key, file, pwd):
##        u'method ReadIniPwd'
##        #return ret
##
##    def Ver(self):
##        u'method Ver'
##        #return ret
##
##    def Log(self, info):
##        u'method Log'
##        #return ret
##
##    def GetWindowClass(self, hwnd):
##        u'method GetWindowClass'
##        #return ret
##
##    def FoobarClose(self, hwnd):
##        u'method FoobarClose'
##        #return ret
##
##    def GetWindowState(self, hwnd, flag):
##        u'method GetWindowState'
##        #return ret
##
##    def ExcludePos(self, all_pos, type, x1, y1, x2, y2):
##        u'method ExcludePos'
##        #return ret
##
##    def SetClipboard(self, data):
##        u'method SetClipboard'
##        #return ret
##
##    def FindMulColor(self, x1, y1, x2, y2, color, sim):
##        u'method FindMulColor'
##        #return ret
##
##    def MiddleClick(self):
##        u'method MiddleClick'
##        #return ret
##
##    def ImageToBmp(self, pic_name, bmp_name):
##        u'method ImageToBmp'
##        #return ret
##
##    def WheelDown(self):
##        u'method WheelDown'
##        #return ret
##
##    def GetWordsNoDict(self, x1, y1, x2, y2, color):
##        u'method GetWordsNoDict'
##        #return ret
##
##    def FindPicMemEx(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
##        u'method FindPicMemEx'
##        #return ret
##
##    def WriteInt(self, hwnd, addr, type, v):
##        u'method WriteInt'
##        #return ret
##
##    def OcrEx(self, x1, y1, x2, y2, color, sim):
##        u'method OcrEx'
##        #return ret
##
##    def FindShapeE(self, x1, y1, x2, y2, offset_color, sim, dir):
##        u'method FindShapeE'
##        #return ret
##
##    def RegNoMac(self, code, Ver):
##        u'method RegNoMac'
##        #return ret
##
##    def SetPath(self, path):
##        u'method SetPath'
##        #return ret
##
##    def SortPosDistance(self, all_pos, type, x, y):
##        u'method SortPosDistance'
##        #return ret
##
##    def SetMemoryHwndAsProcessId(self, en):
##        u'method SetMemoryHwndAsProcessId'
##        #return ret
##
##    def Play(self, file):
##        u'method Play'
##        #return ret
##
##    def WriteData(self, hwnd, addr, data):
##        u'method WriteData'
##        #return ret
##
##    def GetSpecialWindow(self, flag):
##        u'method GetSpecialWindow'
##        #return ret
##
##    def FoobarDrawPic(self, hwnd, x, y, pic, trans_color):
##        u'method FoobarDrawPic'
##        #return ret
##
##    def GetWindowRect(self, hwnd):
##        u'method GetWindowRect'
##        #return x1, y1, x2, y2, ret
##
##    def FindMultiColorEx(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
##        u'method FindMultiColorEx'
##        #return ret
##
##    def FoobarSetFont(self, hwnd, font_name, size, flag):
##        u'method FoobarSetFont'
##        #return ret
##
##    def KeyPressChar(self, key_str):
##        u'method KeyPressChar'
##        #return ret
##
##    def EnableKeypadSync(self, en, time_out):
##        u'method EnableKeypadSync'
##        #return ret
##
##    def EnableIme(self, en):
##        u'method EnableIme'
##        #return ret
##
##    def SaveDict(self, index, file):
##        u'method SaveDict'
##        #return ret
##
##    def FaqCapture(self, x1, y1, x2, y2, quality, delay, time):
##        u'method FaqCapture'
##        #return ret
##
##    def SetDisplayInput(self, mode):
##        u'method SetDisplayInput'
##        #return ret
##
##    def Assemble(self, asm_code, base_addr, is_upper):
##        u'method Assemble'
##        #return ret
##
##    def FindWindow(self, class_name, title_name):
##        u'method FindWindow'
##        #return ret
##
##    def DeleteFile(self, file):
##        u'method DeleteFile'
##        #return ret
##
##    def Md5(self, str):
##        u'method Md5'
##        #return ret
##
##    def EnableDisplayDebug(self, enable_debug):
##        u'method EnableDisplayDebug'
##        #return ret
##
##    def GetScreenDepth(self):
##        u'method GetScreenDepth'
##        #return ret
##
##    def WriteFile(self, file, content):
##        u'method WriteFile'
##        #return ret
##
##    def SetMemoryFindResultToFile(self, file):
##        u'method SetMemoryFindResultToFile'
##        #return ret
##
##    def WriteIni(self, section, key, v, file):
##        u'method WriteIni'
##        #return ret
##
##    def SetScreen(self, width, height, depth):
##        u'method SetScreen'
##        #return ret
##
##    def ReadFloat(self, hwnd, addr):
##        u'method ReadFloat'
##        #return ret
##
##    def LockInput(self, lock):
##        u'method LockInput'
##        #return ret
##
##    def EnumWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2, sort):
##        u'method EnumWindowSuper'
##        #return ret
##
##    def GetPath(self):
##        u'method GetPath'
##        #return ret
##
##    def FoobarLock(self, hwnd):
##        u'method FoobarLock'
##        #return ret
##
##    def RightDown(self):
##        u'method RightDown'
##        #return ret
##
##    def FoobarUpdate(self, hwnd):
##        u'method FoobarUpdate'
##        #return ret
##
##    def MoveR(self, rx, ry):
##        u'method MoveR'
##        #return ret
##
##    def ScreenToClient(self, hwnd):
##        u'method ScreenToClient'
##        #return x, y, ret
##
##    def RegEx(self, code, Ver, ip):
##        u'method RegEx'
##        #return ret
##
##    def IntToData(self, int_value, type):
##        u'method IntToData'
##        #return ret
##
##    def EnableSpeedDx(self, en):
##        u'method EnableSpeedDx'
##        #return ret
##
##    def FoobarFillRect(self, hwnd, x1, y1, x2, y2, color):
##        u'method FoobarFillRect'
##        #return ret
##
##    def IsDisplayDead(self, x1, y1, x2, y2, t):
##        u'method IsDisplayDead'
##        #return ret
##
##    def ReadInt(self, hwnd, addr, type):
##        u'method ReadInt'
##        #return ret
##
##    def FindStrWithFontE(self, x1, y1, x2, y2, str, color, sim, font_name, font_size, flag):
##        u'method FindStrWithFontE'
##        #return ret
##
##    def GetColorHSV(self, x, y):
##        u'method GetColorHSV'
##        #return ret
##
##    def GetBasePath(self):
##        u'method GetBasePath'
##        #return ret
##
##    def FindPicEx(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
##        u'method FindPicEx'
##        #return ret
##
##    def BindWindowEx(self, hwnd, display, mouse, keypad, public_desc, mode):
##        u'method BindWindowEx'
##        #return ret
##
##    def RunApp(self, path, mode):
##        u'method RunApp'
##        #return ret
##
##    def LeftDown(self):
##        u'method LeftDown'
##        #return ret
##
##    def SetDisplayDelay(self, t):
##        u'method SetDisplayDelay'
##        #return ret
##
##    def GetColorBGR(self, x, y):
##        u'method GetColorBGR'
##        #return ret
##
##    def GetNowDict(self):
##        u'method GetNowDict'
##        #return ret
##
##    def CheckUAC(self):
##        u'method CheckUAC'
##        #return ret
##
##    def CreateFoobarRect(self, hwnd, x, y, w, h):
##        u'method CreateFoobarRect'
##        #return ret
##
##    def FindStrE(self, x1, y1, x2, y2, str, color, sim):
##        u'method FindStrE'
##        #return ret
##
##    def UnBindWindow(self):
##        u'method UnBindWindow'
##        #return ret
##
##    def FoobarSetSave(self, hwnd, file, en, header):
##        u'method FoobarSetSave'
##        #return ret
##
##    def GetCursorPos(self):
##        u'method GetCursorPos'
##        #return x, y, ret
##
##    def GetLastError(self):
##        u'method GetLastError'
##        #return ret
##
##    def MoveFile(self, src_file, dst_file):
##        u'method MoveFile'
##        #return ret
##
##    def FoobarDrawLine(self, hwnd, x1, y1, x2, y2, color, style, width):
##        u'method FoobarDrawLine'
##        #return ret
##
##    def EnableRealKeypad(self, en):
##        u'method EnableRealKeypad'
##        #return ret
##
##    def SetMinRowGap(self, row_gap):
##        u'method SetMinRowGap'
##        #return ret
##
##    def FindPic(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
##        u'method FindPic'
##        #return x, y, ret
##
##    def FaqRelease(self, handle):
##        u'method FaqRelease'
##        #return ret
##
##    def GetMousePointWindow(self):
##        u'method GetMousePointWindow'
##        #return ret
##
##    def LockMouseRect(self, x1, y1, x2, y2):
##        u'method LockMouseRect'
##        #return ret
##
##    def DoubleToData(self, double_value):
##        u'method DoubleToData'
##        #return ret
##
##    def SetShowErrorMsg(self, show):
##        u'method SetShowErrorMsg'
##        #return ret
##
##    def IsBind(self, hwnd):
##        u'method IsBind'
##        #return ret
##
##    def RGB2BGR(self, rgb_color):
##        u'method RGB2BGR'
##        #return ret
##
##    def CaptureGif(self, x1, y1, x2, y2, file, delay, time):
##        u'method CaptureGif'
##        #return ret
##
##    def FindDouble(self, hwnd, addr_range, double_value_min, double_value_max):
##        u'method FindDouble'
##        #return ret
##
##    def WheelUp(self):
##        u'method WheelUp'
##        #return ret
##
##    def FindStr(self, x1, y1, x2, y2, str, color, sim):
##        u'method FindStr'
##        #return x, y, ret
##
##    def FoobarPrintText(self, hwnd, text, color):
##        u'method FoobarPrintText'
##        #return ret
##
##    def EnableMouseSync(self, en, time_out):
##        u'method EnableMouseSync'
##        #return ret
##
##    def CreateFoobarRoundRect(self, hwnd, x, y, w, h, rw, rh):
##        u'method CreateFoobarRoundRect'
##        #return ret
##
##    def EnterCri(self):
##        u'method EnterCri'
##        #return ret
##
##    def GetScreenDataBmp(self, x1, y1, x2, y2):
##        u'method GetScreenDataBmp'
##        #return data, size, ret
##
##    def GetWordResultStr(self, str, index):
##        u'method GetWordResultStr'
##        #return ret
##
##    def Stop(self, id):
##        u'method Stop'
##        #return ret
##
##    def MoveWindow(self, hwnd, x, y):
##        u'method MoveWindow'
##        #return ret
##
##    def DownloadFile(self, url, save_file, timeout):
##        u'method DownloadFile'
##        #return ret
##
##    def GetWords(self, x1, y1, x2, y2, color, sim):
##        u'method GetWords'
##        #return ret
##
##    def delay(self, mis):
##        u'method Delay'
##        #return ret
##
##    def CmpColor(self, x, y, color, sim):
##        u'method CmpColor'
##        #return ret
##
##    def GetClipboard(self):
##        u'method GetClipboard'
##        #return ret
##
##    def CapturePre(self, file):
##        u'method CapturePre'
##        #return ret
##
##    def UseDict(self, index):
##        u'method UseDict'
##        #return ret
##
##    def WriteIniPwd(self, section, key, v, file, pwd):
##        u'method WriteIniPwd'
##        #return ret
##
##    def SelectFile(self):
##        u'method SelectFile'
##        #return ret
##
##    def FindFloat(self, hwnd, addr_range, float_value_min, float_value_max):
##        u'method FindFloat'
##        #return ret
##
##    def DownCpu(self, rate):
##        u'method DownCpu'
##        #return ret
##
##    def ForceUnBindWindow(self, hwnd):
##        u'method ForceUnBindWindow'
##        #return ret
##
##    def FetchWord(self, x1, y1, x2, y2, color, word):
##        u'method FetchWord'
##        #return ret
##
##    def SetRowGapNoDict(self, row_gap):
##        u'method SetRowGapNoDict'
##        #return ret
##
##    def SetMouseDelay(self, type, delay):
##        u'method SetMouseDelay'
##        #return ret
##
##    def FindPicExS(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
##        u'method FindPicExS'
##        #return ret
##
##    def GetFileLength(self, file):
##        u'method GetFileLength'
##        #return ret
##
##    def CheckFontSmooth(self):
##        u'method CheckFontSmooth'
##        #return ret
##
##    def MoveToEx(self, x, y, w, h):
##        u'method MoveToEx'
##        #return ret
##
##    def FindPicE(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
##        u'method FindPicE'
##        #return ret
##
##    def FoobarTextRect(self, hwnd, x, y, w, h):
##        u'method FoobarTextRect'
##        #return ret
##
##    def SetWindowTransparent(self, hwnd, v):
##        u'method SetWindowTransparent'
##        #return ret
##
##    def GetEnv(self, index, name):
##        u'method GetEnv'
##        #return ret
##
##    def FindWindowByProcessId(self, process_id, class_name, title_name):
##        u'method FindWindowByProcessId'
##        #return ret
##
##    def SetExportDict(self, index, dict_name):
##        u'method SetExportDict'
##        #return ret
##
##    def DeleteFolder(self, folder_name):
##        u'method DeleteFolder'
##        #return ret
##
##    def FindPicS(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
##        u'method FindPicS'
##        #return x, y, ret
##
##    def SetColGapNoDict(self, col_gap):
##        u'method SetColGapNoDict'
##        #return ret
##
##    def GetDictCount(self, index):
##        u'method GetDictCount'
##        #return ret
##
##    def SendCommand(self, cmd):
##        u'method SendCommand'
##        #return ret
##
##    def EnableRealMouse(self, en, mousedelay, mousestep):
##        u'method EnableRealMouse'
##        #return ret
##
##    def MatchPicName(self, pic_name):
##        u'method MatchPicName'
##        #return ret
##
##    def FoobarTextPrintDir(self, hwnd, dir):
##        u'method FoobarTextPrintDir'
##        #return ret
##
##    def FindNearestPos(self, all_pos, type, x, y):
##        u'method FindNearestPos'
##        #return ret
##
##    def StrStr(self, s, str):
##        u'method StrStr'
##        #return ret
##
##    def FindColorE(self, x1, y1, x2, y2, color, sim, dir):
##        u'method FindColorE'
##        #return ret
##
##    def SelectDirectory(self):
##        u'method SelectDirectory'
##        #return ret
##
##    def GetCursorShape(self):
##        u'method GetCursorShape'
##        #return ret
##
##    def DeleteIni(self, section, key, file):
##        u'method DeleteIni'
##        #return ret
##
##    def GetColor(self, x, y):
##        u'method GetColor'
##        #return ret
##
##    def KeyPress(self, vk):
##        u'method KeyPress'
##        #return ret
##
##    def KeyUp(self, vk):
##        u'method KeyUp'
##        #return ret
##
##    def GetScreenWidth(self):
##        u'method GetScreenWidth'
##        #return ret
##
##    def GetID(self):
##        u'method GetID'
##        #return ret
##
##    def SetDictMem(self, index, addr, size):
##        u'method SetDictMem'
##        #return ret
##
##    def FindWindowByProcess(self, process_name, class_name, title_name):
##        u'method FindWindowByProcess'
##        #return ret
##
##    def LeaveCri(self):
##        u'method LeaveCri'
##        #return ret
##
##    def IsFileExist(self, file):
##        u'method IsFileExist'
##        #return ret
##
##    def SetWindowState(self, hwnd, flag):
##        u'method SetWindowState'
##        #return ret
##
##    def SetDisplayAcceler(self, level):
##        u'method SetDisplayAcceler'
##        #return ret
##
##    def BindWindow(self, hwnd, display, mouse, keypad, mode):
##        u'method BindWindow'
##        #return ret
##
##    def KeyPressStr(self, key_str, delay):
##        u'method KeyPressStr'
##        #return ret
##
##    def GetNetTimeSafe(self):
##        u'method GetNetTimeSafe'
##        #return ret
##
##    def DmGuard(self, en, type):
##        u'method DmGuard'
##        #return ret
##
##    def FindColorEx(self, x1, y1, x2, y2, color, sim, dir):
##        u'method FindColorEx'
##        #return ret
##
##    def SetClientSize(self, hwnd, width, height):
##        u'method SetClientSize'
##        #return ret
##

class dmsoft(CoClass):
    u'dmsoft Class'
    _reg_clsid_ = GUID('{26037A0E-7CBD-4FFF-9C63-56F2D0770214}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{84288AAD-BA02-4EF2-85EC-3FAD4D11354D}', 1, 0)
dmsoft._com_interfaces_ = [Idmsoft]

class Library(object):
    name = u'Dm'
    _reg_typelib_ = ('{84288AAD-BA02-4EF2-85EC-3FAD4D11354D}', 1, 0)

__all__ = [ 'dmsoft', 'Idmsoft']
from comtypes import _check_version; _check_version('')
