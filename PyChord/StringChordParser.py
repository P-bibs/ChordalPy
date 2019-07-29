import functools
import re
from PyChord import Tables, Chord


def parse_chord(string_chord):
    """Takes a string representation of a chord and returns a chord object."""

    root, intervals, bass = "", "", ""

    # split into root, middle section, and bass
    if ":" in string_chord and "/" in string_chord:
        root, middle, bass = string_chord.replace(":", "_").replace("/", "_").split("_")
    elif ":" in string_chord:
        root, middle = string_chord.split(":")
    elif "/" in string_chord:
        root, bass = string_chord.split("/")
    else:
        root = string_chord

    intervals = _middle_to_intervals(middle)

    return Chord(root, intervals, bass)


def _middle_to_intervals(string_rep):
    """Converts the middle portion of a string chord (intervals) to a tuple."""

    # shorthand and then intervals (has a '(' but doesn't start with it)
    if string_rep[0] != "(" and "(" in string_rep:
        shorthand, modifiers = string_rep.split("(")
        modifiers = modifiers.replace(")","")
        modifiers = modifiers.split(",")

        intervals = Tables.intervals["shorthandToIntervals"][shorthand]

        intervals = list(map(_string_interval_to_tuple, intervals))
        modifiers = list(map(_string_interval_to_tuple, modifiers))

        intervals = _apply_modifiers(intervals, modifiers)

    # just intervals (so it starts with "(" )
    elif string_rep[0] == "(":
        intervals = string_rep[1:-1]
        intervals = intervals.split(",")
        intervals = list(map(_string_interval_to_tuple, intervals))

    # Just shorthand so it has no "("
    elif "(" not in string_rep:
        shorthand = string_rep
        intervals = Tables.intervals["shorthandToIntervals"][shorthand]
        intervals = list(map(_string_interval_to_tuple, intervals))

    return intervals


def _apply_modifiers(intervals, modifiers):
    """ Given a set of tuple intervals and a set of modifiers, adjusts the intervals accordingly"""
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


def _string_interval_to_tuple(string_interval):
    """Converts a string interval to a tuple interval"""
    if string_interval[0] == "*":
        interval = (int(string_interval[-1]), -1)
    else:
        interval = Tables.intervals["intervalToTuple"][string_interval]

    return interval
