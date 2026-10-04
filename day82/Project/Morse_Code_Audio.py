
import math
import os
import struct
import subprocess
import sys
import tempfile
import wave

UNIT = 0.1          # 1 unit = 100 ms; lower = faster
FREQUENCY = 700     # tone pitch in Hz
SAMPLE_RATE = 44100
VOLUME = 0.5        # 0.0 to 1.0
FADE = 0.005        # 5 ms fade in/out to avoid clicks


def _tone(duration):
    """Return a sine-wave tone as a list of 16-bit samples."""
    n = int(SAMPLE_RATE * duration)
    fade_n = int(SAMPLE_RATE * FADE)
    samples = []
    for i in range(n):
        value = math.sin(2 * math.pi * FREQUENCY * i / SAMPLE_RATE)
        # Fade in/out
        if i < fade_n:
            value *= i / fade_n
        elif i > n - fade_n:
            value *= (n - i) / fade_n
        samples.append(int(value * VOLUME * 32767))
    return samples


def _silence(duration):
    return [0] * int(SAMPLE_RATE * duration)


def generate_morse_samples(morse_string):
    """
    Standard Morse timing:
      dot = 1 unit, dash = 3 units
      gap between symbols  = 1 unit
      gap between letters  = 3 units  (' ')
      gap between words    = 7 units  ('/')
    """
    samples = []
    for symbol in morse_string:
        if symbol == ".":
            samples += _tone(UNIT) + _silence(UNIT)
        elif symbol == "-":
            samples += _tone(UNIT * 3) + _silence(UNIT)
        elif symbol == " ":
            samples += _silence(UNIT * 2)   # 1 (after symbol) + 2 = 3 units
        elif symbol == "/":
            samples += _silence(UNIT * 2)   # " / " gives 1 + 2 + 2 + 2 = 7 units
        # any other character is ignored
    return samples


def save_morse_wav(morse_string, filename="morse.wav"):
    """Save the Morse code audio to a WAV file."""
    samples = generate_morse_samples(morse_string)
    with wave.open(filename, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)  # 16-bit
        wav.setframerate(SAMPLE_RATE)
        wav.writeframes(struct.pack(f"<{len(samples)}h", *samples))
    return filename


def _play_file(path):
    if sys.platform.startswith("win"):
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME)
    elif sys.platform == "darwin":
        subprocess.run(["afplay", path], check=False)
    else:
        for player in (["aplay", "-q"], ["paplay"], ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet"]):
            try:
                subprocess.run(player + [path], check=True)
                return
            except (FileNotFoundError, subprocess.CalledProcessError):
                continue
        print("No audio player found. Install 'alsa-utils' (aplay) or similar.")


def play_morse(morse_string):
    """Generate Morse audio and play it (called from main.py)."""
    if not any(c in ".-" for c in morse_string):
        print("No Morse code to play.")
        return

    fd, path = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    try:
        save_morse_wav(morse_string, path)
        _play_file(path)
    finally:
        os.remove(path)


if __name__ == "__main__":
    play_morse("... --- ...")