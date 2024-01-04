from random import sample

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

window = ttk.Window(themename="solar")
window.title("Password Manager")
window.geometry("600x500")
window.config(pady=20, padx=20)

# ------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
log = []


def add_data():
    log.append(E1.get())
    log.append(E2.get())
    log.append(E3.get())
    try:
        with open("pass.txt", 'a+') as f:

            pass_w = f.read()
            for s in log:
                f.write(s)
                f.write(" | ")
            f.write("\n")
    except FileNotFoundError:
        text = None

    log.clear()
    E1.delete(0, END)
    E3.delete(0, END)


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

b1 = ttk.Button(frame1, text="Generate Password", style="info")
b1.grid(row=4, column=2, sticky='W', pady=2, padx=5)
b2 = ttk.Button(frame1, text="Add", width=36, style="info", command=add_data)
b2.grid(row=5, column=1, columnspan=2, sticky='w', pady=10, padx=5)

E1 = ttk.Entry(frame1, width=35, style="light")
E1.grid(row=2, column=1, columnspan=2, sticky='w', pady=5, padx=5)
E1.focus()

E2 = ttk.Entry(frame1, width=35, style="light")
E2.grid(row=3, column=1, columnspan=2, sticky='w', pady=5, padx=5)
E2.insert(0, "xyz@sample.uk")

E3 = ttk.Entry(frame1, width=21, style="light")
E3.grid(row=4, column=1, sticky='w', pady=5, padx=5)

label1 = ttk.Label(frame1, text="website")
label1.grid(row=2, column=0, sticky='W', pady=5, padx=5)
label2 = ttk.Label(frame1, text="email/User Name")
label2.grid(row=3, column=0, sticky='W', pady=5, padx=5)
label3 = ttk.Label(frame1, text="Password")
label3.grid(row=4, column=0, sticky='W', pady=5, padx=5)
window.mainloop()
