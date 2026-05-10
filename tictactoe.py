import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")

# Variables
current_player = "X"
board = [""] * 9


# Check winner
def check_winner():
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] != "":
            return True

    return False


# Check draw
def check_draw():
    return "" not in board


# Button click function
def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
            return

        if check_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
            return

        current_player = "O" if current_player == "X" else "X"


# Reset game
def reset_game():
    global current_player, board

    current_player = "X"
    board = [""] * 9

    for button in buttons:
        button.config(text="")


# Create buttons
buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 20),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)


# Reset button
reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 14),
    command=reset_game
)

reset_btn.grid(row=3, column=0, columnspan=3, pady=20)

# Run app
root.mainloop()