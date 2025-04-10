# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterStatsTransExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCharacterStatsTransExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterStatsTransExcel()
        x.Init(buf, n + offset)
        return x

    # CharacterStatsTransExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterStatsTransExcel
    def TransSupportStats(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterStatsTransExcel
    def EchelonExtensionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterStatsTransExcel
    def TransSupportStatsFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterStatsTransExcel
    def StatTransType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def CharacterStatsTransExcelStart(builder): builder.StartObject(4)
def CharacterStatsTransExcelAddTransSupportStats(builder, TransSupportStats): builder.PrependInt32Slot(0, TransSupportStats, 0)
def CharacterStatsTransExcelAddEchelonExtensionType(builder, EchelonExtensionType): builder.PrependInt32Slot(1, EchelonExtensionType, 0)
def CharacterStatsTransExcelAddTransSupportStatsFactor(builder, TransSupportStatsFactor): builder.PrependInt32Slot(2, TransSupportStatsFactor, 0)
def CharacterStatsTransExcelAddStatTransType(builder, StatTransType): builder.PrependInt32Slot(3, StatTransType, 0)
def CharacterStatsTransExcelEnd(builder): return builder.EndObject()
