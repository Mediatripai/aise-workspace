import tkinter as tk
from tkinter import ttk

def recommend_game():
    difficulty = difficulty_var.get()
    players = players_var.get()

    if difficulty not in ["Difficult", "Casual"]:
        result_label.config(text="Enter a valid difficulty.")
        return

    if players not in ["Singleplayer", "Multiplayer"]:
        result_label.config(text="Enter a valid number of players.")
        return

    if difficulty == "Difficult":
        if players == "Multiplayer":
            game = "Poker"
        else:
            game = "Klondike"
    else:  # Casual
        if players == "Multiplayer":
            game = "Hearts"
        else:
            game = "Clock"

    result_label.config(text=f"You should play {game}!")

# --- UI Setup ---
root = tk.Tk()
root.title("Game Recommender")
root.geometry("350x200")

difficulty_var = tk.StringVar()
players_var = tk.StringVar()

tk.Label(root, text="Select Difficulty:").pack(pady=5)
difficulty_menu = ttk.Combobox(
    root,
    textvariable=difficulty_var,
    values=["Difficult", "Casual"],
    state="readonly"
)
difficulty_menu.pack()

tk.Label(root, text="Select Mode:").pack(pady=5)
players_menu = ttk.Combobox(
    root,
    textvariable=players_var,
    values=["Singleplayer", "Multiplayer"],
    state="readonly"
)
players_menu.pack()

tk.Button(root, text="Recommend", command=recommend_game).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()