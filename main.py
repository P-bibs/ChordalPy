import re
import Chord, tables, StringChordParser

# various tester snippets
def main():
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

    print(StringChordParser.parseChord("Ab:sus4(b5, #9)/5"))
        

main()
