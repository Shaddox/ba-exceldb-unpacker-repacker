# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FieldContentStageExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFieldContentStageExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FieldContentStageExcel()
        x.Init(buf, n + offset)
        return x

    # FieldContentStageExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FieldContentStageExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def AreaId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def StageDifficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FieldContentStageExcel
    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def StageEnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def StageEnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def StageEnterCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def StageTopography(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def RecommandLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def GroundID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def BGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def InstantClear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # FieldContentStageExcel
    def FixedEchelonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # FieldContentStageExcel
    def SkipFormationSettings(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def FieldContentStageExcelStart(builder): builder.StartObject(17)
def FieldContentStageExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def FieldContentStageExcelAddSeasonId(builder, SeasonId): builder.PrependInt64Slot(1, SeasonId, 0)
def FieldContentStageExcelAddAreaId(builder, AreaId): builder.PrependInt64Slot(2, AreaId, 0)
def FieldContentStageExcelAddGroupId(builder, GroupId): builder.PrependInt64Slot(3, GroupId, 0)
def FieldContentStageExcelAddStageDifficulty(builder, StageDifficulty): builder.PrependInt32Slot(4, StageDifficulty, 0)
def FieldContentStageExcelAddName(builder, Name): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)
def FieldContentStageExcelAddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(6, BattleDuration, 0)
def FieldContentStageExcelAddStageEnterCostType(builder, StageEnterCostType): builder.PrependInt32Slot(7, StageEnterCostType, 0)
def FieldContentStageExcelAddStageEnterCostId(builder, StageEnterCostId): builder.PrependInt64Slot(8, StageEnterCostId, 0)
def FieldContentStageExcelAddStageEnterCostAmount(builder, StageEnterCostAmount): builder.PrependInt32Slot(9, StageEnterCostAmount, 0)
def FieldContentStageExcelAddStageTopography(builder, StageTopography): builder.PrependInt32Slot(10, StageTopography, 0)
def FieldContentStageExcelAddRecommandLevel(builder, RecommandLevel): builder.PrependInt32Slot(11, RecommandLevel, 0)
def FieldContentStageExcelAddGroundID(builder, GroundID): builder.PrependInt64Slot(12, GroundID, 0)
def FieldContentStageExcelAddBGMId(builder, BGMId): builder.PrependInt64Slot(13, BGMId, 0)
def FieldContentStageExcelAddInstantClear(builder, InstantClear): builder.PrependBoolSlot(14, InstantClear, 0)
def FieldContentStageExcelAddFixedEchelonId(builder, FixedEchelonId): builder.PrependInt64Slot(15, FixedEchelonId, 0)
def FieldContentStageExcelAddSkipFormationSettings(builder, SkipFormationSettings): builder.PrependBoolSlot(16, SkipFormationSettings, 0)
def FieldContentStageExcelEnd(builder): return builder.EndObject()
