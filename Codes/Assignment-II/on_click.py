# Problem Statement: Customizable Text Styling Application

# Design a Tkinter GUI application that allows users to customize the style of a text displayed on the interface. Users should be able to change the font size, font style, font color, and background color of the displayed text by clicking a button.

# Requirements:
# The GUI should consist of:

# A Label widget displaying an initial text with default styling.
# A Button widget labeled "Change Style" to trigger the text style changes.
# Implementations for changing font size, font style, font color, and background color upon button click.
# Implement a function, let's call it change_style(), that:

# Modifies the font size to 14, font style to italic, font color to blue, and background color to light gray when called.
# Binds this function to the button click event.
# Ensure that the GUI layout is well-organized and visually appealing.


import tkinter as tk

def change_style():
    # Change font size
    label.config(font=("Helvetica", 14))
    # Change font style
    label.config(font=("Helvetica", 14, "italic"))
    # Change font color
    label.config(fg="blue")
    # Change background color
    label.config(bg="lightgray")

# Create the main window
window = tk.Tk()
window.title("Font and Color Example")

# Create a label with initial text and style
label = tk.Label(window, text="Hello, Tkinter!", font=("Helvetica", 12), fg="black", bg="white")
label.pack(pady=10)

# Create a button to trigger style change
button = tk.Button(window, text="Change Style", command=change_style)
button.pack()

# Start the Tkinter event loop
window.mainloop()
