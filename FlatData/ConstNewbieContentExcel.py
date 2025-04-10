# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstNewbieContentExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsConstNewbieContentExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstNewbieContentExcel()
        x.Init(buf, n + offset)
        return x

    # ConstNewbieContentExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConstNewbieContentExcel
    def NewbieGachaReleaseDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstNewbieContentExcel
    def NewbieGachaCheckDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstNewbieContentExcel
    def NewbieGachaTokenGraceTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstNewbieContentExcel
    def NewbieAttendanceReleaseDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstNewbieContentExcel
    def NewbieAttendanceStartableEndDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ConstNewbieContentExcel
    def NewbieAttendanceEndDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def ConstNewbieContentExcelStart(builder): builder.StartObject(6)
def ConstNewbieContentExcelAddNewbieGachaReleaseDate(builder, NewbieGachaReleaseDate): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(NewbieGachaReleaseDate), 0)
def ConstNewbieContentExcelAddNewbieGachaCheckDays(builder, NewbieGachaCheckDays): builder.PrependInt32Slot(1, NewbieGachaCheckDays, 0)
def ConstNewbieContentExcelAddNewbieGachaTokenGraceTime(builder, NewbieGachaTokenGraceTime): builder.PrependInt32Slot(2, NewbieGachaTokenGraceTime, 0)
def ConstNewbieContentExcelAddNewbieAttendanceReleaseDate(builder, NewbieAttendanceReleaseDate): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(NewbieAttendanceReleaseDate), 0)
def ConstNewbieContentExcelAddNewbieAttendanceStartableEndDay(builder, NewbieAttendanceStartableEndDay): builder.PrependInt32Slot(4, NewbieAttendanceStartableEndDay, 0)
def ConstNewbieContentExcelAddNewbieAttendanceEndDay(builder, NewbieAttendanceEndDay): builder.PrependInt32Slot(5, NewbieAttendanceEndDay, 0)
def ConstNewbieContentExcelEnd(builder): return builder.EndObject()
