# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LocalizeCodeInBuildExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLocalizeCodeInBuildExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LocalizeCodeInBuildExcel()
        x.Init(buf, n + offset)
        return x

    # LocalizeCodeInBuildExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # LocalizeCodeInBuildExcel
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # LocalizeCodeInBuildExcel
    def Kr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeCodeInBuildExcel
    def Jp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeCodeInBuildExcel
    def Th(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeCodeInBuildExcel
    def Tw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeCodeInBuildExcel
    def En(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def LocalizeCodeInBuildExcelStart(builder): builder.StartObject(6)
def LocalizeCodeInBuildExcelAddKey(builder, Key): builder.PrependUint32Slot(0, Key, 0)
def LocalizeCodeInBuildExcelAddKr(builder, Kr): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Kr), 0)
def LocalizeCodeInBuildExcelAddJp(builder, Jp): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(Jp), 0)
def LocalizeCodeInBuildExcelAddTh(builder, Th): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(Th), 0)
def LocalizeCodeInBuildExcelAddTw(builder, Tw): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(Tw), 0)
def LocalizeCodeInBuildExcelAddEn(builder, En): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(En), 0)
def LocalizeCodeInBuildExcelEnd(builder): return builder.EndObject()
