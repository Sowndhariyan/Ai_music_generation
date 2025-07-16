# AI Music Generation 🎶

This project generates music using AI, specifically using deep learning models like LSTM.

## Steps

1. **Collect MIDI data**: Place MIDI files in the `data/` folder.
2. **Preprocess the data**: We use `music21` to parse MIDI into note sequences.
3. **Train a deep learning model**: An LSTM-based model is trained on the note sequences.
4. **Generate music**: Generate new sequences and convert them back to MIDI.
5. **Save output**: Save the generated sequences to the `output/` folder.

## Requirements

- Python
- music21
- TensorFlow or PyTorch
