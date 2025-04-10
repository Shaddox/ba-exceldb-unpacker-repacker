# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BossExternalBTExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBossExternalBTExcelTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BossExternalBTExcelTable()
        x.Init(buf, n + offset)
        return x

    # BossExternalBTExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BossExternalBTExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatData.BossExternalBTExcel import BossExternalBTExcel
            obj = BossExternalBTExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BossExternalBTExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # BossExternalBTExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def BossExternalBTExcelTableStart(builder): builder.StartObject(1)
def BossExternalBTExcelTableAddDataList(builder, DataList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DataList), 0)
def BossExternalBTExcelTableStartDataListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def BossExternalBTExcelTableEnd(builder): return builder.EndObject()
