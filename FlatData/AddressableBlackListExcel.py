# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AddressableBlackListExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAddressableBlackListExcel(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AddressableBlackListExcel()
        x.Init(buf, n + offset)
        return x

    # AddressableBlackListExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AddressableBlackListExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AddressableBlackListExcel
    def FolderPath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # AddressableBlackListExcel
    def FolderPathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # AddressableBlackListExcel
    def FolderPathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # AddressableBlackListExcel
    def ResourcePath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # AddressableBlackListExcel
    def ResourcePathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # AddressableBlackListExcel
    def ResourcePathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def AddressableBlackListExcelStart(builder): builder.StartObject(3)
def AddressableBlackListExcelAddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def AddressableBlackListExcelAddFolderPath(builder, FolderPath): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(FolderPath), 0)
def AddressableBlackListExcelStartFolderPathVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def AddressableBlackListExcelAddResourcePath(builder, ResourcePath): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(ResourcePath), 0)
def AddressableBlackListExcelStartResourcePathVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def AddressableBlackListExcelEnd(builder): return builder.EndObject()
