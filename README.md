# PyChordParser

A simple python library to ingest and manipulate musical chords stored in plaintext format according to [Christopher Harte's 2010 thesis](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/534/HARTETowardsAutomatic2010.pdf?sequence=1).

## Installation

```bash
python -m pip install PyChordParser
```

## Usage

Parse a chord and print its members

```python
import PyChordParser

my_chord = PyChordParser.parse_chord(C:maj)
spelling = my_chord.get_spelling()
print("C:maj has notes %s" % spelling)
```