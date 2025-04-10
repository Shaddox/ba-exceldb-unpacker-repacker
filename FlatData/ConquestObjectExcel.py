# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestObjectExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsConquestObjectExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestObjectExcel()
        x.Init(buf, n + offset)
        return x

    # ConquestObjectExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConquestObjectExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestObjectExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestObjectExcel
    def ConquestObjectType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestObjectExcel
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # ConquestObjectExcel
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestObjectExcel
    def PrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConquestObjectExcel
    def ConquestRewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestObjectExcel
    def ConquestRewardID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestObjectExcel
    def ConquestRewardAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestObjectExcel
    def Disposable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConquestObjectExcel
    def StepIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConquestObjectExcel
    def StepObjectCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def ConquestObjectExcelStart(builder): builder.StartObject(12)
def ConquestObjectExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def ConquestObjectExcelAddEventContentId(builder, EventContentId): builder.PrependInt64Slot(1, EventContentId, 0)
def ConquestObjectExcelAddConquestObjectType(builder, ConquestObjectType): builder.PrependInt32Slot(2, ConquestObjectType, 0)
def ConquestObjectExcelAddKey(builder, Key): builder.PrependUint32Slot(3, Key, 0)
def ConquestObjectExcelAddName(builder, Name): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)
def ConquestObjectExcelAddPrefabName(builder, PrefabName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(PrefabName), 0)
def ConquestObjectExcelAddConquestRewardParcelType(builder, ConquestRewardParcelType): builder.PrependInt32Slot(6, ConquestRewardParcelType, 0)
def ConquestObjectExcelAddConquestRewardID(builder, ConquestRewardID): builder.PrependInt64Slot(7, ConquestRewardID, 0)
def ConquestObjectExcelAddConquestRewardAmount(builder, ConquestRewardAmount): builder.PrependInt32Slot(8, ConquestRewardAmount, 0)
def ConquestObjectExcelAddDisposable(builder, Disposable): builder.PrependBoolSlot(9, Disposable, 0)
def ConquestObjectExcelAddStepIndex(builder, StepIndex): builder.PrependInt32Slot(10, StepIndex, 0)
def ConquestObjectExcelAddStepObjectCount(builder, StepObjectCount): builder.PrependInt32Slot(11, StepObjectCount, 0)
def ConquestObjectExcelEnd(builder): return builder.EndObject()
