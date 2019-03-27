import Chord, tables, StringChordParser

# various tester snippets
if __name__ == "__main__":
    while True:
        text = input("Type a chord")
        try:
            print(StringChordParser.parseChord(text).getSpelling())
        except:
            print("Sorry, chord couldn't be parsed")