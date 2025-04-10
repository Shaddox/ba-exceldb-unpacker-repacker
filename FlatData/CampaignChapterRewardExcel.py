# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CampaignChapterRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCampaignChapterRewardExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CampaignChapterRewardExcel()
        x.Init(buf, n + offset)
        return x

    # CampaignChapterRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CampaignChapterRewardExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CampaignChapterRewardExcel
    def CampaignChapterStar(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CampaignChapterRewardExcel
    def ChapterRewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CampaignChapterRewardExcel
    def ChapterRewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CampaignChapterRewardExcel
    def ChapterRewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CampaignChapterRewardExcel
    def ChapterRewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # CampaignChapterRewardExcel
    def ChapterRewardId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # CampaignChapterRewardExcel
    def ChapterRewardIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # CampaignChapterRewardExcel
    def ChapterRewardIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CampaignChapterRewardExcel
    def ChapterRewardIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # CampaignChapterRewardExcel
    def ChapterRewardAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CampaignChapterRewardExcel
    def ChapterRewardAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CampaignChapterRewardExcel
    def ChapterRewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CampaignChapterRewardExcel
    def ChapterRewardAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def CampaignChapterRewardExcelStart(builder): builder.StartObject(5)
def CampaignChapterRewardExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def CampaignChapterRewardExcelAddCampaignChapterStar(builder, CampaignChapterStar): builder.PrependInt64Slot(1, CampaignChapterStar, 0)
def CampaignChapterRewardExcelAddChapterRewardParcelType(builder, ChapterRewardParcelType): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(ChapterRewardParcelType), 0)
def CampaignChapterRewardExcelStartChapterRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CampaignChapterRewardExcelAddChapterRewardId(builder, ChapterRewardId): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(ChapterRewardId), 0)
def CampaignChapterRewardExcelStartChapterRewardIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def CampaignChapterRewardExcelAddChapterRewardAmount(builder, ChapterRewardAmount): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(ChapterRewardAmount), 0)
def CampaignChapterRewardExcelStartChapterRewardAmountVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CampaignChapterRewardExcelEnd(builder): return builder.EndObject()
