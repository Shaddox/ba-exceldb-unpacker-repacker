# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentDebuffRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsEventContentDebuffRewardExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentDebuffRewardExcel()
        x.Init(buf, n + offset)
        return x

    # EventContentDebuffRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventContentDebuffRewardExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentDebuffRewardExcel
    def EventStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentDebuffRewardExcel
    def EventContentItemType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentDebuffRewardExcel
    def RewardPercentage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def EventContentDebuffRewardExcelStart(builder): builder.StartObject(4)
def EventContentDebuffRewardExcelAddEventContentId(builder, EventContentId): builder.PrependInt64Slot(0, EventContentId, 0)
def EventContentDebuffRewardExcelAddEventStageId(builder, EventStageId): builder.PrependInt64Slot(1, EventStageId, 0)
def EventContentDebuffRewardExcelAddEventContentItemType(builder, EventContentItemType): builder.PrependInt32Slot(2, EventContentItemType, 0)
def EventContentDebuffRewardExcelAddRewardPercentage(builder, RewardPercentage): builder.PrependInt64Slot(3, RewardPercentage, 0)
def EventContentDebuffRewardExcelEnd(builder): return builder.EndObject()
