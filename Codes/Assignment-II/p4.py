import tkinter as tk

def on_radio_select():
    selected_value.set("Selected: " + radio_var.get())

window = tk.Tk()
window.title("Radiobutton Example")

options = ["Option 1", "Option 2", "Option 3"]

radio_var = tk.StringVar()
selected_value = tk.StringVar()

for option in options:
    radio_button = tk.Radiobutton(window, text=option, variable=radio_var, value=option, command=on_radio_select)
    radio_button.pack()

selection_label = tk.Label(window, textvariable=selected_value)
selection_label.pack(pady=10)

window.mainloop()