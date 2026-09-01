import time
import sys

print("\n\n")

lyrics = [
        ("eEe", 0.20, 0.08),
        ("eEe", 0.20, 0.08),
        ("sAkUdINg", 0.10, 0.06),
        ("kAding", 0.20, 0.05),
        ("PaK", 0.00, 0.05),
        ("dUnGdInG", 0.30, 0.05),
        ("duNG", 0.00, 0.05),
        ("pAnG", 0.00, 0.03),
        ("dUKinG", 0.50, 0.05),
        ("eEe", 0.00, 0.06),
        ("eEe", 0.20, 0.06),
        ("sAkADing", 0.00, 0.06),
        ("SaKAdInG", 0.30, 0.06),
        ("PaK", 0.00, 0.06),
        ("dUnGdInG", 0.00, 0.05),
        ("duNG", 0.20, 0.05),
        ("dANg", 0.10, 0.05),
        ("PaK", 0.10, 0.06,),
        ("kInG", 0.40, 0.08),
        ("EeEE", 0.20, 0.08),
        ("eEe", 0.40, 0.08),
        ("eEe", 2.00, 0.06),
    ]

def type_out(text, char_delay=0.1):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_delay)
        sys.stdout.write("\n")
        sys.stdout.flush()

def play_lyrics(lyrics):
        for line, line_delay, char_delay in lyrics:
            type_out(line, char_delay)
            time.sleep(line_delay)

if __name__ == "__main__":
        play_lyrics(lyrics)