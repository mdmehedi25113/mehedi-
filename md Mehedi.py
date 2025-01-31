import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = screen.get()
            if expression:
                result = str(eval(expression))
                screen.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")
    elif text == "C":
        screen.set("")
    elif text == "←":
        screen.set(screen.get()[:-1])
    else:
        screen.set(screen.get() + text)
root = tk.Tk()
root.title("Calculator")
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold", justify="right", bd=8, relief=tk.SUNKEN)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+']
frame = tk.Frame(root)
frame.pack()

for i, button in enumerate(buttons):
    btn = tk.Button(frame, text=button, font="lucida 15 bold", width=5, height=2, relief=tk.RAISED, bg="lightgray")
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    btn.bind("<Button-1>", click)
root.mainloop()
