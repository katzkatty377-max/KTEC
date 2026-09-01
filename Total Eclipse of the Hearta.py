import time
import sys

print("n\n")

lyrics = [
        ("Turn around", 0.80, 0.10),
        ("Every now and then I get a little bit Lonely", 0.00, 0.07),
        ("And you're never coming around", 0.00, 0.07),
        
        ("Turn around", 0.80, 0.10),
        ("Every now and then i get a little bit tired", 0.00, 0.07),
        ("Of listening to the sound of my tears", 0.00, 0.07),
    
        ("Turn around", 0.60, 0.10),
        ("Every now and then I get a little bit nervous", 0.00, 0.06),
        ("That the best of all the years have gone by", 0.00, 0.06),

        ("Turn around", 0.60, 0.10),
        ("Every now and then I get a little bit terrified", 0.00, 0.07),
        ("And then i see the look in your eyes", 0.00, 0.07),
        
        ("Turn around, bright eyes", 0.80, 0.09),
        ("Every now and then I fall apart", 0.00, 0.08),
        ("Turn around, bright eyes", 0.80, 0.09),
        ("Every now and then I fall apart", 0.80, 0.07),

        ("And I need you now tonight", 0.80, 0.10),
        ("And I need you more than ever", 0.80, 0.10),
        ("And if you only hold me tight", 0.90, 0.09),

        ("We'll be holding on forever", 0.00, 0.09),
        ("And we'll only be making it right", 1.00, 0.07),
        ("'Cause we'll never be wrong", 1.00, 0.07),

        ("Together we can take it to the end of the line", 1.00, 0.06),
        ("Your love is like a shadow on me all of the time", 2.00, 0.07),

        ("I don't know what to do", 0.10, 0.08),
        ("I'm always in the dark", 0.00, 0.07),

        ("Living in a powder keg", 0.00, 0.07),
        ("And giving off sparks", 0.90, 0.08),

        ("I really need you tonight", 0.80, 0.08),
        ("Forever's gonna start tonight", 0.0, 0.08),
        ("Forever's gonna start tonight", 5.00, 0.08)

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