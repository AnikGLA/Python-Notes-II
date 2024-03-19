
# Problem Statement: String Reversal GUI

# You are tasked with developing a graphical user interface (GUI) application in Python using Tkinter that reverses a string input by the user. The application should ensure that only string inputs are accepted and should display the reversed string on the interface.

import tkinter as tk

def reverse_string():
    input_string = entry.get()

    if not input_string.isalpha():
        result_label.config(text="Please enter a valid string.")
        return

    reversed_string = reverse_without_builtin(input_string)
    result_label.config(text=f"Reversed string: {reversed_string}")

def reverse_without_builtin(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

root = tk.Tk()
root.title("String Reversal")

label = tk.Label(root, text="Enter a string:")
label.pack()

entry = tk.Entry(root)
entry.pack()

reverse_button = tk.Button(root, text="Reverse", command=reverse_string)
reverse_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()