import pytest
import StringChordParser
import Chord

def test_ChordParsing():
    # ('C', [(1, 0), (3, 4), (5, 7)], '')
    
    assert StringChordParser.parseChord("C:maj").getSpelling() == Chord.Chord('C', [(1, 0), (3, 4), (5, 7)], '').getSpelling()

    # ('Eb', [(1, 0), (3, 3), (5, 7), (9, 14)], '')
    assert StringChordParser.parseChord("Eb:min7(*7,9)").getSpelling() == Chord.Chord('Eb', [(1, 0), (3, 3), (5, 7), (9, 14)], '').getSpelling()

    assert StringChordParser.parseChord("C:sus2/G").getSpelling() == Chord.Chord('C', [(1, 0), (2, 2), (5, 7)], 'G').getSpelling()

    assert StringChordParser.parseChord("E:7").getSpelling() == Chord.Chord('E', [(1, 0), (3, 4), (5, 7), (7, 10)], '').getSpelling()

    assert StringChordParser.parseChord("A:maj").getSpelling() == Chord.Chord('A', [(1, 0), (3, 4), (5, 7)], '').getSpelling()

    assert StringChordParser.parseChord("F#:min").getSpelling() == Chord.Chord('F#', [(1, 0), (3, 3), (5, 7)], '').getSpelling()

    assert StringChordParser.parseChord("C:dim7").getSpelling() == Chord.Chord('C', [(1, 0), (3, 3), (5, 6), (7, 9)], '').getSpelling()

    assert StringChordParser.parseChord("B:dim").getSpelling() == Chord.Chord('B', [(1, 0), (3, 3), (5, 6)], '').getSpelling()

    assert StringChordParser.parseChord("Cb:maj").getSpelling() == Chord.Chord('Cb', [(1, 0), (3, 4), (5, 7)], '').getSpelling()

def test_ChordSpelling():
    assert Chord.Chord("C",[(1,0),(3,4),(5,7)], "").getSpelling() == ["C", "E", "G"]

    assert Chord.Chord("C",[(1,0),(3,3),(5,7)], "").getSpelling() == ["C", "Eb", "G"]

    assert Chord.Chord("C",[(1,0),(3,3),(5,6)], "").getSpelling() == ["C", "Eb", "Gb"]
    
    assert Chord.Chord("C",[(1,0),(2,3),(5,5)], "").getSpelling() == ["C", "D#", "Gbb"]

    assert Chord.Chord("C",[(1,0),(3,4),(5,7),(9,14)], "").getSpelling() == ["C", "E", "G", "D"]

    assert Chord.Chord("C#",[(1,0),(3,3),(5,6),(7,9)], "").getSpelling() == ["C#", "E", "G", "Bb"]

    assert Chord.Chord("C",[(1,0),(3,3),(7,9),(9,13)], "").getSpelling() == ["C", "Eb", "Bbb", "Db"]

    assert Chord.Chord("Cb",[(1,0),(3,4),(5,7)], "").getSpelling() == ["Cb", "Eb", "Gb"]

def test_ChordNoteArray():
    assert Chord.Chord("C",[(1,0),(3,4),(5,7)], "").getNoteArray() == [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]

    assert Chord.Chord("C",[(1,0),(3,3),(7,9),(9,13)], "").getNoteArray() == [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

    