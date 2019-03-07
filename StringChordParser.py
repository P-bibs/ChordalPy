import re, tables

# takes a chord represented as a string and separates it into 3 components (also expands shorthand)
def parseChord(stringChord):
    print("Parsing chord %s" % stringChord)
    # if chord isn't formatted correctly, warn and break
    #if not verifyChord(stringChord):
    #   print("WARNING: chord %s is not in a parsable format" % stringChord)
    #   return
    
    #try:
    root, temp = stringChord.split(":")
    if "/" in temp:
        middle, bass = temp.split("/")
    else:
        middle = temp
        bass = ""


    #intervals parsing
    if middle[0] != "(":
        #split into intervals and modifiers
        shorthand = re.search(r".+?(?=(\(|$))", middle).group()
        intervals = tables.intervals["shorthand"][shorthand]
        modifiers = re.search(r"(\(.+|$)", middle).group()

        # convert modifiers to same format as intervals    
        modifiers = modifierToTuple(modifiers)
    else: 
        #if no shorthand, set intervals equal to middle and modifiers to empty
        intervals = middle
        modifiers = ()

    #convert intervals to array so it is mutable 
    intervals = [c for c in intervals]
    modifiers = [c for c in modifiers]

    # loop through modifiers.
    # if modifier indicates sharping, flatting, or removing a chordal member
    # then deal with it here.
    # If it indicates adding a chordal member, deal with it in another loop
    # after.
    for i in range(len(modifiers)-1, -1, -1):

        # alias just the number of the chordal member of the modifier
        chordalMemberA = re.search(r"\d", modifiers[i]).group()

        for j in range(len(intervals)-1, -1, -1):
            # alias just the number of the chordal member of the current intervals
            chordalMemberB = re.search(r"\d", intervals[j]).group()

            # if our modifier contains a step that is also in our current inervals,
            # then update it (by reassigning or removing)
            if chordalMemberA==chordalMemberB:
                # if we want to remove a chordal member
                if modifiers[i][0]=="*":
                    intervals.pop(j)
                # if we want to sharp or flat a chordal member
                else:
                    intervals[j] = modifiers[i]
                # pop modifiers as we deal with them so we can deal with leftovers below
                modifiers.pop(i)

    # since we removed modifiers as we added them, the only ones
    # remaining will be additional chordal members that we didn't deal with.
    # Lets add them with the loop below
    for interval in modifiers:
        if "*" in interval:
            raise Exception("ERROR: Attempt to remove a chordal member that doesn't exist (Chordal Member: %s" % interval)
        intervals.append(interval)


    return (root, intervals, bass)
    #except:
    #    raise Exception("The chord " + stringChord + " could not be parsed correctly")

#helper function for main parser
def modifierToTuple(modifierString):
    if len(modifierString)==0:
        return ()

    # strip parentheses
    modifierString = modifierString[1:-1]

    # strip whitespace in case string is formatted wrong
    modifierString = modifierString.replace(" ", "")

    # split along commas to get individual elements
    out = modifierString.split(",")

    #convert to tuple
    out = tuple(out)
    
    return out
    
def verifyChord(stringChord):
    regex = r"[A-G][b#]?:.+?(\/\d)?"

    match = re.search(regex, stringChord)
    if match is not None and (match.span()[1]-match.span()[0]==len(stringChord)):
        return True
    else:
        return False