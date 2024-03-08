import tkinter as tk
import string
import random

class Pass:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("Password Generator")
        self.main.geometry("400x400")
        self.l_label = tk.Label(self.main, text="Enter Password Length:")
        self.l_label.pack(pady=10)
        self.l_entry = tk.Entry(self.main)
        self.l_entry.pack(pady=10)
        self.g_button = tk.Button(self.main, text="Generate Password", command=self.g_and_d)
        self.g_button.pack(pady=10)
        self.pass_label = tk.Label(self.main, text="")
        self.pass_label.pack(pady=10)
        tk.mainloop()

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def g_and_d(self):
        try:
            length = int(self.l_entry.get())
            if length <= 0:
                raise ValueError("Please enter a positive integer for password length.")
            password = self.generate_password(length)
            self.pass_label.config(text=f"Generated Password: {password}")
        except ValueError as e:
            self.pass_label.config(text=str(e))

password = Pass()
