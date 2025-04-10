# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EmblemExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsEmblemExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EmblemExcel()
        x.Init(buf, n + offset)
        return x

    # EmblemExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EmblemExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def Category(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def Rarity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def LocalizeCodeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def UseAtLocalizeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def EmblemTextVisible(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # EmblemExcel
    def IconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EmblemExcel
    def EmblemIconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EmblemExcel
    def EmblemIconNumControl(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def EmblemIconBGPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EmblemExcel
    def EmblemBGPathJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EmblemExcel
    def EmblemBGPathKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EmblemExcel
    def EmblemBGPathTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EmblemExcel
    def EmblemBGPathTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EmblemExcel
    def EmblemBGPathEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EmblemExcel
    def DisplayType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def DisplayStartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EmblemExcel
    def DisplayEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EmblemExcel
    def DislpayFavorLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def CheckPassType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def EmblemParameter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EmblemExcel
    def CheckPassCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def EmblemExcelStart(builder): builder.StartObject(24)
def EmblemExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def EmblemExcelAddCategory(builder, Category): builder.PrependInt32Slot(1, Category, 0)
def EmblemExcelAddRarity(builder, Rarity): builder.PrependInt32Slot(2, Rarity, 0)
def EmblemExcelAddDisplayOrder(builder, DisplayOrder): builder.PrependInt64Slot(3, DisplayOrder, 0)
def EmblemExcelAddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(4, LocalizeEtcId, 0)
def EmblemExcelAddLocalizeCodeId(builder, LocalizeCodeId): builder.PrependUint32Slot(5, LocalizeCodeId, 0)
def EmblemExcelAddUseAtLocalizeId(builder, UseAtLocalizeId): builder.PrependInt64Slot(6, UseAtLocalizeId, 0)
def EmblemExcelAddEmblemTextVisible(builder, EmblemTextVisible): builder.PrependBoolSlot(7, EmblemTextVisible, 0)
def EmblemExcelAddIconPath(builder, IconPath): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(IconPath), 0)
def EmblemExcelAddEmblemIconPath(builder, EmblemIconPath): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(EmblemIconPath), 0)
def EmblemExcelAddEmblemIconNumControl(builder, EmblemIconNumControl): builder.PrependInt32Slot(10, EmblemIconNumControl, 0)
def EmblemExcelAddEmblemIconBGPath(builder, EmblemIconBGPath): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(EmblemIconBGPath), 0)
def EmblemExcelAddEmblemBGPathJp(builder, EmblemBGPathJp): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(EmblemBGPathJp), 0)
def EmblemExcelAddEmblemBGPathKr(builder, EmblemBGPathKr): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(EmblemBGPathKr), 0)
def EmblemExcelAddEmblemBGPathTh(builder, EmblemBGPathTh): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(EmblemBGPathTh), 0)
def EmblemExcelAddEmblemBGPathTw(builder, EmblemBGPathTw): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(EmblemBGPathTw), 0)
def EmblemExcelAddEmblemBGPathEn(builder, EmblemBGPathEn): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(EmblemBGPathEn), 0)
def EmblemExcelAddDisplayType(builder, DisplayType): builder.PrependInt32Slot(17, DisplayType, 0)
def EmblemExcelAddDisplayStartDate(builder, DisplayStartDate): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(DisplayStartDate), 0)
def EmblemExcelAddDisplayEndDate(builder, DisplayEndDate): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(DisplayEndDate), 0)
def EmblemExcelAddDislpayFavorLevel(builder, DislpayFavorLevel): builder.PrependInt32Slot(20, DislpayFavorLevel, 0)
def EmblemExcelAddCheckPassType(builder, CheckPassType): builder.PrependInt32Slot(21, CheckPassType, 0)
def EmblemExcelAddEmblemParameter(builder, EmblemParameter): builder.PrependInt64Slot(22, EmblemParameter, 0)
def EmblemExcelAddCheckPassCount(builder, CheckPassCount): builder.PrependInt64Slot(23, CheckPassCount, 0)
def EmblemExcelEnd(builder): return builder.EndObject()
