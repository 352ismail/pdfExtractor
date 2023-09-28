import tkinter
from tkinter import messagebox
import MainForm 
from tkPDFViewer import tkPDFViewer as pdf

form_bg_color = '#343838'
window = tkinter.Tk()
window.title("Paper Generator")
window.iconbitmap(MainForm.image_path)
window.geometry('800x400')
window.configure(bg=form_bg_color)

def close_current_window():
    window.destroy()

def login():
    username = "ismailkhan"
    password = "ismailkhan"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")


frame = tkinter.Frame(window , bg=form_bg_color)

login_label = tkinter.Label(frame, text="Login First", bg=form_bg_color, fg="#f7faf8", font=("Arial", 20,'bold'))
username_label = tkinter.Label(frame, text="Username", bg=form_bg_color, fg="#ffffff", font=("Arial", 14))
password_label = tkinter.Label(frame, text="Password", bg=form_bg_color, fg="#ffffff", font=("Arial", 14))
username_entry = tkinter.Entry(frame, font=("Arial", 14), bg=form_bg_color,fg="#ffffff")
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 14) , bg=form_bg_color,fg="#ffffff")
login_button = tkinter.Button(frame, text="Login", bg="#4955e3", fg="#ffffff", font=("Arial", 14),command = lambda:[close_current_window(),MainForm.open_main_window()])

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
frame.pack()

window.mainloop()