# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterGearLevelExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCharacterGearLevelExcelTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterGearLevelExcelTable()
        x.Init(buf, n + offset)
        return x

    # CharacterGearLevelExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterGearLevelExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatData.CharacterGearLevelExcel import CharacterGearLevelExcel
            obj = CharacterGearLevelExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CharacterGearLevelExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CharacterGearLevelExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def CharacterGearLevelExcelTableStart(builder): builder.StartObject(1)
def CharacterGearLevelExcelTableAddDataList(builder, DataList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DataList), 0)
def CharacterGearLevelExcelTableStartDataListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CharacterGearLevelExcelTableEnd(builder): return builder.EndObject()
