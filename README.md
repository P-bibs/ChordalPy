# PyChord

A simple python library to ingest and manipulate musical chords stored in plaintext format according to [Christopher Harte's 2010 thesis](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/534/HARTETowardsAutomatic2010.pdf?sequence=1).

## Installation

```bash
python -m pip install PyChord
```

## The format

The chords that this library can parse are in a specific plaintext format detailed [here](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/534/HARTETowardsAutomatic2010.pdf?sequence=1); however, here's a quick and dirty run down.

Each chord has three parts: the root, the intervals, and the bass. They are seperated with a colon and a slash like so

```
root:intervals/bass
```

### Root

The root is simply any letter name. It could be `'C'` or `'G#'` or `'Fbbbbb'`.

### Intervals

The intervals section consists of a shorthand abbreviation for a common set of intervals followed by any changes to those intervals in parantheses. For example, a major triad with an added sharp sixth would be `maj(#6)`. The added intervals can do one of:
1. Add an interval to the existing shorthand.
2. Modify (sharp or flat) an interval in the existing shorthand.
3. Remove an interval in the existing shorthand (notated with a `*` before the interval to be removed).

The list of shorthands can be found on page 105 of the earlier referenced PDF.

### Bass

The bass is an interval degree (any digit 1-9) along with 0 or more modifiers (`#` or `b`)

## A note on intervals

There is an interesting quick to musical intervals that means they cannot be entirely expressed with only one digit. Rather, they requrie a tuple of two integers.

When looking through the source of this library, you will often find intervals notated as such. The first integer represents the number of letter names between the notes (for instance, in the interval from `C` to `G` the first integer would be `5`) and the second integer is the number of half steps (so in the interval from `C` to `G` the second integer would be `7`).

Using this method you can see how you would distiniguish between two enharmonic pitches. For example, `C` to `E` and `C` to `Fb`. The interval from `C` to `E` would be `(3, 4)` while the interval from `C` to `Fb` would be `(4, 4)`.

## Library Usage

Parse a chord and print its members

```python
import PyChord

my_chord = PyChord.parse_chord("C:maj")
spelling = my_chord.get_spelling()
print("C:maj has notes %s" % spelling)
```

Instantiate a chord directly

```python
import PyChord

# C major in first inversion (C:maj/3)
root = "C"
intervals = [(1, 0), (3, 4), (5, 7)]
bass = "E"

my_chord = PyChord.Chord(root, intervals, bass)
```

### `Chord` Class

Print a string representation of a chord
```python
print(str(my_chord))
# C:[(1, 0), (3, 4), (5, 7)]/E
```

Print the spelling of a chord
```python
print(my_chord.get_spelling())
# ['C', 'E', 'G']
```

Print a binary note array of a chord
```python
print(my_chord.get_note_array())
# [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
```

Print a pseudohash of a chord's intervals
```python
print(my_chord.get_pseudo_hash())
# ecca
```

Find the note a given interval above a chord's root
```python
print(my_chord.note_from_interval([5, 8]))
# ecca
```

## See Also
### Projects
[Chordgen.com](paulbiberstein.me/chordgen) - A web tool that uses machine learning to generate chord progressions. [The machine learning model](https://github.com/P-bibs/PyChordGen) was trained on data created with this library.
### Datasets
A non-exhaustive list of datasets that use a format parsable by this library:
* [Isophonics](http://isophonics.net/datasets)
* [Real Book](https://github.com/keunwoochoi/lstm_real_book/blob/master/more_data_to_play_with/jazz_xlab.zip)