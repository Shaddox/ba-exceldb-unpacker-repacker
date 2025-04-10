# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstCombatExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsConstCombatExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstCombatExcel()
        x.Init(buf, n + offset)
        return x

    # ConstCombatExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConstCombatExcel
    def SkillHandCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def DyingTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def BuffIconBlinkTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def ShowBufficonEXSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConstCombatExcel
    def ShowBufficonPassiveSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConstCombatExcel
    def ShowBufficonExtraPassiveSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConstCombatExcel
    def ShowBufficonLeaderSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConstCombatExcel
    def ShowBufficonGroundPassiveSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConstCombatExcel
    def SuppliesConditionStringId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstCombatExcel
    def PublicSpeechBubbleOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstCombatExcel
    def PublicSpeechBubbleOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstCombatExcel
    def PublicSpeechBubbleOffsetZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstCombatExcel
    def PublicSpeechDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstCombatExcel
    def ShowRaidListCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def MaxRaidTicketCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def MaxRaidBossSkillSlot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def EngageTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstCombatExcel
    def EngageWithSupporterTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstCombatExcel
    def VictoryTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstCombatExcel
    def TimeLimitAlarm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def EchelonMaxCommonCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def EchelonInitCommonCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def SkillSlotCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def EnemyRegenCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def ChampionRegenCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def PlayerRegenCostDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def CrowdControlFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def RaidOpenScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstCombatExcel
    def EliminateRaidOpenScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstCombatExcel
    def DefenceConstA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def DefenceConstB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def DefenceConstC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def DefenceConstD(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def AccuracyConstA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def AccuracyConstB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def AccuracyConstC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def AccuracyConstD(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def CriticalConstA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def CriticalConstB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def CriticalConstC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def CriticalConstD(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def MaxGroupBuffLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def EmojiDefaultTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def TimeLineActionRotateSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def BodyRotateSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def NormalTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def FastTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def BulletTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def UIDisplayDelayAfterSkillCutIn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(100))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def UseInitialRangeForCoverMove(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(102))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ConstCombatExcel
    def SlowTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(104))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def AimIKMinDegree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(106))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstCombatExcel
    def AimIKMaxDegree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(108))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstCombatExcel
    def MinimumClearTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def MinimumClearLevelGap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def CheckCheaterMaxUseCostNonArena(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def CheckCheaterMaxUseCostArena(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def AllowedMaxTimeScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(118))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def RandomAnimationOutput(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(120))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def SummonedTeleportDistance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def ArenaMinimumClearTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(124))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLELITTLE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(126))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLELITTLETw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(128))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLELITTLEAsia(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(130))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLELITTLENa(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(132))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLELITTLEGlobal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(134))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEMIDDLE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(136))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEMIDDLETw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(138))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEMIDDLEAsia(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(140))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEMIDDLENa(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(142))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEMIDDLEGlobal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(144))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEHIGH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(146))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEHIGHTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(148))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEHIGHAsia(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(150))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEHIGHNa(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(152))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEHIGHGlobal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(154))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEVERYHIGH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(156))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEVERYHIGHTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(158))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEVERYHIGHAsia(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(160))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEVERYHIGHNa(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(162))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WORLDBOSSBATTLEVERYHIGHGlobal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(164))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WorldRaidAutoSyncTermSecond(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(166))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WorldRaidBossHpDecreaseTerm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(168))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def WorldRaidBossParcelReactionDelay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(170))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def RaidRankingJumpMinimumWaitingTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(172))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def EffectTeleportDistance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(174))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstCombatExcel
    def AuraExitThresholdMargin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(176))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def TSAInteractionDamageFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(178))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def VictoryInteractionRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(180))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def EchelonExtensionEngageTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(182))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstCombatExcel
    def EchelonExtensionEngageWithSupporterTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(184))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstCombatExcel
    def EchelonExtensionVictoryTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(186))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstCombatExcel
    def EchelonExtensionEchelonMaxCommonCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(188))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def EchelonExtensionEchelonInitCommonCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(190))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def EchelonExtensionCostRegenRatio(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(192))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstCombatExcel
    def CheckCheaterMaxUseCostMultiFloorRaid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(194))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def ConstCombatExcelStart(builder): builder.StartObject(96)
def ConstCombatExcelAddSkillHandCount(builder, SkillHandCount): builder.PrependInt32Slot(0, SkillHandCount, 0)
def ConstCombatExcelAddDyingTime(builder, DyingTime): builder.PrependInt32Slot(1, DyingTime, 0)
def ConstCombatExcelAddBuffIconBlinkTime(builder, BuffIconBlinkTime): builder.PrependInt32Slot(2, BuffIconBlinkTime, 0)
def ConstCombatExcelAddShowBufficonEXSkill(builder, ShowBufficonEXSkill): builder.PrependBoolSlot(3, ShowBufficonEXSkill, 0)
def ConstCombatExcelAddShowBufficonPassiveSkill(builder, ShowBufficonPassiveSkill): builder.PrependBoolSlot(4, ShowBufficonPassiveSkill, 0)
def ConstCombatExcelAddShowBufficonExtraPassiveSkill(builder, ShowBufficonExtraPassiveSkill): builder.PrependBoolSlot(5, ShowBufficonExtraPassiveSkill, 0)
def ConstCombatExcelAddShowBufficonLeaderSkill(builder, ShowBufficonLeaderSkill): builder.PrependBoolSlot(6, ShowBufficonLeaderSkill, 0)
def ConstCombatExcelAddShowBufficonGroundPassiveSkill(builder, ShowBufficonGroundPassiveSkill): builder.PrependBoolSlot(7, ShowBufficonGroundPassiveSkill, 0)
def ConstCombatExcelAddSuppliesConditionStringId(builder, SuppliesConditionStringId): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(SuppliesConditionStringId), 0)
def ConstCombatExcelAddPublicSpeechBubbleOffsetX(builder, PublicSpeechBubbleOffsetX): builder.PrependFloat32Slot(9, PublicSpeechBubbleOffsetX, 0.0)
def ConstCombatExcelAddPublicSpeechBubbleOffsetY(builder, PublicSpeechBubbleOffsetY): builder.PrependFloat32Slot(10, PublicSpeechBubbleOffsetY, 0.0)
def ConstCombatExcelAddPublicSpeechBubbleOffsetZ(builder, PublicSpeechBubbleOffsetZ): builder.PrependFloat32Slot(11, PublicSpeechBubbleOffsetZ, 0.0)
def ConstCombatExcelAddPublicSpeechDuration(builder, PublicSpeechDuration): builder.PrependFloat32Slot(12, PublicSpeechDuration, 0.0)
def ConstCombatExcelAddShowRaidListCount(builder, ShowRaidListCount): builder.PrependInt32Slot(13, ShowRaidListCount, 0)
def ConstCombatExcelAddMaxRaidTicketCount(builder, MaxRaidTicketCount): builder.PrependInt64Slot(14, MaxRaidTicketCount, 0)
def ConstCombatExcelAddMaxRaidBossSkillSlot(builder, MaxRaidBossSkillSlot): builder.PrependInt64Slot(15, MaxRaidBossSkillSlot, 0)
def ConstCombatExcelAddEngageTimelinePath(builder, EngageTimelinePath): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(EngageTimelinePath), 0)
def ConstCombatExcelAddEngageWithSupporterTimelinePath(builder, EngageWithSupporterTimelinePath): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(EngageWithSupporterTimelinePath), 0)
def ConstCombatExcelAddVictoryTimelinePath(builder, VictoryTimelinePath): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryTimelinePath), 0)
def ConstCombatExcelAddTimeLimitAlarm(builder, TimeLimitAlarm): builder.PrependInt64Slot(19, TimeLimitAlarm, 0)
def ConstCombatExcelAddEchelonMaxCommonCost(builder, EchelonMaxCommonCost): builder.PrependInt32Slot(20, EchelonMaxCommonCost, 0)
def ConstCombatExcelAddEchelonInitCommonCost(builder, EchelonInitCommonCost): builder.PrependInt32Slot(21, EchelonInitCommonCost, 0)
def ConstCombatExcelAddSkillSlotCoolTime(builder, SkillSlotCoolTime): builder.PrependInt64Slot(22, SkillSlotCoolTime, 0)
def ConstCombatExcelAddEnemyRegenCost(builder, EnemyRegenCost): builder.PrependInt64Slot(23, EnemyRegenCost, 0)
def ConstCombatExcelAddChampionRegenCost(builder, ChampionRegenCost): builder.PrependInt64Slot(24, ChampionRegenCost, 0)
def ConstCombatExcelAddPlayerRegenCostDelay(builder, PlayerRegenCostDelay): builder.PrependInt64Slot(25, PlayerRegenCostDelay, 0)
def ConstCombatExcelAddCrowdControlFactor(builder, CrowdControlFactor): builder.PrependInt64Slot(26, CrowdControlFactor, 0)
def ConstCombatExcelAddRaidOpenScenarioId(builder, RaidOpenScenarioId): builder.PrependUOffsetTRelativeSlot(27, flatbuffers.number_types.UOffsetTFlags.py_type(RaidOpenScenarioId), 0)
def ConstCombatExcelAddEliminateRaidOpenScenarioId(builder, EliminateRaidOpenScenarioId): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(EliminateRaidOpenScenarioId), 0)
def ConstCombatExcelAddDefenceConstA(builder, DefenceConstA): builder.PrependInt64Slot(29, DefenceConstA, 0)
def ConstCombatExcelAddDefenceConstB(builder, DefenceConstB): builder.PrependInt64Slot(30, DefenceConstB, 0)
def ConstCombatExcelAddDefenceConstC(builder, DefenceConstC): builder.PrependInt64Slot(31, DefenceConstC, 0)
def ConstCombatExcelAddDefenceConstD(builder, DefenceConstD): builder.PrependInt64Slot(32, DefenceConstD, 0)
def ConstCombatExcelAddAccuracyConstA(builder, AccuracyConstA): builder.PrependInt64Slot(33, AccuracyConstA, 0)
def ConstCombatExcelAddAccuracyConstB(builder, AccuracyConstB): builder.PrependInt64Slot(34, AccuracyConstB, 0)
def ConstCombatExcelAddAccuracyConstC(builder, AccuracyConstC): builder.PrependInt64Slot(35, AccuracyConstC, 0)
def ConstCombatExcelAddAccuracyConstD(builder, AccuracyConstD): builder.PrependInt64Slot(36, AccuracyConstD, 0)
def ConstCombatExcelAddCriticalConstA(builder, CriticalConstA): builder.PrependInt64Slot(37, CriticalConstA, 0)
def ConstCombatExcelAddCriticalConstB(builder, CriticalConstB): builder.PrependInt64Slot(38, CriticalConstB, 0)
def ConstCombatExcelAddCriticalConstC(builder, CriticalConstC): builder.PrependInt64Slot(39, CriticalConstC, 0)
def ConstCombatExcelAddCriticalConstD(builder, CriticalConstD): builder.PrependInt64Slot(40, CriticalConstD, 0)
def ConstCombatExcelAddMaxGroupBuffLevel(builder, MaxGroupBuffLevel): builder.PrependInt32Slot(41, MaxGroupBuffLevel, 0)
def ConstCombatExcelAddEmojiDefaultTime(builder, EmojiDefaultTime): builder.PrependInt32Slot(42, EmojiDefaultTime, 0)
def ConstCombatExcelAddTimeLineActionRotateSpeed(builder, TimeLineActionRotateSpeed): builder.PrependInt64Slot(43, TimeLineActionRotateSpeed, 0)
def ConstCombatExcelAddBodyRotateSpeed(builder, BodyRotateSpeed): builder.PrependInt64Slot(44, BodyRotateSpeed, 0)
def ConstCombatExcelAddNormalTimeScale(builder, NormalTimeScale): builder.PrependInt64Slot(45, NormalTimeScale, 0)
def ConstCombatExcelAddFastTimeScale(builder, FastTimeScale): builder.PrependInt64Slot(46, FastTimeScale, 0)
def ConstCombatExcelAddBulletTimeScale(builder, BulletTimeScale): builder.PrependInt64Slot(47, BulletTimeScale, 0)
def ConstCombatExcelAddUIDisplayDelayAfterSkillCutIn(builder, UIDisplayDelayAfterSkillCutIn): builder.PrependInt64Slot(48, UIDisplayDelayAfterSkillCutIn, 0)
def ConstCombatExcelAddUseInitialRangeForCoverMove(builder, UseInitialRangeForCoverMove): builder.PrependBoolSlot(49, UseInitialRangeForCoverMove, 0)
def ConstCombatExcelAddSlowTimeScale(builder, SlowTimeScale): builder.PrependInt64Slot(50, SlowTimeScale, 0)
def ConstCombatExcelAddAimIKMinDegree(builder, AimIKMinDegree): builder.PrependFloat32Slot(51, AimIKMinDegree, 0.0)
def ConstCombatExcelAddAimIKMaxDegree(builder, AimIKMaxDegree): builder.PrependFloat32Slot(52, AimIKMaxDegree, 0.0)
def ConstCombatExcelAddMinimumClearTime(builder, MinimumClearTime): builder.PrependInt32Slot(53, MinimumClearTime, 0)
def ConstCombatExcelAddMinimumClearLevelGap(builder, MinimumClearLevelGap): builder.PrependInt32Slot(54, MinimumClearLevelGap, 0)
def ConstCombatExcelAddCheckCheaterMaxUseCostNonArena(builder, CheckCheaterMaxUseCostNonArena): builder.PrependInt32Slot(55, CheckCheaterMaxUseCostNonArena, 0)
def ConstCombatExcelAddCheckCheaterMaxUseCostArena(builder, CheckCheaterMaxUseCostArena): builder.PrependInt32Slot(56, CheckCheaterMaxUseCostArena, 0)
def ConstCombatExcelAddAllowedMaxTimeScale(builder, AllowedMaxTimeScale): builder.PrependInt64Slot(57, AllowedMaxTimeScale, 0)
def ConstCombatExcelAddRandomAnimationOutput(builder, RandomAnimationOutput): builder.PrependInt64Slot(58, RandomAnimationOutput, 0)
def ConstCombatExcelAddSummonedTeleportDistance(builder, SummonedTeleportDistance): builder.PrependInt64Slot(59, SummonedTeleportDistance, 0)
def ConstCombatExcelAddArenaMinimumClearTime(builder, ArenaMinimumClearTime): builder.PrependInt32Slot(60, ArenaMinimumClearTime, 0)
def ConstCombatExcelAddWORLDBOSSBATTLELITTLE(builder, WORLDBOSSBATTLELITTLE): builder.PrependInt64Slot(61, WORLDBOSSBATTLELITTLE, 0)
def ConstCombatExcelAddWORLDBOSSBATTLELITTLETw(builder, WORLDBOSSBATTLELITTLETw): builder.PrependInt64Slot(62, WORLDBOSSBATTLELITTLETw, 0)
def ConstCombatExcelAddWORLDBOSSBATTLELITTLEAsia(builder, WORLDBOSSBATTLELITTLEAsia): builder.PrependInt64Slot(63, WORLDBOSSBATTLELITTLEAsia, 0)
def ConstCombatExcelAddWORLDBOSSBATTLELITTLENa(builder, WORLDBOSSBATTLELITTLENa): builder.PrependInt64Slot(64, WORLDBOSSBATTLELITTLENa, 0)
def ConstCombatExcelAddWORLDBOSSBATTLELITTLEGlobal(builder, WORLDBOSSBATTLELITTLEGlobal): builder.PrependInt64Slot(65, WORLDBOSSBATTLELITTLEGlobal, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEMIDDLE(builder, WORLDBOSSBATTLEMIDDLE): builder.PrependInt64Slot(66, WORLDBOSSBATTLEMIDDLE, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEMIDDLETw(builder, WORLDBOSSBATTLEMIDDLETw): builder.PrependInt64Slot(67, WORLDBOSSBATTLEMIDDLETw, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEMIDDLEAsia(builder, WORLDBOSSBATTLEMIDDLEAsia): builder.PrependInt64Slot(68, WORLDBOSSBATTLEMIDDLEAsia, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEMIDDLENa(builder, WORLDBOSSBATTLEMIDDLENa): builder.PrependInt64Slot(69, WORLDBOSSBATTLEMIDDLENa, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEMIDDLEGlobal(builder, WORLDBOSSBATTLEMIDDLEGlobal): builder.PrependInt64Slot(70, WORLDBOSSBATTLEMIDDLEGlobal, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEHIGH(builder, WORLDBOSSBATTLEHIGH): builder.PrependInt64Slot(71, WORLDBOSSBATTLEHIGH, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEHIGHTw(builder, WORLDBOSSBATTLEHIGHTw): builder.PrependInt64Slot(72, WORLDBOSSBATTLEHIGHTw, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEHIGHAsia(builder, WORLDBOSSBATTLEHIGHAsia): builder.PrependInt64Slot(73, WORLDBOSSBATTLEHIGHAsia, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEHIGHNa(builder, WORLDBOSSBATTLEHIGHNa): builder.PrependInt64Slot(74, WORLDBOSSBATTLEHIGHNa, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEHIGHGlobal(builder, WORLDBOSSBATTLEHIGHGlobal): builder.PrependInt64Slot(75, WORLDBOSSBATTLEHIGHGlobal, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEVERYHIGH(builder, WORLDBOSSBATTLEVERYHIGH): builder.PrependInt64Slot(76, WORLDBOSSBATTLEVERYHIGH, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEVERYHIGHTw(builder, WORLDBOSSBATTLEVERYHIGHTw): builder.PrependInt64Slot(77, WORLDBOSSBATTLEVERYHIGHTw, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEVERYHIGHAsia(builder, WORLDBOSSBATTLEVERYHIGHAsia): builder.PrependInt64Slot(78, WORLDBOSSBATTLEVERYHIGHAsia, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEVERYHIGHNa(builder, WORLDBOSSBATTLEVERYHIGHNa): builder.PrependInt64Slot(79, WORLDBOSSBATTLEVERYHIGHNa, 0)
def ConstCombatExcelAddWORLDBOSSBATTLEVERYHIGHGlobal(builder, WORLDBOSSBATTLEVERYHIGHGlobal): builder.PrependInt64Slot(80, WORLDBOSSBATTLEVERYHIGHGlobal, 0)
def ConstCombatExcelAddWorldRaidAutoSyncTermSecond(builder, WorldRaidAutoSyncTermSecond): builder.PrependInt64Slot(81, WorldRaidAutoSyncTermSecond, 0)
def ConstCombatExcelAddWorldRaidBossHpDecreaseTerm(builder, WorldRaidBossHpDecreaseTerm): builder.PrependInt64Slot(82, WorldRaidBossHpDecreaseTerm, 0)
def ConstCombatExcelAddWorldRaidBossParcelReactionDelay(builder, WorldRaidBossParcelReactionDelay): builder.PrependInt64Slot(83, WorldRaidBossParcelReactionDelay, 0)
def ConstCombatExcelAddRaidRankingJumpMinimumWaitingTime(builder, RaidRankingJumpMinimumWaitingTime): builder.PrependInt64Slot(84, RaidRankingJumpMinimumWaitingTime, 0)
def ConstCombatExcelAddEffectTeleportDistance(builder, EffectTeleportDistance): builder.PrependFloat32Slot(85, EffectTeleportDistance, 0.0)
def ConstCombatExcelAddAuraExitThresholdMargin(builder, AuraExitThresholdMargin): builder.PrependInt64Slot(86, AuraExitThresholdMargin, 0)
def ConstCombatExcelAddTSAInteractionDamageFactor(builder, TSAInteractionDamageFactor): builder.PrependInt64Slot(87, TSAInteractionDamageFactor, 0)
def ConstCombatExcelAddVictoryInteractionRate(builder, VictoryInteractionRate): builder.PrependInt64Slot(88, VictoryInteractionRate, 0)
def ConstCombatExcelAddEchelonExtensionEngageTimelinePath(builder, EchelonExtensionEngageTimelinePath): builder.PrependUOffsetTRelativeSlot(89, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonExtensionEngageTimelinePath), 0)
def ConstCombatExcelAddEchelonExtensionEngageWithSupporterTimelinePath(builder, EchelonExtensionEngageWithSupporterTimelinePath): builder.PrependUOffsetTRelativeSlot(90, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonExtensionEngageWithSupporterTimelinePath), 0)
def ConstCombatExcelAddEchelonExtensionVictoryTimelinePath(builder, EchelonExtensionVictoryTimelinePath): builder.PrependUOffsetTRelativeSlot(91, flatbuffers.number_types.UOffsetTFlags.py_type(EchelonExtensionVictoryTimelinePath), 0)
def ConstCombatExcelAddEchelonExtensionEchelonMaxCommonCost(builder, EchelonExtensionEchelonMaxCommonCost): builder.PrependInt32Slot(92, EchelonExtensionEchelonMaxCommonCost, 0)
def ConstCombatExcelAddEchelonExtensionEchelonInitCommonCost(builder, EchelonExtensionEchelonInitCommonCost): builder.PrependInt32Slot(93, EchelonExtensionEchelonInitCommonCost, 0)
def ConstCombatExcelAddEchelonExtensionCostRegenRatio(builder, EchelonExtensionCostRegenRatio): builder.PrependInt64Slot(94, EchelonExtensionCostRegenRatio, 0)
def ConstCombatExcelAddCheckCheaterMaxUseCostMultiFloorRaid(builder, CheckCheaterMaxUseCostMultiFloorRaid): builder.PrependInt32Slot(95, CheckCheaterMaxUseCostMultiFloorRaid, 0)
def ConstCombatExcelEnd(builder): return builder.EndObject()
