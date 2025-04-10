# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FavorLevelRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFavorLevelRewardExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FavorLevelRewardExcel()
        x.Init(buf, n + offset)
        return x

    # FavorLevelRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FavorLevelRewardExcel
    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FavorLevelRewardExcel
    def FavorLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FavorLevelRewardExcel
    def StatType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # FavorLevelRewardExcel
    def StatTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # FavorLevelRewardExcel
    def StatTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FavorLevelRewardExcel
    def StatTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # FavorLevelRewardExcel
    def StatValue(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # FavorLevelRewardExcel
    def StatValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # FavorLevelRewardExcel
    def StatValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FavorLevelRewardExcel
    def StatValueIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # FavorLevelRewardExcel
    def RewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # FavorLevelRewardExcel
    def RewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # FavorLevelRewardExcel
    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FavorLevelRewardExcel
    def RewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # FavorLevelRewardExcel
    def RewardParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # FavorLevelRewardExcel
    def RewardParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # FavorLevelRewardExcel
    def RewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FavorLevelRewardExcel
    def RewardParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # FavorLevelRewardExcel
    def RewardAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # FavorLevelRewardExcel
    def RewardAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # FavorLevelRewardExcel
    def RewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FavorLevelRewardExcel
    def RewardAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

def FavorLevelRewardExcelStart(builder): builder.StartObject(7)
def FavorLevelRewardExcelAddCharacterId(builder, CharacterId): builder.PrependInt64Slot(0, CharacterId, 0)
def FavorLevelRewardExcelAddFavorLevel(builder, FavorLevel): builder.PrependInt64Slot(1, FavorLevel, 0)
def FavorLevelRewardExcelAddStatType(builder, StatType): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(StatType), 0)
def FavorLevelRewardExcelStartStatTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FavorLevelRewardExcelAddStatValue(builder, StatValue): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(StatValue), 0)
def FavorLevelRewardExcelStartStatValueVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def FavorLevelRewardExcelAddRewardParcelType(builder, RewardParcelType): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelType), 0)
def FavorLevelRewardExcelStartRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FavorLevelRewardExcelAddRewardParcelId(builder, RewardParcelId): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelId), 0)
def FavorLevelRewardExcelStartRewardParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def FavorLevelRewardExcelAddRewardAmount(builder, RewardAmount): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(RewardAmount), 0)
def FavorLevelRewardExcelStartRewardAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def FavorLevelRewardExcelEnd(builder): return builder.EndObject()
