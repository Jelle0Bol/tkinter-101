import tkinter as tk
from tkinter import * 
import random

window = tk.Tk()
window.geometry("800x400")
window.title('My First Window')
window.configure(bg='white')
T = Text(window, height = 5, width = 52)

this_list_1 = ["PlayStation 5","Appel","Oplader","Samsung A50","TV","Airpods","Tandenborstel","Flesje water","Horloge","Zonnebril","Jas"]


def button_pressed_1():
    getal = 10
    if (len(this_list_1)) >= 1:
        T.delete(1.0,END)
        random_word_1 = random.choice(this_list_1)
        T.insert(tk.END, "Je hebt een " + random_word_1 +" gegrabbelt\n")
        T.insert(tk.END, "Je hebt nog " + str(len(this_list_1)) + " grabbels te gaan")
        this_list_1.remove(random_word_1)
    else:
        T.delete(1.0,END)
        T.insert(tk.END, ("Er zit niks meer in de grabbelton"))


button_1 = Button(window,text = "Grabbel", command=button_pressed_1)
button_1.config(height=10,width=40)


button_1.pack()
T.pack()







window.mainloop()