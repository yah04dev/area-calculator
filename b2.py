import tkinter as tk  
from functools import partial  
from tkinter import messagebox
   
   
def bi(how, n1):  
    num1 = (n1.get())  
    messagebox.showinfo("Title", ("Result =", (int(num1)*int(num1)) ,"cm2" ))  
    return  
   
root = tk.Tk()  
root.title('Calculator of square area By yah04 ')  
intr = tk.StringVar()   

tk.Label(root, text="calculator of Square area By yah04").grid(row=1, column=0)  
tk.Label(root, text="Observation the calculator use just cm (cm2) for calculate ").grid(row=2, column=0)
tk.Label(root, text="lenght or width").grid(row=3, column=0)   
entryNum1 = tk.Entry(root, textvariable=intr).grid(row=3, column=1)    
bi = partial(bi, how, intr)  
buttonCal = tk.Button(root, text="Calculate", command=bi).grid(row=4, column=0)  
root.mainloop()  
