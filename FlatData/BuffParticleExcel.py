# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BuffParticleExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBuffParticleExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BuffParticleExcel()
        x.Init(buf, n + offset)
        return x

    # BuffParticleExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BuffParticleExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BuffParticleExcel
    def UniqueName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BuffParticleExcel
    def BuffType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BuffParticleExcel
    def BuffName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BuffParticleExcel
    def ResourcePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def BuffParticleExcelStart(builder): builder.StartObject(5)
def BuffParticleExcelAddUniqueId(builder, UniqueId): builder.PrependInt64Slot(0, UniqueId, 0)
def BuffParticleExcelAddUniqueName(builder, UniqueName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(UniqueName), 0)
def BuffParticleExcelAddBuffType(builder, BuffType): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(BuffType), 0)
def BuffParticleExcelAddBuffName(builder, BuffName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(BuffName), 0)
def BuffParticleExcelAddResourcePath(builder, ResourcePath): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(ResourcePath), 0)
def BuffParticleExcelEnd(builder): return builder.EndObject()
