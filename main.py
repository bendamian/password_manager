import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import random
#import pyperclip

window = ttk.Window(themename="solar")
window.title("Password Manager")
window.geometry("600x500")
window.config(pady=20, padx=20)


# ------------------- PASSWORD GENERATOR ------------------------------- #
def add_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letters_list + symbols_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_one.set(password)
    #pyperclip.copy(password_one)



# ---------------------------- SAVE PASSWORD ------------------------------- #
log = []


def add_data():
    log.append(E1.get())
    log.append(E2.get())
    log.append(E3.get())
    if len(log[0]) == 0 or len(log[2]) == 0:
        messagebox.showinfo(title="message", message="Please fill all the information")
        log.clear()
    else:
        is_ok = messagebox.askokcancel(title="conformation",
                                       message=f"please conform the website name:{log[0]} and password:{log[2]}  ")

        if is_ok:
            try:
                with open("pass.txt", 'a+') as f:
                    for s in log:
                        f.write(f" {s} |")
                    f.write("\n")
                    E1.delete(0, END)
                    E3.delete(0, END)
                    log.clear()
            except FileNotFoundError:
                text = None
        else:
            messagebox.showinfo(title="Hi", message="Please retry")


# ---------------------------- UI SETUP ------------------------------- #

frame1 = ttk.Frame(window, width=400, style='warning')
frame1.pack()
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=5)
frame1.columnconfigure(2, weight=1)
frame1.columnconfigure(3, weight=1)

frame1.rowconfigure(0, weight=3)
frame1.rowconfigure(1, weight=1)
frame1.rowconfigure(2, weight=2)
frame1.rowconfigure(3, weight=2)
frame1.rowconfigure(4, weight=2)
frame1.rowconfigure(4, weight=2)

canvas = ttk.Canvas(frame1, width=200, height=200)
canvas.grid(row=0, column=1, padx=20, pady=20, sticky='W')
logo = ttk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo, anchor=CENTER)

b1 = ttk.Button(frame1, text="Generate Password", style="info", command=add_password)
b1.grid(row=4, column=2, sticky='W', pady=2, padx=5)
b2 = ttk.Button(frame1, text="Add", width=36, style="info", command=add_data)
b2.grid(row=5, column=1, columnspan=2, sticky='w', pady=10, padx=5)

E1 = ttk.Entry(frame1, width=35, style="light")
E1.grid(row=2, column=1, columnspan=2, sticky='w', pady=5, padx=5)
E1.focus()

E2 = ttk.Entry(frame1, width=35, style="light")
E2.grid(row=3, column=1, columnspan=2, sticky='w', pady=5, padx=5)
E2.insert(0, "xyz@sample.uk")
password_one = ttk.StringVar()
E3 = ttk.Entry(frame1, width=21, style="light", textvariable=password_one)
E3.grid(row=4, column=1, sticky='w', pady=5, padx=5)

label1 = ttk.Label(frame1, text="website")
label1.grid(row=2, column=0, sticky='W', pady=5, padx=5)
label2 = ttk.Label(frame1, text="email/User Name")
label2.grid(row=3, column=0, sticky='W', pady=5, padx=5)
label3 = ttk.Label(frame1, text="Password")
label3.grid(row=4, column=0, sticky='W', pady=5, padx=5)
window.mainloop()
