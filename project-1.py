import tkinter as tk
from tkinter import messagebox
import re

def evaluate_strength(password):
    # Rule 1: Weak (Very short)
    if len(password) < 5:
        return "WEAK", "#ff4d4d"  # Bright Red

    # Rule 2: Strong (e.g., MyTASK@1)
    # Checks for: Upper, Lower, and either a Number or Special Character
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    if has_upper and has_lower and (has_digit or has_special):
        return "STRONG", "#2ecc71"  # Neon Green

    # Rule 3: Moderate (e.g., internship task 1)
    return "MODERATE", "#f1c40f"  # Gold/Yellow

def update_display():
    password = password_entry.get()
    if not password:
        result_label.config(text="Strength: ---", fg="#bdc3c7")
        return
    
    status, color = evaluate_strength(password)
    result_label.config(text=f"STRENGTH: {status}", fg=color)

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        eye_btn.config(text="👁") # Eye closed/Hidden state
    else:
        password_entry.config(show='')
        eye_btn.config(text="🔓") # Eye open/Show state

# --- Main Window Setup ---
root = tk.Tk()
root.title("Hunar Intern - Advanced Password Analyst")
root.geometry("600x500") # Bigger screen size
root.configure(bg="#0a192f") # Deep Dark Blue (Cybersecurity theme)

# Header
header = tk.Label(root, text="PASSWORD SECURITY ANALYZER", 
                 font=("Verdana", 20, "bold"), bg="#0a192f", fg="#64ffda", pady=30)
header.pack()

# Container for Password and Eye Icon
input_frame = tk.Frame(root, bg="#0a192f")
input_frame.pack(pady=20)

instruction = tk.Label(input_frame, text="Enter your password to scan:", 
                      font=("Arial", 12), bg="#0a192f", fg="#8892b0")
instruction.pack(anchor="w")

# Sub-frame to hold Entry and Eye Button side-by-side
entry_frame = tk.Frame(input_frame, bg="#0a192f")
entry_frame.pack()

password_entry = tk.Entry(entry_frame, font=("Consolas", 16), width=25, 
                         show="*", bg="#172a45", fg="white", insertbackground="white", borderwidth=0)
password_entry.pack(side="left", padx=5, ipady=5)

# Eye Icon Button (Toggle)
eye_btn = tk.Button(entry_frame, text="👁", command=toggle_password, 
                   font=("Arial", 12), bg="#64ffda", fg="#0a192f", 
                   width=3, relief="flat", cursor="hand2")
eye_btn.pack(side="left")

# Analyze Button
check_btn = tk.Button(root, text="SCAN PASSWORD", command=update_display,
                     font=("Arial", 12, "bold"), bg="#64ffda", fg="#0a192f", 
                     padx=40, pady=10, relief="flat", cursor="hand2")
check_btn.pack(pady=30)

# Result Output
result_label = tk.Label(root, text="STRENGTH: ---", 
                       font=("Courier New", 24, "bold"), bg="#0a192f", fg="#bdc3c7")
result_label.pack(pady=20)

# Footer
footer = tk.Label(root, text="Developed for Hunar Intern - Task 1", 
                 font=("Arial", 10), bg="#0a192f", fg="#495670")
footer.pack(side="bottom", pady=20)

root.mainloop()
