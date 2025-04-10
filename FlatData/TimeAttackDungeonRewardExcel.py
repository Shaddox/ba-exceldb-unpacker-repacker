# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TimeAttackDungeonRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTimeAttackDungeonRewardExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TimeAttackDungeonRewardExcel()
        x.Init(buf, n + offset)
        return x

    # TimeAttackDungeonRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TimeAttackDungeonRewardExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardMaxPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # TimeAttackDungeonRewardExcel
    def RewardMinPoint(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardMinPointAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardMinPointLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardMinPointIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelDefaultAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelDefaultAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelDefaultAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelDefaultAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelMaxAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelMaxAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelMaxAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TimeAttackDungeonRewardExcel
    def RewardParcelMaxAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

def TimeAttackDungeonRewardExcelStart(builder): builder.StartObject(8)
def TimeAttackDungeonRewardExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def TimeAttackDungeonRewardExcelAddRewardMaxPoint(builder, RewardMaxPoint): builder.PrependInt64Slot(1, RewardMaxPoint, 0)
def TimeAttackDungeonRewardExcelAddRewardType(builder, RewardType): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(RewardType), 0)
def TimeAttackDungeonRewardExcelStartRewardTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TimeAttackDungeonRewardExcelAddRewardMinPoint(builder, RewardMinPoint): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(RewardMinPoint), 0)
def TimeAttackDungeonRewardExcelStartRewardMinPointVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def TimeAttackDungeonRewardExcelAddRewardParcelType(builder, RewardParcelType): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelType), 0)
def TimeAttackDungeonRewardExcelStartRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TimeAttackDungeonRewardExcelAddRewardParcelId(builder, RewardParcelId): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelId), 0)
def TimeAttackDungeonRewardExcelStartRewardParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def TimeAttackDungeonRewardExcelAddRewardParcelDefaultAmount(builder, RewardParcelDefaultAmount): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelDefaultAmount), 0)
def TimeAttackDungeonRewardExcelStartRewardParcelDefaultAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def TimeAttackDungeonRewardExcelAddRewardParcelMaxAmount(builder, RewardParcelMaxAmount): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelMaxAmount), 0)
def TimeAttackDungeonRewardExcelStartRewardParcelMaxAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def TimeAttackDungeonRewardExcelEnd(builder): return builder.EndObject()
