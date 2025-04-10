# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ScenarioContentCollectionExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsScenarioContentCollectionExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ScenarioContentCollectionExcel()
        x.Init(buf, n + offset)
        return x

    # ScenarioContentCollectionExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ScenarioContentCollectionExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ScenarioContentCollectionExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ScenarioContentCollectionExcel
    def UnlockConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ScenarioContentCollectionExcel
    def UnlockConditionParameter(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ScenarioContentCollectionExcel
    def UnlockConditionParameterAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ScenarioContentCollectionExcel
    def UnlockConditionParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ScenarioContentCollectionExcel
    def UnlockConditionParameterIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # ScenarioContentCollectionExcel
    def MultipleConditionCheckType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ScenarioContentCollectionExcel
    def UnlockConditionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ScenarioContentCollectionExcel
    def IsObject(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ScenarioContentCollectionExcel
    def IsHorizon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ScenarioContentCollectionExcel
    def EmblemResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ScenarioContentCollectionExcel
    def ThumbResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ScenarioContentCollectionExcel
    def FullResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ScenarioContentCollectionExcel
    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # ScenarioContentCollectionExcel
    def SubNameLocalizeCodeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ScenarioContentCollectionExcelStart(builder): builder.StartObject(13)
def ScenarioContentCollectionExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def ScenarioContentCollectionExcelAddGroupId(builder, GroupId): builder.PrependInt64Slot(1, GroupId, 0)
def ScenarioContentCollectionExcelAddUnlockConditionType(builder, UnlockConditionType): builder.PrependInt32Slot(2, UnlockConditionType, 0)
def ScenarioContentCollectionExcelAddUnlockConditionParameter(builder, UnlockConditionParameter): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(UnlockConditionParameter), 0)
def ScenarioContentCollectionExcelStartUnlockConditionParameterVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ScenarioContentCollectionExcelAddMultipleConditionCheckType(builder, MultipleConditionCheckType): builder.PrependInt32Slot(4, MultipleConditionCheckType, 0)
def ScenarioContentCollectionExcelAddUnlockConditionCount(builder, UnlockConditionCount): builder.PrependInt64Slot(5, UnlockConditionCount, 0)
def ScenarioContentCollectionExcelAddIsObject(builder, IsObject): builder.PrependBoolSlot(6, IsObject, 0)
def ScenarioContentCollectionExcelAddIsHorizon(builder, IsHorizon): builder.PrependBoolSlot(7, IsHorizon, 0)
def ScenarioContentCollectionExcelAddEmblemResource(builder, EmblemResource): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(EmblemResource), 0)
def ScenarioContentCollectionExcelAddThumbResource(builder, ThumbResource): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(ThumbResource), 0)
def ScenarioContentCollectionExcelAddFullResource(builder, FullResource): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(FullResource), 0)
def ScenarioContentCollectionExcelAddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(11, LocalizeEtcId, 0)
def ScenarioContentCollectionExcelAddSubNameLocalizeCodeId(builder, SubNameLocalizeCodeId): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(SubNameLocalizeCodeId), 0)
def ScenarioContentCollectionExcelEnd(builder): return builder.EndObject()
