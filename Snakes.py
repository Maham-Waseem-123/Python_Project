import tkinter as tk
import random

# Constants
MOVE_INCREMENT = 20   # Size of each block the snake moves
GAME_SPEED = 100      # Milliseconds between game updates

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        
        # Create the game canvas
        self.canvas = tk.Canvas(root, bg="black", width=400, height=400)
        self.canvas.pack()
        
        # Initialize snake (3 segments)
        self.snake = [(100, 100), (80, 100), (60, 100)]
        
        # Place initial food
        self.food = self.place_food()
        
        # Start moving right
        self.direction = "Right"
        
        # Game running state
        self.running = True

        # Bind keyboard keys for direction change
        self.root.bind("<Key>", self.change_direction)

        # Start game loop
        self.run_game()

    def draw(self):
        """Draw snake and food on the canvas."""
        self.canvas.delete("all")  # Clear canvas

        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(
                x, y, x + MOVE_INCREMENT, y + MOVE_INCREMENT, fill="green"
            )

        # Draw food
        fx, fy = self.food
        self.canvas.create_oval(
            fx, fy, fx + MOVE_INCREMENT, fy + MOVE_INCREMENT, fill="red"
        )

    def move(self):
        """Move the snake in the current direction."""
        head_x, head_y = self.snake[0]

        # Determine new head position
        if self.direction == "Right":
            head_x += MOVE_INCREMENT
        elif self.direction == "Left":
            head_x -= MOVE_INCREMENT
        elif self.direction == "Up":
            head_y -= MOVE_INCREMENT
        elif self.direction == "Down":
            head_y += MOVE_INCREMENT

        new_head = (head_x, head_y)

        # Check for collisions
        if (
            new_head in self.snake or               # Hits itself
            head_x < 0 or head_x >= 400 or          # Hits left/right wall
            head_y < 0 or head_y >= 400             # Hits top/bottom wall
        ):
            self.running = False
            self.canvas.create_text(
                200, 200, fill="white", font="Arial 20 bold", text="Game Over!"
            )
            return

        # Add new head to the snake
        self.snake.insert(0, new_head)

        # Check for food collision
        if new_head == self.food:
            self.food = self.place_food()  # Place new food
        else:
            self.snake.pop()  # Remove tail segment

    def place_food(self):
        """Place food in a random location not occupied by the snake."""
        while True:
            x = random.randint(0, 19) * MOVE_INCREMENT
            y = random.randint(0, 19) * MOVE_INCREMENT
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        """Change snake direction based on arrow key press."""
        key = event.keysym
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}

        if key in ["Up", "Down", "Left", "Right"]:
            if self.direction != opposite.get(key):
                self.direction = key

    def run_game(self):
        """Main game loop."""
        if self.running:
            self.move()
            self.draw()
            self.root.after(GAME_SPEED, self.run_game)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
