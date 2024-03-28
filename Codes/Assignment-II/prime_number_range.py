# Problem Statement:
# Develop a Python application that allows users to identify prime numbers within a specified range or individually. The application should provide a graphical user interface (GUI) using Tkinter, where users can input a starting and an ending number to find all prime numbers within that range. 


import tkinter as tk

def find_primes():
    start_num = int(start_entry.get())
    end_num = int(end_entry.get())
    primes = []
    for num in range(start_num, end_num + 1):
        if num > 1:  # all prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    result_label.config(text="Prime Numbers: " + ", ".join(map(str, primes)))

# Create the main window
root = tk.Tk()
root.title("Prime Number Finder")

# Create entry widgets for start and end numbers
start_entry = tk.Entry(root)
end_entry = tk.Entry(root)
start_entry.pack()
end_entry.pack()

# Create a button to find prime numbers
find_button = tk.Button(root, text="Find Primes", command=find_primes)
find_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="Prime Numbers: ")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()