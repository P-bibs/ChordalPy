#!/usr/bin/env python3

import sys
import ChordalPy


def NoteFrequency(input_file):

    # Read each chord into a list and strip whitespace
    input_chords = []
    with open(input_file) as f:
        input_chords = f.readlines()
    input_chords = [line.strip('\n') for line in input_chords]

    # Parse each chord
    chords = []
    for chord in input_chords:
        chords.append(ChordalPy.parse_chord(chord))

    note_frequencies = {
        "Cb": 0, "C": 0, "C#": 0,
        "Db": 0, "D": 0, "D#": 0,
        "Eb": 0, "E": 0, "E#": 0,
        "Fb": 0, "F": 0, "F#": 0,
        "Gb": 0, "G": 0, "G#": 0,
        "Ab": 0, "A": 0, "A#": 0,
        "Bb": 0, "B": 0, "B#": 0,
        "other": 0
    }

    for chord in chords:
        spelling = chord.get_spelling()
        for note in spelling:
            if note in note_frequencies.keys():
                note_frequencies[note] += 1
            else:
                note_frequencies["other"] += 1

    keys = note_frequencies.keys()
    for key in keys:
        print("%s occured %i times" % (key, note_frequencies[key]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("""
        Print the frequency of occurences of each note in a given file of chords

        Usage - ./NoteFrequency source-file
        """)
        sys.exit(1)

    INPUT_PATH  = sys.argv[1]
    NoteFrequency(INPUT_PATH)
