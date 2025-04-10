# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RaidRankingRewardExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRaidRankingRewardExcelTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RaidRankingRewardExcelTable()
        x.Init(buf, n + offset)
        return x

    # RaidRankingRewardExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RaidRankingRewardExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatData.RaidRankingRewardExcel import RaidRankingRewardExcel
            obj = RaidRankingRewardExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # RaidRankingRewardExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # RaidRankingRewardExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def RaidRankingRewardExcelTableStart(builder): builder.StartObject(1)
def RaidRankingRewardExcelTableAddDataList(builder, DataList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DataList), 0)
def RaidRankingRewardExcelTableStartDataListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def RaidRankingRewardExcelTableEnd(builder): return builder.EndObject()
