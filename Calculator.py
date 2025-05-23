import tkinter as tk

def on_click(text):
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=16, font=("Arial", 24), justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        b = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: on_click(t))
        b.grid(row=i+1, column=j)

root.mainloop()
