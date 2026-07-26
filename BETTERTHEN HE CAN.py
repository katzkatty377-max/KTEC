import tkinter as tk
import time
import random

try:
    import pygame # type: ignore
    HAS_AUDIO = True
except ImportError:
    HAS_AUDIO = False


# ====================== EDIT THIS SECTION ======================

AUDIO_FILE = ""  # set to "" to disable audio

# (start_time_in_seconds, "lyric text")
LYRICS = [
        (1.0, "GIVE ME A SIGN"),
        (2.0, "TAKE MY HAND, WE'LL BE FINE"),
        (5.9, "PROMISE I WON'T LET YOU DOWN"),
        (10.9, "JUST KNOW THA'T YOU DON'T"),
        (13.9, "HAVE TO DO THIS ALONE"),
        (16.9, "PROMISE I'II NEVER LET YOU DOWN"),
        (21.9, "'CAUSE I KNOW I CAN TREAT YOU BETTER"),
        (25.9, "THAN HE CAN"),
        (28.0, "AND ANY GIRL LIKE YOU DESERVES A"),
        (31.9, "GENTLEMAN"),
        (33.6, "TELL ME, WHY ARE WE WASTING TIME"),
        (34.9, "ON ALL YOUR WASTED CRYIN'"),
        (36.9, "WHEN YOU SHOULD BE WITH ME INSTEAD?"),
        (39.5, "I KNOW I CAN TREAT YOU BETTER"),
        (44.5, "BETTER THAN HE CAN"),
        (50.5, "BETTER THAN HE CAN"),

    ]
 

BOX_W, BOX_H = 400, 300
FONT = ("Impact", 30)
BG_COLOR = "#ffffff"
FG_COLOR = "#211717"

RISE_SPEED = 70          # pixels per second every box moves upward
SPAWN_INTERVAL_MIN = 0   # not used directly; spawning follows LYRICS times
SAFE_EDGE_MARGIN = 0    # min distance from left/right screen edges
BOTTOM_SPAWN_OFFSET = 0  # how far above the bottom edge new boxes spawn



class LyricBox:
    """A single fixed-size lyric popup that rises forever and stays visible."""

    def __init__(self, master, text, x, y):
        self.master = master
        self.win = tk.Toplevel(master)
        self.win.overrideredirect(True)   # no title bar, popup look
        self.win.attributes("-topmost", True)
        self.win.configure(bg=BG_COLOR)
        # Lock the geometry to the fixed box size — same as Start window
        self.win.geometry(f"{BOX_W}x{BOX_H}+{int(x)}+{int(y)}")
        self.win.resizable(False, False)

        self.full_text = text

        self.label = tk.Label(
            self.win,
            text="",
            font=FONT,
            bg=BG_COLOR,
            fg=FG_COLOR,
            wraplength=BOX_W - 30,
            justify="center"
        )
        self.label.pack(expand=True, fill="both", padx=15, pady=15)

        self.typewriter_index = 0
        self.typewriter()

        self.x = x
        self.y = float(y)

    def rise(self, dy):
        self.y -= dy
        self.win.geometry(f"{BOX_W}x{BOX_H}+{int(self.x)}+{int(self.y)}")

    def is_offscreen(self):
        return self.y + BOX_H < -50
    
    def typewriter(self):
        if self.typewriter_index <= len(self.full_text):
            self.label.config(text=self.full_text[:self.typewriter_index])
            self.typewriter_index += 1
            # Faster typewriter speed
            self.win.after(75, self.typewriter)


class LyricFloatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lyric Float Controller")
        # The controller "Start" window uses the SAME fixed size/font
        # as every lyric box, per the same style.
        self.root.geometry(f"{BOX_W}x{BOX_H}")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.start_btn = tk.Button(
            root, text="Start", font=FONT, bg=BG_COLOR, fg=FG_COLOR,
            relief="flat", command=self.start
        )
        self.start_btn.pack(expand=True, fill="both", padx=15, pady=15)

        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()

        self.next_lyric_idx = 0
        self.boxes = []
        self.last_frame_time = None
        self.current_side = "left"  # Alternate between left and right

    def random_safe_x(self):
        """Alternate between left and right positions only."""
        # Calculate left and right positions - closer together
        center_x = self.screen_w // 2
        spacing = BOX_W + 60  # Small gap between boxes
        
        left_x = center_x - spacing
        right_x = center_x + 60
        
        # Alternate between left and right
        if self.current_side == "left":
            self.current_side = "right"
            return left_x
        else:
            self.current_side = "left"
            return right_x

    def start(self):
        self.start_btn.pack_forget()
        self.root.iconify()  
        self.start_time = time.time()
        self.last_frame_time = self.start_time

        if HAS_AUDIO and AUDIO_FILE:
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(AUDIO_FILE)
                pygame.mixer.music.play()
            except Exception as e:
                print(f"Audio failed to load: {e}")

        self.tick()

    def tick(self):
        now = time.time()
        elapsed = now - self.start_time
        dt = now - self.last_frame_time
        self.last_frame_time = now

        # Spawn any lyric windows whose time has come
        while (self.next_lyric_idx < len(LYRICS) and
               LYRICS[self.next_lyric_idx][0] <= elapsed):
            t, text = LYRICS[self.next_lyric_idx]
            x = self.random_safe_x()
            y = self.screen_h - BOX_H - BOTTOM_SPAWN_OFFSET
            box = LyricBox(self.root, text, x, y)
            self.boxes.append(box)
            self.next_lyric_idx += 1

        # Continuously rise ALL existing boxes upward, every frame
        dy = RISE_SPEED * dt
        for box in self.boxes:
            box.rise(dy)

        # Boxes stay visible permanently; we just stop tracking ones that
        # have scrolled fully off the top of the screen (saves memory),
        # but we never fade or destroy them early.
        still_visible = []
        for box in self.boxes:
            if box.is_offscreen():
                try:
                    box.win.destroy()
                except tk.TclError:
                    pass
            else:
                still_visible.append(box)
        self.boxes = still_visible

        # Keep looping as long as there are lyrics left to show or
        # boxes still on screen
        if self.next_lyric_idx < len(LYRICS) or self.boxes:
            self.root.after(16, self.tick)  # ~60fps


if __name__ == "__main__":
    root = tk.Tk()
    app = LyricFloatApp(root)
    root.mainloop()