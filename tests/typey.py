# This is a typing effect
import time
import sys


def typingprint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
