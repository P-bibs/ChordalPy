import re
import Chord, tables, StringChordParser

# various tester snippets
def main():
    while(False):
        chord = input("Type a chord")
        chordTuple = StringChordParser.parseChord(chord)
        chord = Chord.Chord(*chordTuple)

        print(chord.toString())
        print("\t", end="")
        spelling = chord.getSpelling()
        for note in spelling:
            print(note, end=" ")
        print("")

    while(False):
        chord = input("Type a chord")
        if StringChordParser.verifyChord(chord):
            print("Valid")
        else:
            print("Not Valid")

    if False:
        myChords = ["C:sus2/5", "E:7", "A:maj", "D:maj", "E:maj", "F#:min"]
        for chord in myChords:
            myString = StringChordParser.parseChord(chord)
            myChord = Chord.Chord(*myString)
            print("%s is spelled %s" % (chord, myChord.getSpelling()))

    chord = "C:min(7)"
    myString = StringChordParser.parseChord(chord)
    myChord = Chord.Chord(*myString)
    print("%s is spelled %s" % (chord, myChord.getSpelling()))
    print("With notes %s" % myChord.getNotes())
        

main()
