"""Constant values needed for string parsing"""

intervals = {
    "intervalToTuple": {
        "1": (1,0),
        "2": (2,2),
        "b3": (3,3),
        "3": (3,4),
        "4": (4,5),
        "b5": (5,6),
        "5": (5,7),
        "#5": (5,8),
        "6": (6,9),
        "bb7": (7,9),
        "b7": (7,10),
        "7": (7,11),
        "9": (9,14),
        "b9": (9,13),
        "#9": (9,15),
        "11": (11,17),
        "#11": (11,18),
        "b13": (13,20),
        "13": (13,21),

        "s5": (5,8),
        "s9": (9,15),
        "s11": (11,18)
    },
    "shorthandToIntervals": {
        "maj": ("1", "3", "5"),

        "min": ("1", "b3", "5"),

        "dim": ("1", "b3", "b5"),

        "aug": ("1", "3", "#5"),
        "maj7": ("1", "3", "5", "7"),
        "min7": ("1", "b3", "5", "b7"),
        "7": ("1", "3", "5", "b7"),
        "dim7": ("1", "b3", "b5", "bb7"),
        "hdim7": ("1", "b3", "b5", "b7"),
        "minmaj7": ("1", "b3", "5", "7"),

        "maj6": ("1", "3", "5", "6"),
        "min6": ("1", "b3", "5", "6"),

        "9": ("1", "3", "5", "b7", "9"),
        "maj9": ("1", "3", "5", "7", "9"),
        "min9": ("1", "b3", "5", "b7", "9"),
        "9sus": ("1", "4", "5", "b7", "9"),
        "sus9": ("1", "4", "5", "b7", "9"),

        "11": ("1", "3", "5", "b7", "11"),

        "13": ("1", "3", "5", "b7", "13"),

        "sus2": ("1", "2", "5"),
        "sus4": ("1", "4", "5"),

        # Unofficial aliases, comment out for stricter interpretation
        "6": ("1", "3", "5", "6"),
        "hdim": ("1", "b3", "b5", "b7")
    }
}

notes = {
    "naturalToStep": {
        "C": 0,
        "D": 1,
        "E": 2,
        "F": 3,
        "G": 4,
        "A": 5,
        "B": 6,
    },
    "naturalToHalfStep": {
        "Cbb": 10,
        "Cb": 11,
        "C": 0,
        "Dbb": 0,
        "Db": 1,
        "D": 2,
        "Ebb": 2,
        "Eb": 3,
        "E": 4,
        "Fb": 4,
        "F": 5,
        "Gb": 6,
        "G": 7,
        "Abb": 7,
        "Ab": 8,
        "A": 9,
        "Bbb": 9,
        "Bb": 10,
        "B": 11,
        "C#": 1,
        "C##": 2,
        "D#": 3,
        "E#": 5,
        "F#": 6,
        "G#": 8,
        "A#": 10,
        "B#": 12,
    },
    "stepToNatural": {
        "0": "C",
        "1": "D",
        "2": "E",
        "3": "F",
        "4": "G",
        "5": "A",
        "6": "B",
    },
    "natural": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
    ],
    "flat": [
        "C",
        "Db",
        "D",
        "Eb",
        "E",
        "F",
        "Gb",
        "G",
        "Ab",
        "A",
        "Bb",
        "B"
    ],
    "sharp": [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B"
    ]
}