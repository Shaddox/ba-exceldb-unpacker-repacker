# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EquipmentLevelExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsEquipmentLevelExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EquipmentLevelExcel()
        x.Init(buf, n + offset)
        return x

    # EquipmentLevelExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EquipmentLevelExcel
    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EquipmentLevelExcel
    def TierLevelExp(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EquipmentLevelExcel
    def TierLevelExpAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EquipmentLevelExcel
    def TierLevelExpLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EquipmentLevelExcel
    def TierLevelExpIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # EquipmentLevelExcel
    def TotalExp(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EquipmentLevelExcel
    def TotalExpAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EquipmentLevelExcel
    def TotalExpLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EquipmentLevelExcel
    def TotalExpIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def EquipmentLevelExcelStart(builder): builder.StartObject(3)
def EquipmentLevelExcelAddLevel(builder, Level): builder.PrependInt32Slot(0, Level, 0)
def EquipmentLevelExcelAddTierLevelExp(builder, TierLevelExp): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(TierLevelExp), 0)
def EquipmentLevelExcelStartTierLevelExpVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EquipmentLevelExcelAddTotalExp(builder, TotalExp): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(TotalExp), 0)
def EquipmentLevelExcelStartTotalExpVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EquipmentLevelExcelEnd(builder): return builder.EndObject()
