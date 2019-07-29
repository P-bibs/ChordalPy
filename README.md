# PyChord

A simple python library to ingest and manipulate musical chords stored in plaintext format according to [Christopher Harte's 2010 thesis](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/534/HARTETowardsAutomatic2010.pdf?sequence=1).

## Installation

```bash
python -m pip install PyChord
```

## Usage

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

Print a string representation of a chord
```python
print(str(my_chord))
```

## See Also

[Chordgen.com](paulbiberstein.me/chordgen) - A web tool that uses machine learning to generate chord progressions. The machine learning model ([found here](https://github.com/P-bibs/PyChordGen)) was trained on data created with this library.