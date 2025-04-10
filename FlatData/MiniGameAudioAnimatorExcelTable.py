# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameAudioAnimatorExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMiniGameAudioAnimatorExcelTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameAudioAnimatorExcelTable()
        x.Init(buf, n + offset)
        return x

    # MiniGameAudioAnimatorExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameAudioAnimatorExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatData.MiniGameAudioAnimatorExcel import MiniGameAudioAnimatorExcel
            obj = MiniGameAudioAnimatorExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MiniGameAudioAnimatorExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MiniGameAudioAnimatorExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def MiniGameAudioAnimatorExcelTableStart(builder): builder.StartObject(1)
def MiniGameAudioAnimatorExcelTableAddDataList(builder, DataList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DataList), 0)
def MiniGameAudioAnimatorExcelTableStartDataListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MiniGameAudioAnimatorExcelTableEnd(builder): return builder.EndObject()
