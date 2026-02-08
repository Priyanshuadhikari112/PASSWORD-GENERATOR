
import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Password Generator")
        self.root.geometry("420x350")
        self.root.resizable(False, False)

        
        title = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"))
        title.pack(pady=10)

        
        tk.Label(root, text="Password Length:", font=("Arial", 12)).pack()
        self.length_entry = tk.Entry(root, font=("Arial", 12))
        self.length_entry.pack(pady=5)

        
        options_frame = tk.Frame(root)
        options_frame.pack(pady=10)

        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digit_var = tk.BooleanVar(value=True)
        self.symbol_var = tk.BooleanVar(value=True)

        tk.Checkbutton(options_frame, text="Uppercase", variable=self.upper_var).grid(row=0, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Lowercase", variable=self.lower_var).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Digits", variable=self.digit_var).grid(row=0, column=1, sticky="w")
        tk.Checkbutton(options_frame, text="Symbols", variable=self.symbol_var).grid(row=1, column=1, sticky="w")

    
        gen_btn = tk.Button(root, text="Generate Password", command=self.generate_password)
        gen_btn.pack(pady=10)

        
        self.result_entry = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
        self.result_entry.pack(pady=5)

       
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        copy_btn = tk.Button(btn_frame, text="Copy", command=self.copy_password)
        copy_btn.grid(row=0, column=0, padx=5)

        reset_btn = tk.Button(btn_frame, text="Reset", command=self.reset_fields)
        reset_btn.grid(row=0, column=1, padx=5)

    
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError

            char_pool = ""
            if self.upper_var.get():
                char_pool += string.ascii_uppercase
            if self.lower_var.get():
                char_pool += string.ascii_lowercase
            if self.digit_var.get():
                char_pool += string.digits
            if self.symbol_var.get():
                char_pool += string.punctuation

            if not char_pool:
                messagebox.showwarning("Selection Error", "Select at least one character type.")
                return

            password = ''.join(random.choice(char_pool) for _ in range(length))

            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, password)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for length.")

    
    def copy_password(self):
        password = self.result_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Empty", "No password to copy.")

   
    def reset_fields(self):
        self.length_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)



if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
