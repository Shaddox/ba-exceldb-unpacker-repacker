# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameTBGEncounterOptionExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMinigameTBGEncounterOptionExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameTBGEncounterOptionExcel()
        x.Init(buf, n + offset)
        return x

    # MinigameTBGEncounterOptionExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MinigameTBGEncounterOptionExcel
    def OptionGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterOptionExcel
    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterOptionExcel
    def SlotIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterOptionExcel
    def OptionTitleLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MinigameTBGEncounterOptionExcel
    def OptionSuccessLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MinigameTBGEncounterOptionExcel
    def OptionSuccessRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterOptionExcel
    def OptionSuccessOrHigherDiceCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterOptionExcel
    def OptionGreatSuccessOrHigherDiceCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterOptionExcel
    def OptionFailLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MinigameTBGEncounterOptionExcel
    def OptionFailLessDiceCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterOptionExcel
    def RunawayOrHigherDiceCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MinigameTBGEncounterOptionExcel
    def RewardHide(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def MinigameTBGEncounterOptionExcelStart(builder): builder.StartObject(12)
def MinigameTBGEncounterOptionExcelAddOptionGroupId(builder, OptionGroupId): builder.PrependInt64Slot(0, OptionGroupId, 0)
def MinigameTBGEncounterOptionExcelAddUniqueId(builder, UniqueId): builder.PrependInt64Slot(1, UniqueId, 0)
def MinigameTBGEncounterOptionExcelAddSlotIndex(builder, SlotIndex): builder.PrependInt32Slot(2, SlotIndex, 0)
def MinigameTBGEncounterOptionExcelAddOptionTitleLocalize(builder, OptionTitleLocalize): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(OptionTitleLocalize), 0)
def MinigameTBGEncounterOptionExcelAddOptionSuccessLocalize(builder, OptionSuccessLocalize): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(OptionSuccessLocalize), 0)
def MinigameTBGEncounterOptionExcelAddOptionSuccessRewardGroupId(builder, OptionSuccessRewardGroupId): builder.PrependInt64Slot(5, OptionSuccessRewardGroupId, 0)
def MinigameTBGEncounterOptionExcelAddOptionSuccessOrHigherDiceCount(builder, OptionSuccessOrHigherDiceCount): builder.PrependInt32Slot(6, OptionSuccessOrHigherDiceCount, 0)
def MinigameTBGEncounterOptionExcelAddOptionGreatSuccessOrHigherDiceCount(builder, OptionGreatSuccessOrHigherDiceCount): builder.PrependInt32Slot(7, OptionGreatSuccessOrHigherDiceCount, 0)
def MinigameTBGEncounterOptionExcelAddOptionFailLocalize(builder, OptionFailLocalize): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(OptionFailLocalize), 0)
def MinigameTBGEncounterOptionExcelAddOptionFailLessDiceCount(builder, OptionFailLessDiceCount): builder.PrependInt32Slot(9, OptionFailLessDiceCount, 0)
def MinigameTBGEncounterOptionExcelAddRunawayOrHigherDiceCount(builder, RunawayOrHigherDiceCount): builder.PrependInt32Slot(10, RunawayOrHigherDiceCount, 0)
def MinigameTBGEncounterOptionExcelAddRewardHide(builder, RewardHide): builder.PrependBoolSlot(11, RewardHide, 0)
def MinigameTBGEncounterOptionExcelEnd(builder): return builder.EndObject()
