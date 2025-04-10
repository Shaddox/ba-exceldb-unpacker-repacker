# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentCardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsEventContentCardExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentCardExcel()
        x.Init(buf, n + offset)
        return x

    # EventContentCardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventContentCardExcel
    def CardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentCardExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EventContentCardExcel
    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # EventContentCardExcel
    def IconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentCardExcel
    def BackIconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentCardExcel
    def RewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventContentCardExcel
    def RewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EventContentCardExcel
    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentCardExcel
    def RewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # EventContentCardExcel
    def RewardParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EventContentCardExcel
    def RewardParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EventContentCardExcel
    def RewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentCardExcel
    def RewardParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

def EventContentCardExcelStart(builder): builder.StartObject(7)
def EventContentCardExcelAddCardGroupId(builder, CardGroupId): builder.PrependInt32Slot(0, CardGroupId, 0)
def EventContentCardExcelAddEventContentId(builder, EventContentId): builder.PrependInt64Slot(1, EventContentId, 0)
def EventContentCardExcelAddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(2, LocalizeEtcId, 0)
def EventContentCardExcelAddIconPath(builder, IconPath): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(IconPath), 0)
def EventContentCardExcelAddBackIconPath(builder, BackIconPath): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(BackIconPath), 0)
def EventContentCardExcelAddRewardParcelType(builder, RewardParcelType): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelType), 0)
def EventContentCardExcelStartRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventContentCardExcelAddRewardParcelId(builder, RewardParcelId): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelId), 0)
def EventContentCardExcelStartRewardParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EventContentCardExcelEnd(builder): return builder.EndObject()
