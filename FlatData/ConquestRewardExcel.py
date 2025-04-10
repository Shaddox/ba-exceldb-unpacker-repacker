# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsConquestRewardExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestRewardExcel()
        x.Init(buf, n + offset)
        return x

    # ConquestRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConquestRewardExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def RewardTag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def RewardProb(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def RewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def RewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def RewardAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestRewardExcel
    def IsDisplayed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def ConquestRewardExcelStart(builder): builder.StartObject(7)
def ConquestRewardExcelAddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)
def ConquestRewardExcelAddRewardTag(builder, RewardTag): builder.PrependInt32Slot(1, RewardTag, 0)
def ConquestRewardExcelAddRewardProb(builder, RewardProb): builder.PrependInt32Slot(2, RewardProb, 0)
def ConquestRewardExcelAddRewardParcelType(builder, RewardParcelType): builder.PrependInt32Slot(3, RewardParcelType, 0)
def ConquestRewardExcelAddRewardId(builder, RewardId): builder.PrependInt64Slot(4, RewardId, 0)
def ConquestRewardExcelAddRewardAmount(builder, RewardAmount): builder.PrependInt32Slot(5, RewardAmount, 0)
def ConquestRewardExcelAddIsDisplayed(builder, IsDisplayed): builder.PrependBoolSlot(6, IsDisplayed, 0)
def ConquestRewardExcelEnd(builder): return builder.EndObject()
