# automatically generated by the FlatBuffers compiler, do not modify

# namespace: _Element

import flatbuffers

class Unit(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsUnit(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Unit()
        x.Init(buf, n + offset)
        return x

    # Unit
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Unit
    def Filename(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Unit
    def Revision(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Unit
    def Language(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Unit
    def Item(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UnitStart(builder): builder.StartObject(4)
def UnitAddFilename(builder, filename): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(filename), 0)
def UnitAddRevision(builder, revision): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(revision), 0)
def UnitAddLanguage(builder, language): builder.PrependInt32Slot(2, language, 0)
def UnitAddItem(builder, item): builder.PrependInt32Slot(3, item, 0)
def UnitEnd(builder): return builder.EndObject()
