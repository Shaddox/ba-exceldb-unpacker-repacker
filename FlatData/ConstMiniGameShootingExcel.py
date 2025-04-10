# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstMiniGameShootingExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsConstMiniGameShootingExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstMiniGameShootingExcel()
        x.Init(buf, n + offset)
        return x

    # ConstMiniGameShootingExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConstMiniGameShootingExcel
    def NormalStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstMiniGameShootingExcel
    def NormalSectionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstMiniGameShootingExcel
    def HardStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstMiniGameShootingExcel
    def HardSectionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstMiniGameShootingExcel
    def FreeStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstMiniGameShootingExcel
    def FreeSectionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstMiniGameShootingExcel
    def PlayerCharacterId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ConstMiniGameShootingExcel
    def PlayerCharacterIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ConstMiniGameShootingExcel
    def PlayerCharacterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConstMiniGameShootingExcel
    def PlayerCharacterIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # ConstMiniGameShootingExcel
    def HiddenPlayerCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConstMiniGameShootingExcel
    def CameraSmoothTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMiniGameShootingExcel
    def SpawnEffectPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstMiniGameShootingExcel
    def WaitTimeAfterSpawn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConstMiniGameShootingExcel
    def FreeGearInterval(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def ConstMiniGameShootingExcelStart(builder): builder.StartObject(12)
def ConstMiniGameShootingExcelAddNormalStageId(builder, NormalStageId): builder.PrependInt64Slot(0, NormalStageId, 0)
def ConstMiniGameShootingExcelAddNormalSectionCount(builder, NormalSectionCount): builder.PrependInt32Slot(1, NormalSectionCount, 0)
def ConstMiniGameShootingExcelAddHardStageId(builder, HardStageId): builder.PrependInt64Slot(2, HardStageId, 0)
def ConstMiniGameShootingExcelAddHardSectionCount(builder, HardSectionCount): builder.PrependInt32Slot(3, HardSectionCount, 0)
def ConstMiniGameShootingExcelAddFreeStageId(builder, FreeStageId): builder.PrependInt64Slot(4, FreeStageId, 0)
def ConstMiniGameShootingExcelAddFreeSectionCount(builder, FreeSectionCount): builder.PrependInt32Slot(5, FreeSectionCount, 0)
def ConstMiniGameShootingExcelAddPlayerCharacterId(builder, PlayerCharacterId): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(PlayerCharacterId), 0)
def ConstMiniGameShootingExcelStartPlayerCharacterIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ConstMiniGameShootingExcelAddHiddenPlayerCharacterId(builder, HiddenPlayerCharacterId): builder.PrependInt64Slot(7, HiddenPlayerCharacterId, 0)
def ConstMiniGameShootingExcelAddCameraSmoothTime(builder, CameraSmoothTime): builder.PrependFloat32Slot(8, CameraSmoothTime, 0.0)
def ConstMiniGameShootingExcelAddSpawnEffectPath(builder, SpawnEffectPath): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(SpawnEffectPath), 0)
def ConstMiniGameShootingExcelAddWaitTimeAfterSpawn(builder, WaitTimeAfterSpawn): builder.PrependFloat32Slot(10, WaitTimeAfterSpawn, 0.0)
def ConstMiniGameShootingExcelAddFreeGearInterval(builder, FreeGearInterval): builder.PrependInt32Slot(11, FreeGearInterval, 0)
def ConstMiniGameShootingExcelEnd(builder): return builder.EndObject()
