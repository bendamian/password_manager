import ttkbootstrap as ttk
from ttkbootstrap.constants import *

window = ttk.Window(themename="solar")
window.title("Password Manager")
window.geometry("600x500")

# ------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

frame1 = ttk.Frame(window, style='warning')
frame1.pack()
frame1.columnconfigure(0, weight=3)
frame1.columnconfigure(1, weight=1)

frame1.rowconfigure(0, weight=3)
frame1.rowconfigure(1, weight=1)
frame1.rowconfigure(2, weight=2)

canvas = ttk.Canvas(frame1, width=200, height=200)
canvas.grid(row=0, column=0, padx=20, pady=20, sticky='E')
logo = ttk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo, anchor=CENTER)

b1 = ttk.Button(frame1, text="Submit", style="light")
b1.grid(row=2, column=1, sticky='e', pady=5, padx=5)

E1 = ttk.Entry(frame1, style="light", )
E1.grid(row=2, column=0, sticky='w', pady=5, padx=5)

window.mainloop()
