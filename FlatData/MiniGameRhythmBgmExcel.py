# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameRhythmBgmExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMiniGameRhythmBgmExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameRhythmBgmExcel()
        x.Init(buf, n + offset)
        return x

    # MiniGameRhythmBgmExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MiniGameRhythmBgmExcel
    def RhythmBgmId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameRhythmBgmExcel
    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameRhythmBgmExcel
    def StageSelectImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameRhythmBgmExcel
    def Bpm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameRhythmBgmExcel
    def Bgm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MiniGameRhythmBgmExcel
    def BgmNameText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameRhythmBgmExcel
    def BgmArtistText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameRhythmBgmExcel
    def HasLyricist(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # MiniGameRhythmBgmExcel
    def BgmComposerText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MiniGameRhythmBgmExcel
    def BgmLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def MiniGameRhythmBgmExcelStart(builder): builder.StartObject(10)
def MiniGameRhythmBgmExcelAddRhythmBgmId(builder, RhythmBgmId): builder.PrependInt64Slot(0, RhythmBgmId, 0)
def MiniGameRhythmBgmExcelAddEventContentId(builder, EventContentId): builder.PrependInt64Slot(1, EventContentId, 0)
def MiniGameRhythmBgmExcelAddStageSelectImagePath(builder, StageSelectImagePath): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(StageSelectImagePath), 0)
def MiniGameRhythmBgmExcelAddBpm(builder, Bpm): builder.PrependInt64Slot(3, Bpm, 0)
def MiniGameRhythmBgmExcelAddBgm(builder, Bgm): builder.PrependInt64Slot(4, Bgm, 0)
def MiniGameRhythmBgmExcelAddBgmNameText(builder, BgmNameText): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(BgmNameText), 0)
def MiniGameRhythmBgmExcelAddBgmArtistText(builder, BgmArtistText): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(BgmArtistText), 0)
def MiniGameRhythmBgmExcelAddHasLyricist(builder, HasLyricist): builder.PrependBoolSlot(7, HasLyricist, 0)
def MiniGameRhythmBgmExcelAddBgmComposerText(builder, BgmComposerText): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(BgmComposerText), 0)
def MiniGameRhythmBgmExcelAddBgmLength(builder, BgmLength): builder.PrependInt32Slot(9, BgmLength, 0)
def MiniGameRhythmBgmExcelEnd(builder): return builder.EndObject()
