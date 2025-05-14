import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Modern Calculator")
root.resizable(False, False)  # Disable resizing

# Set modern color scheme
bg_color = "#2e2e2e"
button_bg = "#3e3e3e"
button_fg = "#ffffff"
operator_bg = "#ff9500"
equal_bg = "#ff2d55"
clear_bg = "#a5a5a5"
entry_bg = "#1e1e1e"
entry_fg = "#ffffff"

root.configure(bg=bg_color)

# Create an entry widget for the display
entry = tk.Entry(root, width=14, font=("Segoe UI", 36), borderwidth=0, relief=tk.FLAT, justify='right', bg=entry_bg, fg=entry_fg, insertbackground='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 10), ipady=10)

# Define the button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Create buttons with modern styling
for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        if button_text.isdigit():  # Numbers
            btn_bg = button_bg
        elif button_text == "C":   # Clear button
            btn_bg = clear_bg
        elif button_text == "=":   # Equal button
            btn_bg = equal_bg
        else:                      # Operators
            btn_bg = operator_bg
            
        button = tk.Button(root, text=button_text, 
                          font=("Segoe UI", 18, 'bold'),
                          bg=btn_bg, fg=button_fg,
                          borderwidth=0, relief=tk.FLAT,
                          activebackground=btn_bg,
                          activeforeground=button_fg,
                          command=lambda text=button_text: on_click(text))
        
        # Add some padding and make buttons slightly rounded
        button.grid(row=i+1, column=j, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
        
        # Configure grid to expand buttons
        root.grid_columnconfigure(j, weight=1)
    root.grid_rowconfigure(i+1, weight=1)

# Add some hover effects
def on_enter(e):
    e.widget['bg'] = '#505050' if e.widget['bg'] == button_bg else e.widget['bg']
    if e.widget['bg'] == operator_bg:
        e.widget['bg'] = '#ffaa33'
    elif e.widget['bg'] == equal_bg:
        e.widget['bg'] = '#ff3d6d'
    elif e.widget['bg'] == clear_bg:
        e.widget['bg'] = '#b5b5b5'

def on_leave(e):
    if e.widget['text'].isdigit():
        e.widget['bg'] = button_bg
    elif e.widget['text'] == "C":
        e.widget['bg'] = clear_bg
    elif e.widget['text'] == "=":
        e.widget['bg'] = equal_bg
    else:
        e.widget['bg'] = operator_bg

# Bind hover effects to all buttons
for child in root.winfo_children():
    if isinstance(child, tk.Button):
        child.bind("<Enter>", on_enter)
        child.bind("<Leave>", on_leave)

# Run the application
root.mainloop()