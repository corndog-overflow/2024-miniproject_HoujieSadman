#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# Create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    """Play a tone with a specific frequency and duration."""
    speaker.duty_u16(1000)  # Set the PWM duty cycle (volume)
    speaker.freq(int(frequency))  # Set the frequency of the tone
    utime.sleep(duration)  # Play the tone for the given duration


def quiet() -> None:
    """Stop the tone."""
    speaker.duty_u16(0)  # Set the duty cycle to 0 to turn off the tone


# Define notes and their frequencies
notes = {
    "1":494,
    "2":440,
    "wait" : 0,
    "3": 783/2,
    "4": 739/2,
    "5": 659/2,
    "6": 311,
    "7": 311,
    "8": 246,
    "9": 220
}

song = [
    ("1", 0.185),
    ("2", 0.185),
    ("1", 1.5),
    ("wait", 0),
    ("2", 0.185),
    ("3", 0.185),
    ("4", 0.185),
    ("5", 0.185),
    ("6", 0.185*3),
    ("5", 0.185*3)
    
]

for note, duration in song:
    frequency = notes.get(note, 0)
    if frequency >= 0:
        if frequency == 0:
            quiet()
        else:
            playtone(int(frequency*1.1), duration)
    utime.sleep(0.05)  

quiet()
