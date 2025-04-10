# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ObstacleExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsObstacleExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ObstacleExcel()
        x.Init(buf, n + offset)
        return x

    # ObstacleExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ObstacleExcel
    def Index(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleExcel
    def PrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ObstacleExcel
    def JumpAble(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ObstacleExcel
    def SubOffset(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ObstacleExcel
    def SubOffsetAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # ObstacleExcel
    def SubOffsetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ObstacleExcel
    def SubOffsetIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # ObstacleExcel
    def X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ObstacleExcel
    def Z(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ObstacleExcel
    def Hp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleExcel
    def MaxHp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ObstacleExcel
    def BlockRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ObstacleExcel
    def EvasionRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ObstacleExcel
    def DestroyType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ObstacleExcel
    def Point1Offeset(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ObstacleExcel
    def Point1OffesetAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # ObstacleExcel
    def Point1OffesetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ObstacleExcel
    def Point1OffesetIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

    # ObstacleExcel
    def EnemyPoint1Osset(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ObstacleExcel
    def EnemyPoint1OssetAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # ObstacleExcel
    def EnemyPoint1OssetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ObstacleExcel
    def EnemyPoint1OssetIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

    # ObstacleExcel
    def Point2Offeset(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ObstacleExcel
    def Point2OffesetAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # ObstacleExcel
    def Point2OffesetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ObstacleExcel
    def Point2OffesetIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        return o == 0

    # ObstacleExcel
    def EnemyPoint2Osset(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ObstacleExcel
    def EnemyPoint2OssetAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # ObstacleExcel
    def EnemyPoint2OssetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ObstacleExcel
    def EnemyPoint2OssetIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0

    # ObstacleExcel
    def SubObstacleID(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ObstacleExcel
    def SubObstacleIDAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # ObstacleExcel
    def SubObstacleIDLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ObstacleExcel
    def SubObstacleIDIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0

def ObstacleExcelStart(builder): builder.StartObject(16)
def ObstacleExcelAddIndex(builder, Index): builder.PrependInt64Slot(0, Index, 0)
def ObstacleExcelAddPrefabName(builder, PrefabName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(PrefabName), 0)
def ObstacleExcelAddJumpAble(builder, JumpAble): builder.PrependBoolSlot(2, JumpAble, 0)
def ObstacleExcelAddSubOffset(builder, SubOffset): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(SubOffset), 0)
def ObstacleExcelStartSubOffsetVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ObstacleExcelAddX(builder, X): builder.PrependFloat32Slot(4, X, 0.0)
def ObstacleExcelAddZ(builder, Z): builder.PrependFloat32Slot(5, Z, 0.0)
def ObstacleExcelAddHp(builder, Hp): builder.PrependInt64Slot(6, Hp, 0)
def ObstacleExcelAddMaxHp(builder, MaxHp): builder.PrependInt64Slot(7, MaxHp, 0)
def ObstacleExcelAddBlockRate(builder, BlockRate): builder.PrependInt32Slot(8, BlockRate, 0)
def ObstacleExcelAddEvasionRate(builder, EvasionRate): builder.PrependInt32Slot(9, EvasionRate, 0)
def ObstacleExcelAddDestroyType(builder, DestroyType): builder.PrependInt32Slot(10, DestroyType, 0)
def ObstacleExcelAddPoint1Offeset(builder, Point1Offeset): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(Point1Offeset), 0)
def ObstacleExcelStartPoint1OffesetVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ObstacleExcelAddEnemyPoint1Osset(builder, EnemyPoint1Osset): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyPoint1Osset), 0)
def ObstacleExcelStartEnemyPoint1OssetVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ObstacleExcelAddPoint2Offeset(builder, Point2Offeset): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(Point2Offeset), 0)
def ObstacleExcelStartPoint2OffesetVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ObstacleExcelAddEnemyPoint2Osset(builder, EnemyPoint2Osset): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyPoint2Osset), 0)
def ObstacleExcelStartEnemyPoint2OssetVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ObstacleExcelAddSubObstacleID(builder, SubObstacleID): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(SubObstacleID), 0)
def ObstacleExcelStartSubObstacleIDVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ObstacleExcelEnd(builder): return builder.EndObject()
