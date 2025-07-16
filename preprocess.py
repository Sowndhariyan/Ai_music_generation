# preprocess.py

from music21 import converter, note, chord
import os
import pickle

def get_notes(midi_dir):
    notes = []
    for file in os.listdir(midi_dir):
        if file.endswith(".mid"):
            midi = converter.parse(os.path.join(midi_dir, file))
            notes_to_parse = midi.flat.notes
            for element in notes_to_parse:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))
    with open("data/notes.pkl", "wb") as f:
        pickle.dump(notes, f)
    return notes

if __name__ == "__main__":
    get_notes("data")
