# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MemoryLobbyExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMemoryLobbyExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MemoryLobbyExcel()
        x.Init(buf, n + offset)
        return x

    # MemoryLobbyExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MemoryLobbyExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MemoryLobbyExcel
    def ProductionStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MemoryLobbyExcel
    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MemoryLobbyExcel
    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MemoryLobbyExcel
    def PrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MemoryLobbyExcel
    def MemoryLobbyCategory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MemoryLobbyExcel
    def SlotTextureName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MemoryLobbyExcel
    def RewardTextureName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MemoryLobbyExcel
    def BGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # MemoryLobbyExcel
    def AudioClipJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MemoryLobbyExcel
    def AudioClipKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MemoryLobbyExcel
    def AudioClipTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MemoryLobbyExcel
    def AudioClipTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MemoryLobbyExcel
    def AudioClipEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def MemoryLobbyExcelStart(builder): builder.StartObject(14)
def MemoryLobbyExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def MemoryLobbyExcelAddProductionStep(builder, ProductionStep): builder.PrependInt32Slot(1, ProductionStep, 0)
def MemoryLobbyExcelAddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(2, LocalizeEtcId, 0)
def MemoryLobbyExcelAddCharacterId(builder, CharacterId): builder.PrependInt64Slot(3, CharacterId, 0)
def MemoryLobbyExcelAddPrefabName(builder, PrefabName): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(PrefabName), 0)
def MemoryLobbyExcelAddMemoryLobbyCategory(builder, MemoryLobbyCategory): builder.PrependInt32Slot(5, MemoryLobbyCategory, 0)
def MemoryLobbyExcelAddSlotTextureName(builder, SlotTextureName): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(SlotTextureName), 0)
def MemoryLobbyExcelAddRewardTextureName(builder, RewardTextureName): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(RewardTextureName), 0)
def MemoryLobbyExcelAddBGMId(builder, BGMId): builder.PrependInt64Slot(8, BGMId, 0)
def MemoryLobbyExcelAddAudioClipJp(builder, AudioClipJp): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(AudioClipJp), 0)
def MemoryLobbyExcelAddAudioClipKr(builder, AudioClipKr): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(AudioClipKr), 0)
def MemoryLobbyExcelAddAudioClipTh(builder, AudioClipTh): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(AudioClipTh), 0)
def MemoryLobbyExcelAddAudioClipTw(builder, AudioClipTw): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(AudioClipTw), 0)
def MemoryLobbyExcelAddAudioClipEn(builder, AudioClipEn): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(AudioClipEn), 0)
def MemoryLobbyExcelEnd(builder): return builder.EndObject()
