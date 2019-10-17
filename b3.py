import tkinter as tk  
from functools import partial  
from tkinter import messagebox
   
   
def bi(n1):  
    num1 = (n1.get())  
    messagebox.showinfo("Title", ("Result =", ((int(num1)*int(num1))*3,1415) ,"cm2" ))  
    return  
   
root = tk.Tk()  
root.title("Calculator of area of circle By yah04")  
intr = tk.StringVar()   

tk.Label(root, text="calculator of circle area By yah04").grid(row=1, column=0)  
tk.Label(root, text="Observation the calculator use just cm (cm2) for calculate ").grid(row=2, column=0)
tk.Label(root, text="raduis").grid(row=3, column=0)  

entryNum1 = tk.Entry(root, textvariable=intr).grid(row=3, column=2)    
bi = partial(bi, intr)  
buttonCal = tk.Button(root, text="Calculate", command=bi).grid(row=4, column=0)  
root.mainloop()  
