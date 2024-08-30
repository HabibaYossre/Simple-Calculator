from tkinter import *

# Function to update the entry widget
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, END)

# Function to perform calculation
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

root = Tk()
root.title("Simple Calculator")

# Adjust the size of the window
root.geometry("350x485")
#root.resizable(width=0,height=0)
root.configure(bg="#f0f0f0")

# Define colors
button_bg = "#ffcccc"
button_fg = "#333333"
entry_bg = "#fffaf0"
entry_fg = "#333333"
highlight_bg = "#ff9999"
clear_bg = "#ff6666"
equal_bg = "#ffcc99"

# Entry widget for display
entry = Entry(root, bd=5, width=16, font=("Arial", 24), bg=entry_bg, fg=entry_fg, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, ipady=10)

# List of button texts and their positions
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Creating buttons
for (text, row, col) in buttons:
    if text == "C":
        btn = Button(root, text=text, font=("Arial", 20), bg=clear_bg, fg=button_fg, bd=0, padx=20, pady=20, 
                     command=button_clear, relief=GROOVE, highlightbackground=highlight_bg, activebackground=clear_bg, activeforeground=button_fg)
    elif text == "=":
        btn = Button(root, text=text, font=("Arial", 20), bg=equal_bg, fg=button_fg, bd=0, padx=20, pady=20, 
                     command=button_equal, relief=GROOVE, highlightbackground=highlight_bg, activebackground=equal_bg, activeforeground=button_fg)
    else:
        btn = Button(root, text=text, font=("Arial", 20), bg=button_bg, fg=button_fg, bd=0, padx=20, pady=20, 
                     command=lambda t=text: button_click(t), relief=GROOVE, highlightbackground=highlight_bg, activebackground=button_bg, activeforeground=button_fg)
    
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
