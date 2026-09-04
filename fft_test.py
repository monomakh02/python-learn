import sounddevice as sd
import numpy as np

RATE = 44100
BLOCK = 2048


def callback(indata, frames, time, status):

    audio = indata[:, 0]

    fft = np.fft.rfft(audio)

    magnitude = np.abs(fft)

    freqs = np.fft.rfftfreq(len(audio), 1 / RATE)

    dominant = np.argmax(magnitude)
        

    print(
        f"\rDominan : {freqs[dominant]:7.1f} Hz | Energy : {magnitude[dominant]:.3f}",
        end="",
    )


print("Analisa frekuensi...")

with sd.InputStream(
    samplerate=RATE,
    blocksize=BLOCK,
    channels=1,
    callback=callback,
):
    while True:
        pass
