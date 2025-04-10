# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WorldRaidStageExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsWorldRaidStageExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WorldRaidStageExcel()
        x.Init(buf, n + offset)
        return x

    # WorldRaidStageExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # WorldRaidStageExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def UseBossIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WorldRaidStageExcel
    def UseBossAIPhaseSync(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WorldRaidStageExcel
    def WorldRaidBossGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def PortraitPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WorldRaidStageExcel
    def BGPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WorldRaidStageExcel
    def RaidCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def BossCharacterId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # WorldRaidStageExcel
    def BossCharacterIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # WorldRaidStageExcel
    def BossCharacterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # WorldRaidStageExcel
    def BossCharacterIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

    # WorldRaidStageExcel
    def AssistCharacterLimitCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def WorldRaidDifficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def DifficultyOpenCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WorldRaidStageExcel
    def RaidEnterAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def ReEnterAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def RaidBattleEndRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def RaidRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def BattleReadyTimelinePath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # WorldRaidStageExcel
    def BattleReadyTimelinePathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # WorldRaidStageExcel
    def BattleReadyTimelinePathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0

    # WorldRaidStageExcel
    def BattleReadyTimelinePhaseStart(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # WorldRaidStageExcel
    def BattleReadyTimelinePhaseStartAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # WorldRaidStageExcel
    def BattleReadyTimelinePhaseStartLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # WorldRaidStageExcel
    def BattleReadyTimelinePhaseStartIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        return o == 0

    # WorldRaidStageExcel
    def BattleReadyTimelinePhaseEnd(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # WorldRaidStageExcel
    def BattleReadyTimelinePhaseEndAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # WorldRaidStageExcel
    def BattleReadyTimelinePhaseEndLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # WorldRaidStageExcel
    def BattleReadyTimelinePhaseEndIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        return o == 0

    # WorldRaidStageExcel
    def VictoryTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WorldRaidStageExcel
    def PhaseChangeTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WorldRaidStageExcel
    def TimeLinePhase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def EnterScenarioKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def ClearScenarioKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def UseFixedEchelon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WorldRaidStageExcel
    def FixedEchelonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def IsRaidScenarioBattle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WorldRaidStageExcel
    def ShowSkillCard(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WorldRaidStageExcel
    def BossBGInfoKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def DamageToWorldBoss(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WorldRaidStageExcel
    def AllyPassiveSkill(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # WorldRaidStageExcel
    def AllyPassiveSkillLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # WorldRaidStageExcel
    def AllyPassiveSkillIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        return o == 0

    # WorldRaidStageExcel
    def AllyPassiveSkillLevel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # WorldRaidStageExcel
    def AllyPassiveSkillLevelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # WorldRaidStageExcel
    def AllyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # WorldRaidStageExcel
    def AllyPassiveSkillLevelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        return o == 0

    # WorldRaidStageExcel
    def SaveCurrentLocalBossHP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WorldRaidStageExcel
    def EchelonExtensionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def WorldRaidStageExcelStart(builder): builder.StartObject(35)
def WorldRaidStageExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def WorldRaidStageExcelAddUseBossIndex(builder, UseBossIndex): builder.PrependBoolSlot(1, UseBossIndex, 0)
def WorldRaidStageExcelAddUseBossAIPhaseSync(builder, UseBossAIPhaseSync): builder.PrependBoolSlot(2, UseBossAIPhaseSync, 0)
def WorldRaidStageExcelAddWorldRaidBossGroupId(builder, WorldRaidBossGroupId): builder.PrependInt64Slot(3, WorldRaidBossGroupId, 0)
def WorldRaidStageExcelAddPortraitPath(builder, PortraitPath): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(PortraitPath), 0)
def WorldRaidStageExcelAddBGPath(builder, BGPath): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(BGPath), 0)
def WorldRaidStageExcelAddRaidCharacterId(builder, RaidCharacterId): builder.PrependInt64Slot(6, RaidCharacterId, 0)
def WorldRaidStageExcelAddBossCharacterId(builder, BossCharacterId): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(BossCharacterId), 0)
def WorldRaidStageExcelStartBossCharacterIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def WorldRaidStageExcelAddAssistCharacterLimitCount(builder, AssistCharacterLimitCount): builder.PrependInt64Slot(8, AssistCharacterLimitCount, 0)
def WorldRaidStageExcelAddWorldRaidDifficulty(builder, WorldRaidDifficulty): builder.PrependInt32Slot(9, WorldRaidDifficulty, 0)
def WorldRaidStageExcelAddDifficultyOpenCondition(builder, DifficultyOpenCondition): builder.PrependBoolSlot(10, DifficultyOpenCondition, 0)
def WorldRaidStageExcelAddRaidEnterAmount(builder, RaidEnterAmount): builder.PrependInt64Slot(11, RaidEnterAmount, 0)
def WorldRaidStageExcelAddReEnterAmount(builder, ReEnterAmount): builder.PrependInt64Slot(12, ReEnterAmount, 0)
def WorldRaidStageExcelAddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(13, BattleDuration, 0)
def WorldRaidStageExcelAddGroundId(builder, GroundId): builder.PrependInt64Slot(14, GroundId, 0)
def WorldRaidStageExcelAddRaidBattleEndRewardGroupId(builder, RaidBattleEndRewardGroupId): builder.PrependInt64Slot(15, RaidBattleEndRewardGroupId, 0)
def WorldRaidStageExcelAddRaidRewardGroupId(builder, RaidRewardGroupId): builder.PrependInt64Slot(16, RaidRewardGroupId, 0)
def WorldRaidStageExcelAddBattleReadyTimelinePath(builder, BattleReadyTimelinePath): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePath), 0)
def WorldRaidStageExcelStartBattleReadyTimelinePathVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def WorldRaidStageExcelAddBattleReadyTimelinePhaseStart(builder, BattleReadyTimelinePhaseStart): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePhaseStart), 0)
def WorldRaidStageExcelStartBattleReadyTimelinePhaseStartVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def WorldRaidStageExcelAddBattleReadyTimelinePhaseEnd(builder, BattleReadyTimelinePhaseEnd): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePhaseEnd), 0)
def WorldRaidStageExcelStartBattleReadyTimelinePhaseEndVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def WorldRaidStageExcelAddVictoryTimelinePath(builder, VictoryTimelinePath): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryTimelinePath), 0)
def WorldRaidStageExcelAddPhaseChangeTimelinePath(builder, PhaseChangeTimelinePath): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseChangeTimelinePath), 0)
def WorldRaidStageExcelAddTimeLinePhase(builder, TimeLinePhase): builder.PrependInt64Slot(22, TimeLinePhase, 0)
def WorldRaidStageExcelAddEnterScenarioKey(builder, EnterScenarioKey): builder.PrependInt64Slot(23, EnterScenarioKey, 0)
def WorldRaidStageExcelAddClearScenarioKey(builder, ClearScenarioKey): builder.PrependInt64Slot(24, ClearScenarioKey, 0)
def WorldRaidStageExcelAddUseFixedEchelon(builder, UseFixedEchelon): builder.PrependBoolSlot(25, UseFixedEchelon, 0)
def WorldRaidStageExcelAddFixedEchelonId(builder, FixedEchelonId): builder.PrependInt64Slot(26, FixedEchelonId, 0)
def WorldRaidStageExcelAddIsRaidScenarioBattle(builder, IsRaidScenarioBattle): builder.PrependBoolSlot(27, IsRaidScenarioBattle, 0)
def WorldRaidStageExcelAddShowSkillCard(builder, ShowSkillCard): builder.PrependBoolSlot(28, ShowSkillCard, 0)
def WorldRaidStageExcelAddBossBGInfoKey(builder, BossBGInfoKey): builder.PrependUint32Slot(29, BossBGInfoKey, 0)
def WorldRaidStageExcelAddDamageToWorldBoss(builder, DamageToWorldBoss): builder.PrependInt64Slot(30, DamageToWorldBoss, 0)
def WorldRaidStageExcelAddAllyPassiveSkill(builder, AllyPassiveSkill): builder.PrependUOffsetTRelativeSlot(31, flatbuffers.number_types.UOffsetTFlags.py_type(AllyPassiveSkill), 0)
def WorldRaidStageExcelStartAllyPassiveSkillVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def WorldRaidStageExcelAddAllyPassiveSkillLevel(builder, AllyPassiveSkillLevel): builder.PrependUOffsetTRelativeSlot(32, flatbuffers.number_types.UOffsetTFlags.py_type(AllyPassiveSkillLevel), 0)
def WorldRaidStageExcelStartAllyPassiveSkillLevelVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def WorldRaidStageExcelAddSaveCurrentLocalBossHP(builder, SaveCurrentLocalBossHP): builder.PrependBoolSlot(33, SaveCurrentLocalBossHP, 0)
def WorldRaidStageExcelAddEchelonExtensionType(builder, EchelonExtensionType): builder.PrependInt32Slot(34, EchelonExtensionType, 0)
def WorldRaidStageExcelEnd(builder): return builder.EndObject()
