import tkinter as tk  # Corrected spelling of tkinter

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Create main window
root = tk.Tk()
root.geometry("300x400")
root.title("Simple Calculator")

# Entry screen
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=10, relief=tk.RIDGE, justify='right')
entry.pack(fill="both", ipadx=8, ipady=8, padx=10, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

# Create and place buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)
    for btn in row:
        button = tk.Button(frame, text=btn, font='Arial 18', relief=tk.GROOVE, borderwidth=2)
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", click)

# Run the app
root.mainloop()
