# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WeekDungeonRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsWeekDungeonRewardExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WeekDungeonRewardExcel()
        x.Init(buf, n + offset)
        return x

    # WeekDungeonRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # WeekDungeonRewardExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def DungeonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def RewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def RewardParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def RewardParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def RewardParcelProbability(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def IsDisplayed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WeekDungeonRewardExcel
    def DropItemModelPrefabPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def WeekDungeonRewardExcelStart(builder): builder.StartObject(8)
def WeekDungeonRewardExcelAddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)
def WeekDungeonRewardExcelAddDungeonType(builder, DungeonType): builder.PrependInt32Slot(1, DungeonType, 0)
def WeekDungeonRewardExcelAddRewardParcelType(builder, RewardParcelType): builder.PrependInt32Slot(2, RewardParcelType, 0)
def WeekDungeonRewardExcelAddRewardParcelId(builder, RewardParcelId): builder.PrependInt64Slot(3, RewardParcelId, 0)
def WeekDungeonRewardExcelAddRewardParcelAmount(builder, RewardParcelAmount): builder.PrependInt64Slot(4, RewardParcelAmount, 0)
def WeekDungeonRewardExcelAddRewardParcelProbability(builder, RewardParcelProbability): builder.PrependInt64Slot(5, RewardParcelProbability, 0)
def WeekDungeonRewardExcelAddIsDisplayed(builder, IsDisplayed): builder.PrependBoolSlot(6, IsDisplayed, 0)
def WeekDungeonRewardExcelAddDropItemModelPrefabPath(builder, DropItemModelPrefabPath): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(DropItemModelPrefabPath), 0)
def WeekDungeonRewardExcelEnd(builder): return builder.EndObject()
