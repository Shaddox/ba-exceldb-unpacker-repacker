# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentZoneVisitRewardExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsEventContentZoneVisitRewardExcelTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentZoneVisitRewardExcelTable()
        x.Init(buf, n + offset)
        return x

    # EventContentZoneVisitRewardExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventContentZoneVisitRewardExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatData.EventContentZoneVisitRewardExcel import EventContentZoneVisitRewardExcel
            obj = EventContentZoneVisitRewardExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # EventContentZoneVisitRewardExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentZoneVisitRewardExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def EventContentZoneVisitRewardExcelTableStart(builder): builder.StartObject(1)
def EventContentZoneVisitRewardExcelTableAddDataList(builder, DataList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DataList), 0)
def EventContentZoneVisitRewardExcelTableStartDataListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventContentZoneVisitRewardExcelTableEnd(builder): return builder.EndObject()
