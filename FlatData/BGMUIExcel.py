# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BGMUIExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBGMUIExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BGMUIExcel()
        x.Init(buf, n + offset)
        return x

    # BGMUIExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BGMUIExcel
    def UIPrefab(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # BGMUIExcel
    def BGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGMUIExcel
    def BGMId2nd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGMUIExcel
    def BGMId3rd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGMUIExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def BGMUIExcelStart(builder): builder.StartObject(5)
def BGMUIExcelAddUIPrefab(builder, UIPrefab): builder.PrependUint32Slot(0, UIPrefab, 0)
def BGMUIExcelAddBGMId(builder, BGMId): builder.PrependInt64Slot(1, BGMId, 0)
def BGMUIExcelAddBGMId2nd(builder, BGMId2nd): builder.PrependInt64Slot(2, BGMId2nd, 0)
def BGMUIExcelAddBGMId3rd(builder, BGMId3rd): builder.PrependInt64Slot(3, BGMId3rd, 0)
def BGMUIExcelAddEventContentId(builder, EventContentId): builder.PrependInt64Slot(4, EventContentId, 0)
def BGMUIExcelEnd(builder): return builder.EndObject()
