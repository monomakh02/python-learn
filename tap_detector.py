import sounddevice as sd
import numpy as np
import time

THRESHOLD = 0.025
DELTA = 0.020
COOLDOWN = 0.4

last_peak = 0
last_tap = 0


def callback(indata, frames, time_info, status):
    global last_peak
    global last_tap

    peak = np.max(np.abs(indata))

    change = peak - last_peak

    now = time.time()

    if peak > THRESHOLD and change > DELTA and now - last_tap > COOLDOWN:
        print(f">>> KETUKAN ({peak:.3f}) <<<")
        last_tap = now

    last_peak = peak


print("Menunggu ketukan...")

with sd.InputStream(callback=callback):
    while True:
        pass
