import tkinter as tk
window = tk.Tk()
window.geometry("400x300")


window.title('Hello')
window.configure(bg='blue')

box1=tk.Label(window,text="hello\n tkinter!",bg="gray",fg="white",font=("Elephant",16))
box1.pack(ipadx=50,ipady=50,expand=True)


window.mainloop()