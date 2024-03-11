import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

# Create the main window
window = tk.Tk()
window.title("Tkinter Example")

# Create a label
label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=10) #pady=10 adds some vertical padding.
#The pack() method is used to organize and display the widget

# Create a button
button = tk.Button(window, text="Click me!", command=on_button_click)
button.pack()

# Start the Tkinter event loop
window.mainloop()