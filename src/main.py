import os, traceback, json
import Chord, Tables, StringChordParser, Transposers


INPUT_PATH = "/Users/paulbiberstein/Desktop/Datasets/jazz_xlab"
OUTPUT_PATH = "/Users/paulbiberstein/Desktop/hashedReverseDict.json"

def makeReverseDictionary(inputPath, outputPath):
    directory = os.listdir(inputPath)

    outDict = {}
    totalFiles = 0
    totalLines = 0
    errorFiles = 0
    errorLines = 0

    # Loop through each file and process
    for index, file in enumerate(directory):
        # Only process data files
        if ".xlab" not in file:
            continue

        totalFiles+=1

        # Start by transposing the file.
        # Returns a list of transposed chords
        try:
            transposedList = Transposers.transposeRealBookFile(inputPath + "/" + file)
        except:
            errorFiles+=1
            print("trouble with file " + file)
            continue

        # Then read in each chord and convert to note Array
        for chord in transposedList:
            totalLines+=1
            try:
                key = str(StringChordParser.parseChord(chord).getPseudoHash())
                value = chord
                if key in outDict and value not in outDict[key]:
                    outDict[key] = outDict[key] + [value]
                else:
                    outDict[key] = [value]
            except:
                errorLines+=1

        if totalFiles % 100 == 0:
            print(str(totalFiles) + " files processed")

    print("Errors: %s files out of %s total files" % (errorFiles, totalFiles))
    print("Errors: %s lines out of %s total lines" % (errorLines, totalLines))


    with open(outputPath, mode='w') as f:
        f.write(json.dumps(outDict))


# Process files in a directory in Real Book format and return note arrays
if __name__ == "__main__":
    makeReverseDictionary(INPUT_PATH, OUTPUT_PATH)