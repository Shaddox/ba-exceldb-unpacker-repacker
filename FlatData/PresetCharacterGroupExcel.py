# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PresetCharacterGroupExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPresetCharacterGroupExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PresetCharacterGroupExcel()
        x.Init(buf, n + offset)
        return x

    # PresetCharacterGroupExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PresetCharacterGroupExcel
    def PresetCharacterGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def GetPresetType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # PresetCharacterGroupExcel
    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def Exp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def FavorExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def FavorRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def StarGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def ExSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def PassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def ExtraPassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def CommonSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def LeaderSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def EquipSlot01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # PresetCharacterGroupExcel
    def EquipSlotTier01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def EquipSlotLevel01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def EquipSlot02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # PresetCharacterGroupExcel
    def EquipSlotTier02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def EquipSlotLevel02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def EquipSlot03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # PresetCharacterGroupExcel
    def EquipSlotTier03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def EquipSlotLevel03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def EquipCharacterWeapon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # PresetCharacterGroupExcel
    def EquipCharacterWeaponTier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def EquipCharacterWeaponLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def EquipCharacterGear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # PresetCharacterGroupExcel
    def EquipCharacterGearTier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def EquipCharacterGearLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def PotentialType01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def PotentialLevel01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def PotentialType02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def PotentialLevel02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def PotentialType03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # PresetCharacterGroupExcel
    def PotentialLevel03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def PresetCharacterGroupExcelStart(builder): builder.StartObject(33)
def PresetCharacterGroupExcelAddPresetCharacterGroupId(builder, PresetCharacterGroupId): builder.PrependInt64Slot(0, PresetCharacterGroupId, 0)
def PresetCharacterGroupExcelAddGetPresetType(builder, GetPresetType): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(GetPresetType), 0)
def PresetCharacterGroupExcelAddLevel(builder, Level): builder.PrependInt32Slot(2, Level, 0)
def PresetCharacterGroupExcelAddExp(builder, Exp): builder.PrependInt32Slot(3, Exp, 0)
def PresetCharacterGroupExcelAddFavorExp(builder, FavorExp): builder.PrependInt32Slot(4, FavorExp, 0)
def PresetCharacterGroupExcelAddFavorRank(builder, FavorRank): builder.PrependInt32Slot(5, FavorRank, 0)
def PresetCharacterGroupExcelAddStarGrade(builder, StarGrade): builder.PrependInt32Slot(6, StarGrade, 0)
def PresetCharacterGroupExcelAddExSkillLevel(builder, ExSkillLevel): builder.PrependInt32Slot(7, ExSkillLevel, 0)
def PresetCharacterGroupExcelAddPassiveSkillLevel(builder, PassiveSkillLevel): builder.PrependInt32Slot(8, PassiveSkillLevel, 0)
def PresetCharacterGroupExcelAddExtraPassiveSkillLevel(builder, ExtraPassiveSkillLevel): builder.PrependInt32Slot(9, ExtraPassiveSkillLevel, 0)
def PresetCharacterGroupExcelAddCommonSkillLevel(builder, CommonSkillLevel): builder.PrependInt32Slot(10, CommonSkillLevel, 0)
def PresetCharacterGroupExcelAddLeaderSkillLevel(builder, LeaderSkillLevel): builder.PrependInt32Slot(11, LeaderSkillLevel, 0)
def PresetCharacterGroupExcelAddEquipSlot01(builder, EquipSlot01): builder.PrependBoolSlot(12, EquipSlot01, 0)
def PresetCharacterGroupExcelAddEquipSlotTier01(builder, EquipSlotTier01): builder.PrependInt32Slot(13, EquipSlotTier01, 0)
def PresetCharacterGroupExcelAddEquipSlotLevel01(builder, EquipSlotLevel01): builder.PrependInt32Slot(14, EquipSlotLevel01, 0)
def PresetCharacterGroupExcelAddEquipSlot02(builder, EquipSlot02): builder.PrependBoolSlot(15, EquipSlot02, 0)
def PresetCharacterGroupExcelAddEquipSlotTier02(builder, EquipSlotTier02): builder.PrependInt32Slot(16, EquipSlotTier02, 0)
def PresetCharacterGroupExcelAddEquipSlotLevel02(builder, EquipSlotLevel02): builder.PrependInt32Slot(17, EquipSlotLevel02, 0)
def PresetCharacterGroupExcelAddEquipSlot03(builder, EquipSlot03): builder.PrependBoolSlot(18, EquipSlot03, 0)
def PresetCharacterGroupExcelAddEquipSlotTier03(builder, EquipSlotTier03): builder.PrependInt32Slot(19, EquipSlotTier03, 0)
def PresetCharacterGroupExcelAddEquipSlotLevel03(builder, EquipSlotLevel03): builder.PrependInt32Slot(20, EquipSlotLevel03, 0)
def PresetCharacterGroupExcelAddEquipCharacterWeapon(builder, EquipCharacterWeapon): builder.PrependBoolSlot(21, EquipCharacterWeapon, 0)
def PresetCharacterGroupExcelAddEquipCharacterWeaponTier(builder, EquipCharacterWeaponTier): builder.PrependInt32Slot(22, EquipCharacterWeaponTier, 0)
def PresetCharacterGroupExcelAddEquipCharacterWeaponLevel(builder, EquipCharacterWeaponLevel): builder.PrependInt32Slot(23, EquipCharacterWeaponLevel, 0)
def PresetCharacterGroupExcelAddEquipCharacterGear(builder, EquipCharacterGear): builder.PrependBoolSlot(24, EquipCharacterGear, 0)
def PresetCharacterGroupExcelAddEquipCharacterGearTier(builder, EquipCharacterGearTier): builder.PrependInt32Slot(25, EquipCharacterGearTier, 0)
def PresetCharacterGroupExcelAddEquipCharacterGearLevel(builder, EquipCharacterGearLevel): builder.PrependInt32Slot(26, EquipCharacterGearLevel, 0)
def PresetCharacterGroupExcelAddPotentialType01(builder, PotentialType01): builder.PrependInt32Slot(27, PotentialType01, 0)
def PresetCharacterGroupExcelAddPotentialLevel01(builder, PotentialLevel01): builder.PrependInt32Slot(28, PotentialLevel01, 0)
def PresetCharacterGroupExcelAddPotentialType02(builder, PotentialType02): builder.PrependInt32Slot(29, PotentialType02, 0)
def PresetCharacterGroupExcelAddPotentialLevel02(builder, PotentialLevel02): builder.PrependInt32Slot(30, PotentialLevel02, 0)
def PresetCharacterGroupExcelAddPotentialType03(builder, PotentialType03): builder.PrependInt32Slot(31, PotentialType03, 0)
def PresetCharacterGroupExcelAddPotentialLevel03(builder, PotentialLevel03): builder.PrependInt32Slot(32, PotentialLevel03, 0)
def PresetCharacterGroupExcelEnd(builder): return builder.EndObject()
