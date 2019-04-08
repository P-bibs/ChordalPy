import functools
import re, tables, Chord

# takes a chord represented as a string and separates it into 3 components (also expands shorthand)
def parseChord(stringChord):

    root, intervals, bass = "", "", ""

    # split into root, middle section, and bass
    if ":" in stringChord and "/" in stringChord:
        root, middle, bass = stringChord.replace(":", "_").replace("/", "_").split("_")
    elif ":" in stringChord:
        root, middle = stringChord.split(":")
    elif "/" in stringChord:
        root, bass = stringChord.split("/")
    else:
        root = stringChord

    intervals = middleToIntervals(middle)

    return Chord.Chord(root, intervals, bass)

# Convert String Intervals to tuple intervals
def middleToIntervals(stringRep):
    # shorthand and then intervals (has a '(' but doesn't start with it)
    if stringRep[0] != "(" and "(" in stringRep:
        shorthand, modifiers = stringRep.split("(")
        modifiers = modifiers.replace(")","")
        modifiers = modifiers.split(",")

        intervals = tables.intervals["shorthandToIntervals"][shorthand]

        intervals = list(map(stringIntervalToTuple, intervals))
        modifiers = list(map(stringIntervalToTuple, modifiers))
        
        intervals = applyModifiers(intervals, modifiers)

    # just intervals (so it starts with "(" )
    elif stringRep[0] == "(":
        intervals = stringRep[1:-2]
        intervals = intervals.split(",")
        intervals = list(map(stringIntervalToTuple, intervals))

    # Just shorthand so it has no "("
    elif "(" not in stringRep:
        shorthand = stringRep
        intervals = tables.intervals["shorthandToIntervals"][shorthand]
        intervals = list(map(stringIntervalToTuple, intervals))

    return intervals

def applyModifiers(intervals, modifiers):
    # Replace intervals that are flatted or sharped
    for i in range(len(intervals)-1, -1, -1):
        for j in range(len(modifiers)-1, -1, -1):
            if intervals[i][0] == modifiers[j][0]:
                if modifiers[j][1] == -1:
                    intervals.pop(i)
                    modifiers.pop(j)
                    break
                else:
                    intervals[i] = modifiers[j]
                    modifiers.pop(i)
                    break
    
    for modifier in modifiers:
        intervals.append(modifier)

    return intervals

def stringIntervalToTuple(stringInterval):
    if stringInterval[0] == "*":
        interval = (int(stringInterval[-1]), -1)
    else:
        interval = tables.intervals["intervalToTuple"][stringInterval]
    
    return interval