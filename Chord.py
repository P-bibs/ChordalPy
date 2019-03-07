import tables

class Chord:
    def __init__(self, root, intervals, bass):
        self.root = root
        self.intervals = intervals
        self.bass = bass

    # returns each characteristic of chord concatenated (ie: root + quality + size)
    def toString(self):
        return self.root + ":" + self.intervals + "/" + self.bass

    # returns 12 item array of booleans representing notes in chord
    def getNotes(self):
        noteList = [False for c in range(12)]

        for interval in self.intervals:
            noteList.append(tables.intervals["intervalToStep"][interval[-1]])

        out = [False for c in range(12)]
        rootIndex = tables.notes["noteToStep"][self.root]
        for i in range(rootIndex, rootIndex + len(noteList)):
            out[i % 12] = noteList[i - rootIndex]

        return out

    # returns letter names of notes in chord starting from root
    def getSpelling(self):
        splitIntervals = []
        spelling = []

        rootIndex = tables.notes["natural"].index(self.root[0])

        splitIntervals = [("", self.intervals[c][0]) if len(self.intervals)==1 else (self.intervals[c][0:-1], self.intervals[c][-1]) for c in range(len(self.intervals))]
        

        for interval in splitIntervals:
            spelling.append(interval[0] + tables.notes["natural"][(rootIndex + int(interval[1]) - 1) % 7])


        return spelling

    def getSpelling2(self):
        actualStep = []
        for interval in self.intervals:
            intervalInt = interval[-1]-1
            intervalInt -= intervalInt.count("b")
            intervalInt += intervalInt.count("#")
            actualStep.append(intervalInt)

        naturalStep = []
        for interval in self.intervals:
            ()
