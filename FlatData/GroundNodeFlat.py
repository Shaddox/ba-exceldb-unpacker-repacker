# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GroundNodeFlat(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGroundNodeFlat(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GroundNodeFlat()
        x.Init(buf, n + offset)
        return x

    # GroundNodeFlat
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GroundNodeFlat
    def X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GroundNodeFlat
    def Y(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GroundNodeFlat
    def IsCanNotUseSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # GroundNodeFlat
    def Position(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from FlatData.GroundVector3 import GroundVector3
            obj = GroundVector3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GroundNodeFlat
    def NodeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GroundNodeFlat
    def OriginalNodeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def GroundNodeFlatStart(builder): builder.StartObject(6)
def GroundNodeFlatAddX(builder, X): builder.PrependInt32Slot(0, X, 0)
def GroundNodeFlatAddY(builder, Y): builder.PrependInt32Slot(1, Y, 0)
def GroundNodeFlatAddIsCanNotUseSkill(builder, IsCanNotUseSkill): builder.PrependBoolSlot(2, IsCanNotUseSkill, 0)
def GroundNodeFlatAddPosition(builder, Position): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(Position), 0)
def GroundNodeFlatAddNodeType(builder, NodeType): builder.PrependInt32Slot(4, NodeType, 0)
def GroundNodeFlatAddOriginalNodeType(builder, OriginalNodeType): builder.PrependInt32Slot(5, OriginalNodeType, 0)
def GroundNodeFlatEnd(builder): return builder.EndObject()
