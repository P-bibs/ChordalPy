import os, traceback
import Chord, Tables, StringChordParser, Transposers

# Input Directory
PATH = "/Users/paulbiberstein/Desktop/Datasets/jazz_xlab"

# Process files in a directory in Real Book format and return note arrays
if __name__ == "__main__":
    
    directory = os.listdir(PATH)

    totalLines = 0
    errorLines = 0
    totalFiles = 0
    errorFiles = 0

    # Loop through each file and process
    for file in directory:
        # Only process data files
        if ".xlab" not in file:
            continue

        totalFiles+=1

        # Start by transposing the file.
        # Returns a list of transposed chords
        try:
            transposedList = Transposers.transposeRealBookFile(path + "/" + file)
        except:
            errorFiles+=1
            print("trouble with file " + file)

        # Then read in each chord and convert to note Array
        for chord in transposedList:
            totalLines+=1
            try:
                StringChordParser.parseChord(chord).getNoteArray()
            except:
                errorLines+=1
        
        if totalFiles % 100 == 0:
            print(str(totalFiles) + " files processed")

    print("Errors: %s files out of %s total files" % (errorFiles, totalFiles))
    print("Errors: %s lines out of %s total lines" % (errorLines, totalLines))

        