"""Unit tests to be used with pytest"""

import pytest
import StringChordParser
import Chord

def test_ChordParsing():
    # ('C', [(1, 0), (3, 4), (5, 7)], '')

    assert StringChordParser.parse_chord("C:maj").get_spelling() == Chord.Chord('C', [(1, 0), (3, 4), (5, 7)], '').get_spelling()

    # ('Eb', [(1, 0), (3, 3), (5, 7), (9, 14)], '')
    assert StringChordParser.parse_chord("Eb:min7(*7,9)").get_spelling() == Chord.Chord('Eb', [(1, 0), (3, 3), (5, 7), (9, 14)], '').get_spelling()

    assert StringChordParser.parse_chord("C:sus2/G").get_spelling() == Chord.Chord('C', [(1, 0), (2, 2), (5, 7)], 'G').get_spelling()

    assert StringChordParser.parse_chord("E:7").get_spelling() == Chord.Chord('E', [(1, 0), (3, 4), (5, 7), (7, 10)], '').get_spelling()

    assert StringChordParser.parse_chord("A:maj").get_spelling() == Chord.Chord('A', [(1, 0), (3, 4), (5, 7)], '').get_spelling()

    assert StringChordParser.parse_chord("F#:min").get_spelling() == Chord.Chord('F#', [(1, 0), (3, 3), (5, 7)], '').get_spelling()

    assert StringChordParser.parse_chord("C:dim7").get_spelling() == Chord.Chord('C', [(1, 0), (3, 3), (5, 6), (7, 9)], '').get_spelling()

    assert StringChordParser.parse_chord("B:dim").get_spelling() == Chord.Chord('B', [(1, 0), (3, 3), (5, 6)], '').get_spelling()

    assert StringChordParser.parse_chord("Cb:maj").get_spelling() == Chord.Chord('Cb', [(1, 0), (3, 4), (5, 7)], '').get_spelling()

def test_ChordSpelling():
    assert Chord.Chord("C",[(1,0),(3,4),(5,7)], "").get_spelling() == ["C", "E", "G"]

    assert Chord.Chord("C",[(1,0),(3,3),(5,7)], "").get_spelling() == ["C", "Eb", "G"]

    assert Chord.Chord("C",[(1,0),(3,3),(5,6)], "").get_spelling() == ["C", "Eb", "Gb"]

    assert Chord.Chord("C",[(1,0),(2,3),(5,5)], "").get_spelling() == ["C", "D#", "Gbb"]

    assert Chord.Chord("C",[(1,0),(3,4),(5,7),(9,14)], "").get_spelling() == ["C", "E", "G", "D"]

    assert Chord.Chord("C#",[(1,0),(3,3),(5,6),(7,9)], "").get_spelling() == ["C#", "E", "G", "Bb"]

    assert Chord.Chord("C",[(1,0),(3,3),(7,9),(9,13)], "").get_spelling() == ["C", "Eb", "Bbb", "Db"]

    assert Chord.Chord("Cb",[(1,0),(3,4),(5,7)], "").get_spelling() == ["Cb", "Eb", "Gb"]

def test_ChordNoteArray():
    assert Chord.Chord("C",[(1,0),(3,4),(5,7)], "").get_note_array() == [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]

    assert Chord.Chord("C",[(1,0),(3,3),(7,9),(9,13)], "").get_note_array() == [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
