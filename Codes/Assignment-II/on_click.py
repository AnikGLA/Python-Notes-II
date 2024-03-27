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
