import tkinter as tk
from tkinter import ttk

def calculate_love():
    name1 = entry_name1.get()
    name2 = entry_name2.get()

    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count('t')
    r = lower_names.count('r')
    u = lower_names.count('u')
    e = lower_names.count('e')
    first_digit = t + r + u + e

    l = lower_names.count('l')
    o = lower_names.count('o')
    v = lower_names.count('v')
    e = lower_names.count('e')
    second_digit = l + o + v + e

    score = str(first_digit) + str(second_digit)

    result_label.config(text=f"Your love match is {score}%")

# Create the main window
root = tk.Tk()
root.title("Love Calculator")

# Configure window size and style
root.geometry("400x250")
style = ttk.Style()
style.configure('TButton', padding=(10, 5))

# Create and place widgets
label1 = ttk.Label(root, text="Enter your name:")
label1.pack(pady=10)

entry_name1 = ttk.Entry(root)
entry_name1.pack(pady=5)

label2 = ttk.Label(root, text="Enter their name:")
label2.pack(pady=10)

entry_name2 = ttk.Entry(root)
entry_name2.pack(pady=5)

calculate_button_text = "Calculate Love \u2764️"  # Unicode heart symbol
calculate_button = ttk.Button(root, text=calculate_button_text, command=calculate_love)
calculate_button.pack(pady=15)

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
