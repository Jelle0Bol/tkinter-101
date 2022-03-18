from tkinter import *
import time

root = Tk()
root.title("Digitale Klok")
root.geometry("500x100")

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    my_label.config(text=hour + ":" + minute + ":" + second)
    my_label.after(1000, clock)

def update():
    my_label.config(text="New Text")

my_label = Label(root, text="",font=("Helvetica",48), fg="black", bg="white")
my_label.pack(pady=20)

clock()

#my_label.after(5000, update)

root.mainloop()