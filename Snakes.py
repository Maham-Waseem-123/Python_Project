import tkinter as tk
import random

# Constants
MOVE_INCREMENT = 20
GAME_SPEED = 100

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🌈 Colorful Snake Game 🐍")
        
        # Canvas
        self.canvas = tk.Canvas(root, bg="#1e1e2f", width=400, height=400)
        self.canvas.pack()

        self.restart_button = None
        self.quit_button = None

        self.initialize_game()

        self.root.bind("<Key>", self.change_direction)
        self.run_game()

    def initialize_game(self):
        # Score tracking
        self.score = 0
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.place_food()
        self.direction = "Right"
        self.running = True

    def draw(self):
        self.canvas.delete("all")
        
        # Score
        self.canvas.create_text(
            200, 10, fill="white", font=("Arial", 14, "bold"), text=f"Score: {self.score}"
        )

        # Snake with gradient colors
        colors = ["#00FF00", "#33FF99", "#66FF66", "#99FF33", "#CCFF00"]
        for i, (x, y) in enumerate(self.snake):
            color = colors[i % len(colors)]
            self.canvas.create_rectangle(
                x, y, x + MOVE_INCREMENT, y + MOVE_INCREMENT, fill=color, outline="#111"
            )

        # Food
        fx, fy = self.food
        self.canvas.create_oval(
            fx, fy, fx + MOVE_INCREMENT, fy + MOVE_INCREMENT, fill="#FF007F", outline="#FFD1DC", width=2
        )

    def move(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Right":
            head_x += MOVE_INCREMENT
        elif self.direction == "Left":
            head_x -= MOVE_INCREMENT
        elif self.direction == "Up":
            head_y -= MOVE_INCREMENT
        elif self.direction == "Down":
            head_y += MOVE_INCREMENT

        new_head = (head_x, head_y)

        # Collision check
        if (
            new_head in self.snake or
            head_x < 0 or head_x >= 400 or
            head_y < 0 or head_y >= 400
        ):
            self.running = False
            self.game_over_screen()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 10
            self.food = self.place_food()
        else:
            self.snake.pop()

    def place_food(self):
        while True:
            x = random.randint(0, 19) * MOVE_INCREMENT
            y = random.randint(0, 19) * MOVE_INCREMENT
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        key = event.keysym
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if key in ["Up", "Down", "Left", "Right"]:
            if self.direction != opposite.get(key):
                self.direction = key

    def game_over_screen(self):
        """Display a game over message with Restart and Quit buttons."""
        self.canvas.delete("all")
        self.canvas.create_text(
            200, 160,
            fill="red",
            font=("Arial", 28, "bold"),
            text="GAME OVER"
        )
        self.canvas.create_text(
            200, 200,
            fill="white",
            font=("Arial", 14),
            text=f"Final Score: {self.score}"
        )

        # Restart Button
        self.restart_button = tk.Button(
            self.root, text="🔄 Restart", font=("Arial", 12, "bold"),
            command=self.restart_game, bg="#4CAF50", fg="white"
        )
        self.restart_button.place(x=120, y=240, width=80, height=30)

        # Quit Button
        self.quit_button = tk.Button(
            self.root, text="❌ Quit", font=("Arial", 12, "bold"),
            command=self.root.destroy, bg="#f44336", fg="white"
        )
        self.quit_button.place(x=210, y=240, width=80, height=30)

    def restart_game(self):
        """Restart the game by resetting variables."""
        if self.restart_button:
            self.restart_button.destroy()
        if self.quit_button:
            self.quit_button.destroy()
        
        self.initialize_game()
        self.draw()
        self.run_game()

    def run_game(self):
        if self.running:
            self.move()
            if self.running:  # Only draw if still alive
                self.draw()
            self.root.after(GAME_SPEED, self.run_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
