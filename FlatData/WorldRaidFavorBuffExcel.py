# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WorldRaidFavorBuffExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsWorldRaidFavorBuffExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WorldRaidFavorBuffExcel()
        x.Init(buf, n + offset)
        return x

    # WorldRaidFavorBuffExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # WorldRaidFavorBuffExcel
    def WorldRaidFavorRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidFavorBuffExcel
    def WorldRaidFavorRankBonus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def WorldRaidFavorBuffExcelStart(builder): builder.StartObject(2)
def WorldRaidFavorBuffExcelAddWorldRaidFavorRank(builder, WorldRaidFavorRank): builder.PrependInt64Slot(0, WorldRaidFavorRank, 0)
def WorldRaidFavorBuffExcelAddWorldRaidFavorRankBonus(builder, WorldRaidFavorRankBonus): builder.PrependInt64Slot(1, WorldRaidFavorRankBonus, 0)
def WorldRaidFavorBuffExcelEnd(builder): return builder.EndObject()
