# Problem Statement: Text Styling Customization Interface

# Develop a Tkinter GUI application that enables users to customize the styling of a displayed text through the use of separate buttons. The application should include three buttons, each responsible for modifying a different aspect of the text's style: font size, font color, and background color.

# Requirements:
# The GUI should feature:

# A Label widget displaying an initial text with default styling.
# Three Button widgets labeled "Change Font Size", "Change Font Color", and "Change Background Color", each assigned to a specific style modification function.
# Implementations for changing font size, font color, and background color upon clicking the respective buttons.
# Implement three separate functions, each responsible for modifying a particular aspect of the text's style:

# change_font_size(): Changes the font size of the displayed text to 14 when called (also font style).
# change_font_color(): Changes the font color of the displayed text to blue when called.
# change_background_color(): Changes the background color of the displayed text to light gray when called.
# Ensure that the GUI layout is well-organized and visually appealing, with the buttons positioned horizontally.


import tkinter as tk

def change_font_size():
    label.config(font=("Helvetica", 14, "italic"))

def change_font_color():
    label.config(fg="blue")

def change_background_color():
    label.config(bg="lightgray")

# Create the main window
window = tk.Tk()
window.title("Customizable Text Styling Application")

# Create a label with initial text and style
label = tk.Label(window, text="Hello, Tkinter!", font=("Helvetica", 12), fg="black", bg="white")
label.pack(pady=10)

# Create buttons to trigger different style changes
font_size_button = tk.Button(window, text="Change Font Size", command=change_font_size)
font_size_button.pack(side=tk.LEFT, padx=5)

font_color_button = tk.Button(window, text="Change Font Color", command=change_font_color)
font_color_button.pack(side=tk.LEFT, padx=5)

background_color_button = tk.Button(window, text="Change Background Color", command=change_background_color)
background_color_button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
window.mainloop()