import sounddevice as sd
import numpy as np


def callback(indata, frames, time, status):
    samples = np.abs(indata[:, 0])

    maximum = np.max(samples)

    bars = int(maximum * 50)

    print("█" * bars)


print("Silakan bicara atau ketuk laptop...")

with sd.InputStream(callback=callback):
    while True:
        pass
