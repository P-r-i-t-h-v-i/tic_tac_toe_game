import tkinter as tk
import numpy as np
from tkinter import messagebox
num = 0
c = np.zeros((3,3))
def win(a) :
    global c
    for x in (1, -1):
        mask = (c == x)
        if mask.all(1).any() or mask.all(0).any() or np.diag(mask).all() or np.diag(mask[:, ::-1]).all():
            messagebox.askokcancel("results",a+' won')
            root.destroy()
    return False
def on_click(btn,b,d):
    global num
    print("clicked ",b+1,d+1)
    if int(num)%2 == 0:
        c[b][d] = 1       
        btn.config(text='X',font=("Consolas",20),fg="black",disabledforeground="black")
        win('X')
    else :
        c[b][d] = -1
        btn.config(text='O',font=("Consolas",20),fg="black",disabledforeground="black")
        win('O')
    btn.config(state=tk.DISABLED)
    num +=1
 
root = tk.Tk()
root.title("Tic tac toe")
root.geometry("460x580")
root.configure(bg='black')
buttons = []
for i in range(3):
    a = []
    for j in range(3):
        btn = tk.Button(root, command=lambda b=i,d=j: on_click(buttons[b][d],b,d),width=9,height=5,font=("Consolas",20),relief="flat")
        btn.grid(row=i, column=j, padx=5, pady=5)
        a.append(btn)
    buttons.append(a)
root.mainloop()