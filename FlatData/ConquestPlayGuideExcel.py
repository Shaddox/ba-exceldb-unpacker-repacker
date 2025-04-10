# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestPlayGuideExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsConquestPlayGuideExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestPlayGuideExcel()
        x.Init(buf, n + offset)
        return x

    # ConquestPlayGuideExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConquestPlayGuideExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestPlayGuideExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestPlayGuideExcel
    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestPlayGuideExcel
    def GuideTitle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestPlayGuideExcel
    def GuideImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestPlayGuideExcel
    def GuideText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ConquestPlayGuideExcelStart(builder): builder.StartObject(6)
def ConquestPlayGuideExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def ConquestPlayGuideExcelAddEventContentId(builder, EventContentId): builder.PrependInt64Slot(1, EventContentId, 0)
def ConquestPlayGuideExcelAddDisplayOrder(builder, DisplayOrder): builder.PrependInt32Slot(2, DisplayOrder, 0)
def ConquestPlayGuideExcelAddGuideTitle(builder, GuideTitle): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(GuideTitle), 0)
def ConquestPlayGuideExcelAddGuideImagePath(builder, GuideImagePath): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(GuideImagePath), 0)
def ConquestPlayGuideExcelAddGuideText(builder, GuideText): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(GuideText), 0)
def ConquestPlayGuideExcelEnd(builder): return builder.EndObject()
