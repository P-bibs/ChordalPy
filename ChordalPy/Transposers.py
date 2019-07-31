scales = {
    "Cb": ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb'],
    "C": ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    "C#": ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#'],
    "Db": ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'],
    "D": ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
    "D#": ['D#', 'E#', 'F##', 'G#', 'A#', 'B#', 'C##'],
    "Eb": ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],
    "E": ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
    "E#": ['E#', 'F##', 'G##', 'A#', 'B#', 'C##', 'D##'],
    "F": ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
    "F#": ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#'],
    "Gb": ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F'],
    "G": ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
    "G#": ['G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F##'],
    "Ab": ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],
    "A": ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
    "A#": ['A#', 'B#', 'C##', 'D#', 'E#', 'F##', 'G##'],
    "Bb": ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
    "B": ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
    "B#": ['B#', 'C##', 'D##', 'E#', 'F##', 'G##', 'A##']
}

naturalToHalfStep = {
    "Cb": -1,
    "C": 0,
    "C#": 1,
    "C##": 2,
    "Dbb": 0,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "D##": 4,
    "Ebb": 2,
    "Eb": 3,
    "E": 4,
    "E#": 5,
    "Fb": 4,
    "F": 5,
    "F#": 6,
    "F##": 7,
    "Gbb": 5,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "G##": 9,
    "Abb": 7,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "A##": 11,
    "Bbb": 9,
    "Bb": 10,
    "B": 11,
    "B#": 0
}

# accepts a path to a file in digital real book format and returns an array of chords in that file transposed to 'C'
# 51:1 705.8823529411765 2 712.9411764705883 G:maj7 GMaj7 C
def transposeRealBookFile(pathToFile):
    f = open(pathToFile, "r")

    # Strip extra info to leave just a pair [chord, key] for each line
    pairs = []
    for line in f:
        if line == "\n":
            continue
        strippedLine = line.strip("\n").split(" ")[4:]
        strippedLine.pop(1)
        pairs.append(strippedLine)

    # Transpose each chord and return a single chord
    transposedChords = []
    for pair in pairs:
        transposedChords.append(transpose(pair[0], pair[1]))

    f.close()
    return transposedChords


def transpose(chord, key):
    # If key is minor, use a hacky solution to change it to relative major
    if key[-1] == "m":
        key = key [0:-1]
        key = scales[key][2]
        if "##" in key:
            key = key[0] + "#"
        elif "#" in key:
            key = key[0]
        elif "b" in key:
            key = key + "b"
        else:
            key = key + "b"

    #If chord is already in key of C
    if key == "C":
        return chord

    root, restOfTheChord = chord.split(":")

    # If chord is diatonic to its key
    if root in scales[key]:
        scaleDegree = scales[key].index(root)
        return scales["C"][scaleDegree] + ":" + restOfTheChord

    # If chord is not diatonic
    for note in scales[key]:
        if root[0] == note[0]:
            scaleDegree = scales[key].index(note)

    halfStepOffset = naturalToHalfStep[root] - naturalToHalfStep[scales[key][scaleDegree % 7]]

    if halfStepOffset == 0:
        accidental = ""
    elif halfStepOffset > 0:
        accidental = "#" * halfStepOffset
    elif halfStepOffset < 0:
        accidental = "b" * (-1*halfStepOffset)

    return scales["C"][scaleDegree % 7] + accidental + ":" + restOfTheChord

