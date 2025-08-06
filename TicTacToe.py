import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Colorful Tic-Tac-Toe")
        self.root.configure(bg="lightblue")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.colors = ["#FFC0CB", "#90EE90", "#ADD8E6"]  # Button colors
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                color = self.colors[(row + col) % 3]
                btn = tk.Button(self.root, text="", font=("Arial", 36), width=5, height=2,
                                bg=color, activebackground="white",
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = btn

    def on_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(
                text=self.current_player,
                disabledforeground="red" if self.current_player == "X" else "blue",
                state="disabled"
            )

            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"🎉 Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a Draw! 🤝")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Row
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Column
                return True
        if all(self.board[i][i] == player for i in range(3)):      # Diagonal
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):  # Anti-diagonal
            return True
        return False

    def check_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                color = self.colors[(row + col) % 3]
                btn = self.buttons[row][col]
                btn.config(text="", state="normal", bg=color)
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
