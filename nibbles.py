#!/usr/bin/env python3

import math

volume = 0.5

base = 200.0

beat = 44100.0 / 10.0

tau = 2 * math.pi


def note(time):
    if time < beat:
        return base
    elif time < beat * 2.0:
        return base * 9.0 / 8.0
    elif time < beat * 3:
        return base * 5.0 / 4.0
    elif time < beat * 4:
        return base * 9.0 / 8.0
    elif time < beat * 5:
        return base
    elif time < beat * 6:
        return base * 9.0 / 8.0
    elif time < beat * 7.5:
        return base * 5.0 / 4.0
    elif time < beat * 8:
        return None
    elif time < beat * 9.5:
        return base
    elif time < beat * 10:
        return None
    elif time < beat * 11.5:
        return base
    else:
        return None


def wave(phase):
    if phase < tau / 2:
        return -1
    else:
        return 1


phase = 0

for time in range(0, int(beat * 16)):
    frequency = note(time)
    if frequency:
        phase += frequency * tau / 44100
        while phase >= tau:
            phase -= tau
        print(wave(phase) * volume)
    else:
        print(0)
