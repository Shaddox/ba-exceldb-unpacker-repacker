# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GroundModuleRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGroundModuleRewardExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GroundModuleRewardExcel()
        x.Init(buf, n + offset)
        return x

    # GroundModuleRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GroundModuleRewardExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # GroundModuleRewardExcel
    def RewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GroundModuleRewardExcel
    def RewardParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GroundModuleRewardExcel
    def RewardParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GroundModuleRewardExcel
    def RewardParcelProbability(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # GroundModuleRewardExcel
    def IsDisplayed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # GroundModuleRewardExcel
    def DropItemModelPrefabPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def GroundModuleRewardExcelStart(builder): builder.StartObject(7)
def GroundModuleRewardExcelAddGroupId(builder, GroupId): builder.PrependUint32Slot(0, GroupId, 0)
def GroundModuleRewardExcelAddRewardParcelType(builder, RewardParcelType): builder.PrependInt32Slot(1, RewardParcelType, 0)
def GroundModuleRewardExcelAddRewardParcelId(builder, RewardParcelId): builder.PrependInt64Slot(2, RewardParcelId, 0)
def GroundModuleRewardExcelAddRewardParcelAmount(builder, RewardParcelAmount): builder.PrependInt64Slot(3, RewardParcelAmount, 0)
def GroundModuleRewardExcelAddRewardParcelProbability(builder, RewardParcelProbability): builder.PrependInt64Slot(4, RewardParcelProbability, 0)
def GroundModuleRewardExcelAddIsDisplayed(builder, IsDisplayed): builder.PrependBoolSlot(5, IsDisplayed, 0)
def GroundModuleRewardExcelAddDropItemModelPrefabPath(builder, DropItemModelPrefabPath): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(DropItemModelPrefabPath), 0)
def GroundModuleRewardExcelEnd(builder): return builder.EndObject()
