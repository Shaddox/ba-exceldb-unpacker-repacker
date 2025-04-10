# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestCameraSettingExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsConquestCameraSettingExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestCameraSettingExcel()
        x.Init(buf, n + offset)
        return x

    # ConquestCameraSettingExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConquestCameraSettingExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # ConquestCameraSettingExcel
    def ConquestMapBoundaryOffsetLeft(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConquestCameraSettingExcel
    def ConquestMapBoundaryOffsetRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConquestCameraSettingExcel
    def ConquestMapBoundaryOffsetTop(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConquestCameraSettingExcel
    def ConquestMapBoundaryOffsetBottom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConquestCameraSettingExcel
    def ConquestMapCenterOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConquestCameraSettingExcel
    def ConquestMapCenterOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConquestCameraSettingExcel
    def CameraAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConquestCameraSettingExcel
    def CameraZoomMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConquestCameraSettingExcel
    def CameraZoomMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ConquestCameraSettingExcel
    def CameraZoomDefault(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def ConquestCameraSettingExcelStart(builder): builder.StartObject(11)
def ConquestCameraSettingExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def ConquestCameraSettingExcelAddConquestMapBoundaryOffsetLeft(builder, ConquestMapBoundaryOffsetLeft): builder.PrependFloat32Slot(1, ConquestMapBoundaryOffsetLeft, 0.0)
def ConquestCameraSettingExcelAddConquestMapBoundaryOffsetRight(builder, ConquestMapBoundaryOffsetRight): builder.PrependFloat32Slot(2, ConquestMapBoundaryOffsetRight, 0.0)
def ConquestCameraSettingExcelAddConquestMapBoundaryOffsetTop(builder, ConquestMapBoundaryOffsetTop): builder.PrependFloat32Slot(3, ConquestMapBoundaryOffsetTop, 0.0)
def ConquestCameraSettingExcelAddConquestMapBoundaryOffsetBottom(builder, ConquestMapBoundaryOffsetBottom): builder.PrependFloat32Slot(4, ConquestMapBoundaryOffsetBottom, 0.0)
def ConquestCameraSettingExcelAddConquestMapCenterOffsetX(builder, ConquestMapCenterOffsetX): builder.PrependFloat32Slot(5, ConquestMapCenterOffsetX, 0.0)
def ConquestCameraSettingExcelAddConquestMapCenterOffsetY(builder, ConquestMapCenterOffsetY): builder.PrependFloat32Slot(6, ConquestMapCenterOffsetY, 0.0)
def ConquestCameraSettingExcelAddCameraAngle(builder, CameraAngle): builder.PrependFloat32Slot(7, CameraAngle, 0.0)
def ConquestCameraSettingExcelAddCameraZoomMax(builder, CameraZoomMax): builder.PrependFloat32Slot(8, CameraZoomMax, 0.0)
def ConquestCameraSettingExcelAddCameraZoomMin(builder, CameraZoomMin): builder.PrependFloat32Slot(9, CameraZoomMin, 0.0)
def ConquestCameraSettingExcelAddCameraZoomDefault(builder, CameraZoomDefault): builder.PrependFloat32Slot(10, CameraZoomDefault, 0.0)
def ConquestCameraSettingExcelEnd(builder): return builder.EndObject()
