# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CampaignUnitExcelTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCampaignUnitExcelTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CampaignUnitExcelTable()
        x.Init(buf, n + offset)
        return x

    # CampaignUnitExcelTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CampaignUnitExcelTable
    def DataList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatData.CampaignUnitExcel import CampaignUnitExcel
            obj = CampaignUnitExcel()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CampaignUnitExcelTable
    def DataListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CampaignUnitExcelTable
    def DataListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def CampaignUnitExcelTableStart(builder): builder.StartObject(1)
def CampaignUnitExcelTableAddDataList(builder, DataList): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DataList), 0)
def CampaignUnitExcelTableStartDataListVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CampaignUnitExcelTableEnd(builder): return builder.EndObject()
