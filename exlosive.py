import tkinter as tk
window = tk.Tk()
window.geometry("50x50")
window.title('My First Window')
window.configure(bg='white')

print("6")

def change_size_1():
    print("5")
    window.geometry("100x100")
    window.configure(bg='yellow')

def change_size_2():
    print("4")
    window.geometry("150x150")
    window.configure(bg='orange')

def change_size_3():
    print("3")
    window.geometry("200x200")
    window.configure(bg='red')

def change_size_4():
    print("2")
    window.geometry("250x250")
    window.configure(bg='purple')

def change_size_5():
    print("1")
    window.geometry("300x300")
    window.configure(bg='black')

def text_1():
    print("BOOM!!")
    window.destroy()

window.after(2000, change_size_1)
window.after(4000, change_size_2)
window.after(6000, change_size_3)
window.after(8000, change_size_4)
window.after(10000, change_size_5)
window.after(12000, text_1)

window.mainloop()