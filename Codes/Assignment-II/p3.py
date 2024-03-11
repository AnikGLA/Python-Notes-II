import tkinter as tk

def on_select(event):
    selected_item = listbox.get(listbox.curselection())
    selection_label.config(text="Selected: " + selected_item)

window = tk.Tk()
window.title("Listbox Example")

options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

listbox = tk.Listbox(window, selectmode=tk.SINGLE)
for option in options:
    listbox.insert(tk.END, option)
listbox.pack(pady=10)

scrollbar = tk.Scrollbar(window, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

listbox.bind('<<ListboxSelect>>', on_select)

selection_label = tk.Label(window, text="Selected: None")
selection_label.pack(pady=10)

window.mainloop()