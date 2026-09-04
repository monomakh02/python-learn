import sounddevice as sd
import numpy as np

THRESHOLD = 0.05

def audio_callback(indata, frames, time, status):
    volume = np.linalg.norm(indata)

    print(f"\rVolume : {volume:.5f}", end="")

with sd.InputStream(callback=audio_callback):
    print("Mendengarkan mikrofon... (CTRL+C untuk keluar)")
    while True:
        pass