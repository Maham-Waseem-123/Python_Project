import tkinter as tk
import random

# List of words
WORDS = ['python', 'hangman', 'challenge', 'programming', 'tkinter', 'project']

# Stick figure drawing steps
def draw_hangman(canvas, wrong):
    parts = [
        lambda: canvas.create_line(50, 230, 150, 230),           # base
        lambda: canvas.create_line(100, 230, 100, 50),           # pole
        lambda: canvas.create_line(100, 50, 180, 50),            # top bar
        lambda: canvas.create_line(180, 50, 180, 70),            # rope
        lambda: canvas.create_oval(160, 70, 200, 110),           # head
        lambda: canvas.create_line(180, 110, 180, 170),          # body
        lambda: canvas.create_line(180, 130, 160, 150),          # left arm
        lambda: canvas.create_line(180, 130, 200, 150),          # right arm
        lambda: canvas.create_line(180, 170, 160, 200),          # left leg
        lambda: canvas.create_line(180, 170, 200, 200)           # right leg
    ]
    if wrong < len(parts):
        parts[wrong]()

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word = random.choice(WORDS).upper()
        self.guessed = set()
        self.wrong_guesses = 0

        self.canvas = tk.Canvas(root, width=300, height=250, bg="white")
        self.canvas.pack()

        self.word_label = tk.Label(root, text=self.display_word(), font=("Courier", 18))
        self.word_label.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.message_label = tk.Label(root, text="", font=("Arial", 14), fg="red")
        self.message_label.pack(pady=5)

        self.create_letter_buttons()

    def display_word(self):
        return ' '.join([letter if letter in self.guessed else '_' for letter in self.word])

    def create_letter_buttons(self):
        for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            btn = tk.Button(self.buttons_frame, text=letter, width=4, command=lambda l=letter: self.guess(l))
            btn.grid(row=i//9, column=i%9, padx=2, pady=2)

    def guess(self, letter):
        if letter in self.guessed:
            return

        self.guessed.add(letter)

        if letter in self.word:
            self.word_label.config(text=self.display_word())
            if all(l in self.guessed for l in self.word):
                self.message_label.config(text="🎉 You Win!")
                self.disable_buttons()
        else:
            draw_hangman(self.canvas, self.wrong_guesses)
            self.wrong_guesses += 1
            if self.wrong_guesses == 10:
                self.word_label.config(text=' '.join(self.word))
                self.message_label.config(text="💀 You Lost!")
                self.disable_buttons()

    def disable_buttons(self):
        for child in self.buttons_frame.winfo_children():
            child.config(state="disabled")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
