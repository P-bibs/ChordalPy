import tables

class Chord:
    def __init__(self, root, intervals, bass):
        # PitchName object
        self.root = root
        # tuple of Interval object
        self.intervals = intervals
        # PitchName object
        self.bass = bass

    # returns each characteristic of chord concatenated (ie: root + quality + size)
    def toString(self):
        return self.root + ":" + str(self.intervals) + "/" + self.bass
    
    def getSpelling(self):
        notes = [self.root]
        rootNumeral = tables.notes["naturalToStep"][self.root[0]]-1

        for i in range(1, len(self.intervals)):
            notes.append(noteFromInterval(self.root, self.intervals[i]))
    
        return notes


def noteFromInterval(root, interval):
        rootNumeral = tables.notes["naturalToStep"][root[0]]-1
        natural = tables.notes["stepToNatural"][str(((rootNumeral + interval[0]) % 7))]

        naturalHalfSteps = tables.notes["naturalToHalfStep"][natural]
        rootHalfSteps = tables.notes["naturalToHalfStep"][root]

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
