# Problem Statement:
# You are tasked with developing a simple Withdrawal Application using Python's Tkinter library. The application should allow users to input a withdrawal amount and process the withdrawal. If the withdrawal amount is valid and does not exceed the current balance, the application should update the balance and display the updated amount. However, if the withdrawal amount exceeds the current balance or is invalid, appropriate error messages should be displayed to the user.


import tkinter as tk
from tkinter import messagebox

class WithdrawalApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Withdrawal App")
        
        self.current_balance = 1000  # Default balance
        
        # Create and place the label for current balance
        self.balance_label = tk.Label(master, text=f"Current Balance: {self.current_balance}")
        self.balance_label.pack()
        
        # Create and place the entry widget for withdrawal amount
        self.amount_label = tk.Label(master, text="Enter Withdrawal Amount:")
        self.amount_label.pack()
        
        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()
        
        # Create and place the withdraw button
        self.withdraw_button = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()
        
    def withdraw(self):
        # Get the withdrawal amount from the entry widget
        withdrawal_amount = self.amount_entry.get()
        
        # Check if the withdrawal amount is a valid number
        try:
            withdrawal_amount = float(withdrawal_amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid withdrawal amount")
            return
        
        # Check if the withdrawal amount is positive
        if withdrawal_amount <= 0:
            messagebox.showerror("Error", "Withdrawal amount must be positive")
            return
        
        # Check if the withdrawal amount exceeds the current balance
        if withdrawal_amount > self.current_balance:
            messagebox.showerror("Error", "Insufficient funds")
            return
        
        # Update the current balance and display it in the label
        self.current_balance -= withdrawal_amount
        self.balance_label.config(text=f"Current Balance: {self.current_balance}")
        messagebox.showinfo("Withdrawal Successful", f"Withdrawal of {withdrawal_amount} processed")

# Create the Tkinter root window
root = tk.Tk()

# Create an instance of WithdrawalApp
app = WithdrawalApp(root)

# Start the Tkinter event loop
root.mainloop()