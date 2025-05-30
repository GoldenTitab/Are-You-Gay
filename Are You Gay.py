import tkinter as tk
import random


def say_yes():
    result_label.config(text="You MF faggot!")


def say_no(event):
    new_x = random.randint(0, window.winfo_width() - button2.winfo_width())
    new_y = random.randint(0, window.winfo_height() - button2.winfo_height())
    button2.place(x=new_x, y=new_y)


window = tk.Tk()
window.title("WAYG")
window.geometry("400x300")

question = tk.Label(window, text="Are You Gay?")
question.pack()

button1 = tk.Button(window, text="Yes", command=say_yes)
button1.pack(side='left', padx=10, pady=10)

button2 = tk.Button(window, text="No")
button2.place(x=200, y=150)
button2.bind("<Enter>", say_no)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
