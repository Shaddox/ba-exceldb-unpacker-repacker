# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CafeRankExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCafeRankExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CafeRankExcel()
        x.Init(buf, n + offset)
        return x

    # CafeRankExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CafeRankExcel
    def CafeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CafeRankExcel
    def Rank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CafeRankExcel
    def RecipeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CafeRankExcel
    def ComfortMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CafeRankExcel
    def TagCountMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CafeRankExcel
    def CharacterVisitMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CafeRankExcel
    def CharacterVisitMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CafeRankExcel
    def CafeVisitWeightBase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CafeRankExcel
    def CafeVisitWeightTagBonusStep(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CafeRankExcel
    def CafeVisitWeightTagBonusStepAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CafeRankExcel
    def CafeVisitWeightTagBonusStepLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CafeRankExcel
    def CafeVisitWeightTagBonusStepIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # CafeRankExcel
    def CafeVisitWeightTagBonus(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CafeRankExcel
    def CafeVisitWeightTagBonusAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # CafeRankExcel
    def CafeVisitWeightTagBonusLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CafeRankExcel
    def CafeVisitWeightTagBonusIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

def CafeRankExcelStart(builder): builder.StartObject(10)
def CafeRankExcelAddCafeId(builder, CafeId): builder.PrependInt64Slot(0, CafeId, 0)
def CafeRankExcelAddRank(builder, Rank): builder.PrependInt64Slot(1, Rank, 0)
def CafeRankExcelAddRecipeId(builder, RecipeId): builder.PrependInt64Slot(2, RecipeId, 0)
def CafeRankExcelAddComfortMax(builder, ComfortMax): builder.PrependInt64Slot(3, ComfortMax, 0)
def CafeRankExcelAddTagCountMax(builder, TagCountMax): builder.PrependInt64Slot(4, TagCountMax, 0)
def CafeRankExcelAddCharacterVisitMin(builder, CharacterVisitMin): builder.PrependInt32Slot(5, CharacterVisitMin, 0)
def CafeRankExcelAddCharacterVisitMax(builder, CharacterVisitMax): builder.PrependInt32Slot(6, CharacterVisitMax, 0)
def CafeRankExcelAddCafeVisitWeightBase(builder, CafeVisitWeightBase): builder.PrependInt32Slot(7, CafeVisitWeightBase, 0)
def CafeRankExcelAddCafeVisitWeightTagBonusStep(builder, CafeVisitWeightTagBonusStep): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(CafeVisitWeightTagBonusStep), 0)
def CafeRankExcelStartCafeVisitWeightTagBonusStepVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CafeRankExcelAddCafeVisitWeightTagBonus(builder, CafeVisitWeightTagBonus): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(CafeVisitWeightTagBonus), 0)
def CafeRankExcelStartCafeVisitWeightTagBonusVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CafeRankExcelEnd(builder): return builder.EndObject()
