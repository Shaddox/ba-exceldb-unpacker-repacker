# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LocalizeErrorExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLocalizeErrorExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LocalizeErrorExcel()
        x.Init(buf, n + offset)
        return x

    # LocalizeErrorExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # LocalizeErrorExcel
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # LocalizeErrorExcel
    def ErrorLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # LocalizeErrorExcel
    def Kr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeErrorExcel
    def Jp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeErrorExcel
    def Th(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeErrorExcel
    def Tw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # LocalizeErrorExcel
    def En(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def LocalizeErrorExcelStart(builder): builder.StartObject(7)
def LocalizeErrorExcelAddKey(builder, Key): builder.PrependUint32Slot(0, Key, 0)
def LocalizeErrorExcelAddErrorLevel(builder, ErrorLevel): builder.PrependInt32Slot(1, ErrorLevel, 0)
def LocalizeErrorExcelAddKr(builder, Kr): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(Kr), 0)
def LocalizeErrorExcelAddJp(builder, Jp): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(Jp), 0)
def LocalizeErrorExcelAddTh(builder, Th): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(Th), 0)
def LocalizeErrorExcelAddTw(builder, Tw): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(Tw), 0)
def LocalizeErrorExcelAddEn(builder, En): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(En), 0)
def LocalizeErrorExcelEnd(builder): return builder.EndObject()
