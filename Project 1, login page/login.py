# we gonna create a log in window using tkinter

import tkinter as tk
from tkinter import messagebox

screen = tk.Tk()
screen.title("Login System")
screen.geometry("1000x800")
screen.configure(bg="white")

slide = tk.Label(screen, text="Hi there", font=("times new roman", 20, "bold"), fg="black", bg="white")

slide.pack(pady=5, anchor="n")

slide.pack(expand=True)
full_text = "Hi there!"
first_index = 0


def text_type():
    global first_index
    if first_index <= len(full_text):
        slide.config(text=full_text[:first_index])

        first_index += 1
        screen.after(100, text_type)

text_type()

users = {}

def sign_up():
    username = username_entry.get()

    password = password_entry.get()

    if username in users:
        messagebox.showerror("Error", "Username already exists! Try another one ")
    else:
        users[username] = password
        messagebox.showinfo("Success", "Sign Up Successful!")


def login():
    username = username_entry.get()

    password = password_entry.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# work on the widgets

# main frame will hold both username and password, also it's arrangements
main_frame = tk.Frame(screen)

main_frame.pack(expand=True, pady=300)

main_frame.pack_configure(padx=200)

username_frame = tk.Frame(main_frame)
username_frame.pack(pady=5)
username_label = tk.Label(username_frame, text="Username", font=("times new roman", 18, "bold"))
username_label.pack(side="left", padx=(0, 5))

username_entry = tk.Entry(username_frame, font=("times new roman", 16))
username_entry.pack(side="left")

password_frame = tk.Frame(main_frame)
password_frame.pack(pady=15)

password_label = tk.Label(password_frame, text="Password", font=("times new roman", 18, "bold"))
password_label.pack(side="left", padx=(0, 5))

password_entry = tk.Entry(password_frame, font=("times new roman", 16))
password_entry.pack(side="left")

# work on the buttons
# buttons are out of the main frame
buttons_frame = tk.Frame(screen, bg="white")
buttons_frame.pack(pady=50)
buttons_frame.pack_configure(padx=200)

sign_up_button = tk.Button(buttons_frame, text="Sign in", font=("times new roman", 14, "bold"), command=sign_up)
sign_up_button.pack(side="left", padx=10)  # space between buttons

login_button = tk.Button(buttons_frame, text="Login", font=("times new roman", 14, "bold"), command=login)
login_button.pack(side="left", padx=10)

screen.mainloop()
