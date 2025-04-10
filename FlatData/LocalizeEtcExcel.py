# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LocalizeEtcExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLocalizeEtcExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LocalizeEtcExcel()
        x.Init(buf, n + offset)
        return x

    # LocalizeEtcExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # LocalizeEtcExcel
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # LocalizeEtcExcel
    def NameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeEtcExcel
    def DescriptionKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeEtcExcel
    def NameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeEtcExcel
    def DescriptionJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeEtcExcel
    def NameTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeEtcExcel
    def DescriptionTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeEtcExcel
    def NameTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeEtcExcel
    def DescriptionTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeEtcExcel
    def NameEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeEtcExcel
    def DescriptionEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def LocalizeEtcExcelStart(builder): builder.StartObject(11)
def LocalizeEtcExcelAddKey(builder, Key): builder.PrependUint32Slot(0, Key, 0)
def LocalizeEtcExcelAddNameKr(builder, NameKr): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(NameKr), 0)
def LocalizeEtcExcelAddDescriptionKr(builder, DescriptionKr): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(DescriptionKr), 0)
def LocalizeEtcExcelAddNameJp(builder, NameJp): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(NameJp), 0)
def LocalizeEtcExcelAddDescriptionJp(builder, DescriptionJp): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(DescriptionJp), 0)
def LocalizeEtcExcelAddNameTh(builder, NameTh): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(NameTh), 0)
def LocalizeEtcExcelAddDescriptionTh(builder, DescriptionTh): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(DescriptionTh), 0)
def LocalizeEtcExcelAddNameTw(builder, NameTw): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(NameTw), 0)
def LocalizeEtcExcelAddDescriptionTw(builder, DescriptionTw): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(DescriptionTw), 0)
def LocalizeEtcExcelAddNameEn(builder, NameEn): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(NameEn), 0)
def LocalizeEtcExcelAddDescriptionEn(builder, DescriptionEn): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(DescriptionEn), 0)
def LocalizeEtcExcelEnd(builder): return builder.EndObject()
