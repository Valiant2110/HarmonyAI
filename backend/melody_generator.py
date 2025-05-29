# backend/melody_generator.py

import random
import os
from music21 import stream, note, tempo, midi
from midi2audio import FluidSynth

GENERATED_DIR = "generated"
os.makedirs(GENERATED_DIR, exist_ok=True)

MOOD_TEMPOS = {
    "happy": 140,
    "sad": 60,
    "angry": 120,
    "relaxed": 90
}

MOOD_SCALES = {
    "happy": ['C4', 'D4', 'E4', 'G4', 'A4'],
    "sad": ['A3', 'B3', 'C4', 'E4', 'F4'],
    "angry": ['C4', 'D#4', 'F4', 'G4', 'A#4'],
    "relaxed": ['C4', 'D4', 'F4', 'G4', 'A4']
}

def generate_melody(mood: str = "happy", duration=16) -> str:
    # Create a music21 stream
    s = stream.Stream()

    # Set tempo
    bpm = MOOD_TEMPOS.get(mood, 100)
    s.append(tempo.MetronomeMark(number=bpm))

    # Pick scale based on mood
    scale_notes = MOOD_SCALES.get(mood, ['C4', 'D4', 'E4', 'F4', 'G4'])

    # Generate notes
    for _ in range(duration):
        pitch = random.choice(scale_notes)
        n = note.Note(pitch)
        n.quarterLength = random.choice([0.5, 1.0])
        s.append(n)

    # Save to MIDI
    midi_filename = os.path.join(GENERATED_DIR, f"melody_{mood}.mid")
    s.write('midi', fp=midi_filename)

    # Convert to WAV using FluidSynth
    wav_filename = midi_filename.replace(".mid", ".wav")
    fs = FluidSynth()
    fs.midi_to_audio(midi_filename, wav_filename)

    return wav_filename
