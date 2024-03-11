import tkinter as tk

def on_submit():
    result_label.config(text="Hello, " + entry.get())

window = tk.Tk()
window.title("Entry Widget Example")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.pack()

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()