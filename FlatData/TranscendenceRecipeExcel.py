# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TranscendenceRecipeExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTranscendenceRecipeExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TranscendenceRecipeExcel()
        x.Init(buf, n + offset)
        return x

    # TranscendenceRecipeExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TranscendenceRecipeExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TranscendenceRecipeExcel
    def DevName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TranscendenceRecipeExcel
    def CostCurrencyType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TranscendenceRecipeExcel
    def CostCurrencyAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TranscendenceRecipeExcel
    def ParcelType_(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # TranscendenceRecipeExcel
    def ParcelType_AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # TranscendenceRecipeExcel
    def ParcelType_Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TranscendenceRecipeExcel
    def ParcelType_IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # TranscendenceRecipeExcel
    def ParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # TranscendenceRecipeExcel
    def ParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # TranscendenceRecipeExcel
    def ParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TranscendenceRecipeExcel
    def ParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # TranscendenceRecipeExcel
    def ParcelAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # TranscendenceRecipeExcel
    def ParcelAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # TranscendenceRecipeExcel
    def ParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TranscendenceRecipeExcel
    def ParcelAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

def TranscendenceRecipeExcelStart(builder): builder.StartObject(7)
def TranscendenceRecipeExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def TranscendenceRecipeExcelAddDevName(builder, DevName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(DevName), 0)
def TranscendenceRecipeExcelAddCostCurrencyType(builder, CostCurrencyType): builder.PrependInt32Slot(2, CostCurrencyType, 0)
def TranscendenceRecipeExcelAddCostCurrencyAmount(builder, CostCurrencyAmount): builder.PrependInt64Slot(3, CostCurrencyAmount, 0)
def TranscendenceRecipeExcelAddParcelType_(builder, ParcelType_): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(ParcelType_), 0)
def TranscendenceRecipeExcelStartParcelType_Vector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TranscendenceRecipeExcelAddParcelId(builder, ParcelId): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ParcelId), 0)
def TranscendenceRecipeExcelStartParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def TranscendenceRecipeExcelAddParcelAmount(builder, ParcelAmount): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(ParcelAmount), 0)
def TranscendenceRecipeExcelStartParcelAmountVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TranscendenceRecipeExcelEnd(builder): return builder.EndObject()
