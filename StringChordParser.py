import re

# takes a chord represented as a string and separates it into 3 components
# also explicitly states any qualities implied in chord naming (such as major or minor based on case)
def parseChord(input):
    try:
        stringChord = input

        # if the chord isn't a triad get the size and then chop it off
        if stringChord[-1:].isdigit():
            size = stringChord[-1:]
            stringChord = stringChord[:-1]
        else:
            size = "3"

        # if root is a two digit roman numeral then use the first two chars of the string, otherwise only use 1
        # chop off root from string once done
        if len(stringChord) > 1 and (stringChord[1] == "v" or stringChord[1] == "i" or stringChord[1] == "V" or stringChord[1] == "I"):
            # check for 'iii'
            if len(stringChord) > 2 and (stringChord[2] == "i" or stringChord[2] == "I"):
                root = stringChord[0:3]
                stringChord = stringChord[3:]
            else:
                root = stringChord[0:2]
                stringChord = stringChord[2:]
        else:
            root = stringChord[0]
            stringChord = stringChord[1:]

        if size == "3":
            # if triad has an implicit quality (maj or min)
            if len(stringChord) == 0:
                if root.isupper():
                    quality = "maj"
                elif root.islower():
                    quality = "min"
                else:
                    print("Error: chord is both upper and lower case")
            # if triad has explicit quality (dim or aug)
            else:
                quality = stringChord

        # if chord is not a triad (seventh or greater)
        else: 
            # if chord has an implicit quality (dom or min)
            if len(stringChord) == 0:
                if root.isupper():
                    quality = "dom"
                elif root.islower():
                    quality = "min"
                else:
                    print("Error: chord is both upper and lower case")
            # if triad has explicit quality
            else:
                quality = stringChord
    
        return (root, quality, size)
    except:
        print("The chord " + input + " could not be parsed correctly")



    
def verifyChord(stringChord):
    regex = "[VvIi]{1,3}([a-z]{3}|.{0})\d{0,2}"

    match = re.search(regex, stringChord)
    if match is not None and (match.span()[1]-match.span()[0]==len(stringChord)):
        return True
    else:
        return False