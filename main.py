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
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)

frame1.rowconfigure(0, weight=3)
frame1.rowconfigure(1, weight=1)

b1 = ttk.Button(frame1, text="Submit", style="light")
b1.grid(row=1, column=1, sticky='w', pady=5, padx=5)

E1 = ttk.Entry(frame1, style="light", )
E1.grid(row=1, column=0, sticky='e', pady=5, padx=5)

window.mainloop()
