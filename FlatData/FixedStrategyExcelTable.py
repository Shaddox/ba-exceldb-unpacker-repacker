# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FixedStrategyExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFixedStrategyExcelTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FixedStrategyExcelTable()
        x.Init(buf, n + offset)
        return x

    # FixedStrategyExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FixedStrategyExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatData.FixedStrategyExcel import FixedStrategyExcel
            obj = FixedStrategyExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FixedStrategyExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FixedStrategyExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def FixedStrategyExcelTableStart(builder): builder.StartObject(1)
def FixedStrategyExcelTableAddDataList(builder, DataList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DataList), 0)
def FixedStrategyExcelTableStartDataListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FixedStrategyExcelTableEnd(builder): return builder.EndObject()
