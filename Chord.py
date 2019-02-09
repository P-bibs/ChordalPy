class Chord:
    def __init__(self, root, quality, size):
        self.root = root
        self.quality = quality
        self.size = size

    # returns each characteristic of chord concatenated (ie: root + quality + size)
    def toString(self):
        if(self.size == 3):
            return self.root + self.quality
        return self.root + self.quality + self.size

    # returns 12 item array of booleans representing notes in chord
    def getNotes(self):
        noteList = [False for c in range(12)]
        noteIndex = romToStep(self.root)
        noteList[noteIndex] = True
        for interval in intervals[self.size][self.quality]:
            noteIndex += interval
            noteList[noteIndex % 12] = True

        return noteList 

    # returns letter names of notes in chord starting from root
    def getSpelling(self):
        notesArry = self.getNotes()
        outArry = []
        rootIndex = romToStep(self.root)
        for i in range(12):
            index = (i + rootIndex) % 12
            if notesArry[index]:
                #Ensure that correct enharmonic equivalent is used
                if self.quality == "aug":
                    outArry.append(notes["sharp"][index])
                else:
                    outArry.append(notes["flat"][index])
        return outArry 
