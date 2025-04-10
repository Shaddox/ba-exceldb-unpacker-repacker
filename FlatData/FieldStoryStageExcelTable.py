# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FieldStoryStageExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFieldStoryStageExcelTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FieldStoryStageExcelTable()
        x.Init(buf, n + offset)
        return x

    # FieldStoryStageExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FieldStoryStageExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatData.FieldStoryStageExcel import FieldStoryStageExcel
            obj = FieldStoryStageExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FieldStoryStageExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FieldStoryStageExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def FieldStoryStageExcelTableStart(builder): builder.StartObject(1)
def FieldStoryStageExcelTableAddDataList(builder, DataList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DataList), 0)
def FieldStoryStageExcelTableStartDataListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FieldStoryStageExcelTableEnd(builder): return builder.EndObject()
