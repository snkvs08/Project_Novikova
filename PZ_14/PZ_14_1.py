#вариант 11
import tkinter as tk
from tkinter import messagebox

def on_sign_up():
    first_name = entry_first_name.get().strip()
    last_name = entry_last_name.get().strip()
    email = entry_email.get().strip()
    website = entry_website.get().strip()
    password = entry_password.get()
    password_conf = entry_password_conf.get()
    
    if first_name == "" or first_name == "First Name":
        messagebox.showerror("Ошибка", "Введите First Name")
        return
    if last_name == "" or last_name == "Last Name":
        messagebox.showerror("Ошибка", "Введите Last Name")
        return
    if email == "" or email == "Email address":
        messagebox.showerror("Ошибка", "Введите Email")
        return
    if password == "" or password == "8-10 characters":
        messagebox.showerror("Ошибка", "Введите пароль")
        return
    if password != password_conf:
        messagebox.showerror("Ошибка", "Пароли не совпадают!")
        return
    
    messagebox.showinfo("Успех", f"Добро пожаловать, {first_name} {last_name}!")

def on_focus_in(entry, placeholder, is_password=False):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black")
        if is_password:
            entry.config(show="*")

def on_focus_out(entry, placeholder, is_password=False):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="gray")
        if is_password:
            entry.config(show="")

root = tk.Tk()
root.title("Sign Up Form")
root.geometry("480x620")
root.resizable(False, False)
root.configure(bg='#c0c0c0')

canvas = tk.Canvas(root, width=400, height=560, bg='#c0c0c0', highlightthickness=0)
canvas.place(relx=0.5, rely=0.5, anchor='center')

card_bg = '#d4d4d4'  
canvas.create_rounded_rect = lambda x1, y1, x2, y2, radius, **kwargs: (
    canvas.create_polygon(
        (x1+radius, y1), (x2-radius, y1), (x2, y1), (x2, y1+radius),
        (x2, y2-radius), (x2, y2), (x2-radius, y2), (x1+radius, y2),
        (x1, y2), (x1, y2-radius), (x1, y1+radius), (x1, y1),
        smooth=True, **kwargs
    )
)
canvas.create_rounded_rect(0, 0, 400, 560, 15, fill=card_bg, outline='#4a4a4a', width=3)

canvas.create_rounded_rect(0, 0, 400, 55, 15, fill='#4a4a4a', outline='#4a4a4a', width=0)

canvas.create_rectangle(0, 40, 400, 55, fill='#4a4a4a', outline='')

canvas.create_text(200, 27, text="Contact Us", font=("Arial", 20, "bold"), anchor='center', fill='black')

form_frame = tk.Frame(canvas, bg='#d4d4d4')
form_frame.place(x=35, y=75, width=330, height=470)

tk.Label(form_frame, text="First Name", font=("Arial", 10), bg='#d4d4d4', fg="#333").pack(anchor="w", pady=(0, 5))
entry_first_name = tk.Entry(form_frame, width=35, font=("Arial", 10), fg="gray", relief='sunken', bd=2)
entry_first_name.insert(0, "First Name")
entry_first_name.pack(anchor="w", pady=(0, 15))
entry_first_name.bind("<FocusIn>", lambda e: on_focus_in(entry_first_name, "First Name"))
entry_first_name.bind("<FocusOut>", lambda e: on_focus_out(entry_first_name, "First Name"))

tk.Label(form_frame, text="Last Name", font=("Arial", 10), bg='#d4d4d4', fg="#333").pack(anchor="w", pady=(0, 5))
entry_last_name = tk.Entry(form_frame, width=35, font=("Arial", 10), fg="gray", relief='sunken', bd=2)
entry_last_name.insert(0, "Smith")
entry_last_name.pack(anchor="w", pady=(0, 15))
entry_last_name.bind("<FocusIn>", lambda e: on_focus_in(entry_last_name, "Smith"))
entry_last_name.bind("<FocusOut>", lambda e: on_focus_out(entry_last_name, "Smith"))

tk.Label(form_frame, text="Email", font=("Arial", 10), bg='#d4d4d4', fg="#333").pack(anchor="w", pady=(0, 5))
entry_email = tk.Entry(form_frame, width=35, font=("Arial", 10), fg="gray", relief='sunken', bd=2)
entry_email.insert(0, "Email address")
entry_email.pack(anchor="w", pady=(0, 15))
entry_email.bind("<FocusIn>", lambda e: on_focus_in(entry_email, "Email address"))
entry_email.bind("<FocusOut>", lambda e: on_focus_out(entry_email, "Email address"))

tk.Label(form_frame, text="Website", font=("Arial", 10), bg='#d4d4d4', fg="#333").pack(anchor="w", pady=(0, 5))
entry_website = tk.Entry(form_frame, width=35, font=("Arial", 10), fg="gray", relief='sunken', bd=2)
entry_website.insert(0, "www.example.com")
entry_website.pack(anchor="w", pady=(0, 15))
entry_website.bind("<FocusIn>", lambda e: on_focus_in(entry_website, "www.example.com"))
entry_website.bind("<FocusOut>", lambda e: on_focus_out(entry_website, "www.example.com"))

tk.Label(form_frame, text="Password", font=("Arial", 10), bg='#d4d4d4', fg="#333").pack(anchor="w", pady=(0, 5))
entry_password = tk.Entry(form_frame, width=35, font=("Arial", 10), fg="gray", show="", relief='sunken', bd=2)
entry_password.insert(0, "8-10 characters")
entry_password.pack(anchor="w", pady=(0, 15))
entry_password.bind("<FocusIn>", lambda e: on_focus_in(entry_password, "8-10 characters", True))
entry_password.bind("<FocusOut>", lambda e: on_focus_out(entry_password, "8-10 characters", True))

tk.Label(form_frame, text="Password Confirmation", font=("Arial", 10), bg='#d4d4d4', fg="#333").pack(anchor="w", pady=(0, 5))
entry_password_conf = tk.Entry(form_frame, width=35, font=("Arial", 10), fg="gray", show="", relief='sunken', bd=2)
entry_password_conf.insert(0, "Type your password again")
entry_password_conf.pack(anchor="w", pady=(0, 20))
entry_password_conf.bind("<FocusIn>", lambda e: on_focus_in(entry_password_conf, "Type your password again", True))
entry_password_conf.bind("<FocusOut>", lambda e: on_focus_out(entry_password_conf, "Type your password again", True))

sign_up_btn = tk.Button(form_frame, text="Sign Up", command=on_sign_up,
                        bg="#4a4a4a", fg="white", font=("Arial", 10, "bold"),
                        padx=35, pady=7, relief='raised', bd=2)
sign_up_btn.pack(pady=(10, 0))

root.mainloop()