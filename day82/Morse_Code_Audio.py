import winsound
import time

UNIT = 0.1  # 1 unit = 100ms, adjust this for speed


def dot():
    winsound.Beep(700, int(UNIT * 1000))
    time.sleep(UNIT)  # gap after symbol


def dash():
    winsound.Beep(700, int(UNIT * 3 * 1000))
    time.sleep(UNIT)  # gap after symbol


def play_morse(morse_string):
    for symbol in morse_string:
        if symbol == ".":
            dot()
        elif symbol == "-":
            dash()
        elif symbol == " ":
            time.sleep(UNIT)  # gap between letters
        elif symbol == "/":
            time.sleep(UNIT * 2)
