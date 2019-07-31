import functools
from ChordalPy import Tables


class Chord:
    """A class representing a chord.

    Attributes:
        root (string): The root note of the chord.
        intervals (list[(int, int), ...]): The imaginary part of complex number.
        bass (string): The bass note of the chord.
    """

    def __init__(self, root, intervals, bass):
        """Construct a chord given a root, intervals, and a bass."""
        # PitchName object
        self.root = root
        # tuple of Interval object
        self.intervals = intervals
        # PitchName object
        self.bass = bass

        self.spelling = []

    def __repr__(self):
        """returns each characteristic of chord concatenated (ie: root + quality + size)."""
        return self.root + ":" + str(self.intervals) + "/" + self.bass

    def get_spelling(self):
        """Computes chord spelling, or returns cached version if already computed."""
        if self.spelling == []:
            notes = [self.root]

            for i in range(1, len(self.intervals)):
                notes.append(self.note_from_interval(self.intervals[i]))

            self.spelling = notes

        return self.spelling

    def get_note_array(self):
        """Returns a 12 item, binary list that represents the chord.

        For example: C:maj is [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0].
        """

        noteArray = [0 for c in range(12)]
        rootNumeral = Tables.notes["naturalToHalfStep"][self.root]
        noteArray[rootNumeral % 12] = 1

        for i in range(len(self.intervals)):
            halfStep = self.intervals[i][1]
            noteArray[(rootNumeral+halfStep) % 12] = 1

        return noteArray

    def get_pseudo_hash(self):
        """Returns a four character string that encodes all interval information

        Hash contains only letters a-h.
        """
        noteArray = self.get_note_array()
        pseudoHash = ''
        for i in range(0, 12, 3):
            seg = functools.reduce((lambda a,b : str(a)+str(b)), noteArray[i:i+3])
            pseudoHash += str(chr(int(seg, 2) + 97))

        return pseudoHash

    def note_from_interval(self, interval):
        """Given an interval above the root,
        returns the letter name of the corresponding note."""
        # -1 is added because an interval of a first corresponds to the root pitch
        rootNumeral = Tables.notes["naturalToStep"][self.root[0]]-1
        natural = Tables.notes["stepToNatural"][str(((rootNumeral + interval[0]) % 7))]

        naturalHalfSteps = Tables.notes["naturalToHalfStep"][natural]
        rootHalfSteps = Tables.notes["naturalToHalfStep"][self.root]

        # This is necessary for it all to work. Don't ask why
        if self.root=="Cb":
            naturalHalfSteps+=12

        if (naturalHalfSteps - rootHalfSteps)<0:
            halfStepOffset = interval[1]%12 - (naturalHalfSteps+12 - rootHalfSteps)
        else:
            halfStepOffset = interval[1]%12 - (naturalHalfSteps - rootHalfSteps)

        if halfStepOffset == 0:
            accidental = ""
        elif halfStepOffset > 0:
            accidental = "#" * halfStepOffset
        elif halfStepOffset < 0:
            accidental = "b" * (-1*halfStepOffset)

        return natural + accidental
