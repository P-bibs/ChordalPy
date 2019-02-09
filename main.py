import re
import Chord, tables, StringChordParser


def romToStep(romNumeral):
    return romReference[romNumeral]


def main():
    myChords = ["I", "i7", "IVmaj7", "V7", "II7", "III7", "Iaug"]
    if False:
        parsedChords = []

        for chord in myChords:
            chordTuple = StringChordParser.parseChord(chord)
            parsedChords.append(Chord(*chordTuple))

        for chord in parsedChords:
            print(chord.toString())
            print("\t", end="")

            spelling = chord.getSpelling()
            for note in spelling:
                print(note, end=" ")

            print("")
    
    while(False):
        chord = input("Type a chord")
        chordTuple = StringChordParser.parseChord(chord)
        chord = Chord(*chordTuple)

        print(chord.toString())
        print("\t", end="")
        spelling = chord.getSpelling()
        for note in spelling:
            print(note, end=" ")
        print("")

    while(False):
        chord = input("Type a chord")
        if verifyChord(chord):
            print("Valid")
        else:
            print("Not Valid")

    for item in myChords:
        print(item + " is ", end="")
        if StringChordParser.verifyChord(item):
            print("Valid")
        else:
            print("Not Valid")
        

main()