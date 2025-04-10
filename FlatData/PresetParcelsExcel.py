# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PresetParcelsExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPresetParcelsExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PresetParcelsExcel()
        x.Init(buf, n + offset)
        return x

    # PresetParcelsExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PresetParcelsExcel
    def ParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetParcelsExcel
    def ParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # PresetParcelsExcel
    def PresetGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # PresetParcelsExcel
    def ParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def PresetParcelsExcelStart(builder): builder.StartObject(4)
def PresetParcelsExcelAddParcelType(builder, ParcelType): builder.PrependInt32Slot(0, ParcelType, 0)
def PresetParcelsExcelAddParcelId(builder, ParcelId): builder.PrependInt64Slot(1, ParcelId, 0)
def PresetParcelsExcelAddPresetGroupId(builder, PresetGroupId): builder.PrependInt64Slot(2, PresetGroupId, 0)
def PresetParcelsExcelAddParcelAmount(builder, ParcelAmount): builder.PrependInt64Slot(3, ParcelAmount, 0)
def PresetParcelsExcelEnd(builder): return builder.EndObject()
