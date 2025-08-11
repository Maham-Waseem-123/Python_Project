import tkinter as tk
import random

class BalloonPopGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎈 Balloon Pop Game")
        self.root.geometry("400x600")
        self.canvas = tk.Canvas(root, width=400, height=600, bg="skyblue")
        self.canvas.pack()

        self.score = 0
        self.lives = 5
        self.balloons = []

        self.speed = 5  # Initial balloon speed
        self.level = 1  # Game level to control speed increase

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.place(x=10, y=10)

        self.lives_label = tk.Label(root, text="Lives: 5", font=("Arial", 14))
        self.lives_label.place(x=300, y=10)

        self.level_label = tk.Label(root, text="Level: 1", font=("Arial", 14))
        self.level_label.place(x=160, y=10)

        self.spawn_balloon()
        self.move_balloons()
        self.increase_speed()

    def spawn_balloon(self):
        x = random.randint(20, 360)
        color = random.choice(['red', 'yellow', 'green', 'blue', 'purple'])
        balloon = self.canvas.create_oval(x, 580, x+40, 620, fill=color, outline="black")
        self.canvas.tag_bind(balloon, "<Button-1>", lambda event, b=balloon: self.pop_balloon(b))
        self.balloons.append((balloon, x, 580))  # (id, x, y)
        if self.lives > 0:
            self.root.after(1000, self.spawn_balloon)

    def move_balloons(self):
        for i, (balloon, x, y) in enumerate(self.balloons):
            if self.canvas.coords(balloon):  # Check if balloon is still on screen
                self.canvas.move(balloon, 0, -self.speed)
                y -= self.speed
                if y < 0:
                    self.canvas.delete(balloon)
                    self.lives -= 1
                    self.lives_label.config(text=f"Lives: {self.lives}")
                    if self.lives == 0:
                        self.end_game()
                else:
                    self.balloons[i] = (balloon, x, y)
        if self.lives > 0:
            self.root.after(50, self.move_balloons)

    def pop_balloon(self, balloon):
        if self.canvas.coords(balloon):  # Check if balloon is still there
            self.canvas.delete(balloon)
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

    def increase_speed(self):
        if self.lives > 0:
            self.level += 1
            self.speed += 0.5  # Increase speed gradually
            self.level_label.config(text=f"Level: {self.level}")
            self.root.after(5000, self.increase_speed)  # Increase every 5 seconds

    def end_game(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 300, text=f"Game Over!\nScore: {self.score}", font=("Arial", 24), fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    game = BalloonPopGame(root)
    root.mainloop()
