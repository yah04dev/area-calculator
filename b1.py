import tkinter as tk  
from functools import partial  
from tkinter import messagebox
   
   
def bi( n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    messagebox.showinfo("Title", ("Result =", (int(num1)*int(num2))/2 ,"cm2" ))  
    return  
   
root = tk.Tk()  
root.title('Calculator of triangle area')  
leng = tk.StringVar()  
wid = tk.StringVar()  

tk.Label(root, text="calculator of triangle area By yah04").grid(row=1, column=0)  
tk.Label(root, text="Observation the calculator use just cm (cm2) for calculate ").grid(row=2, column=0)   
tk.Label(root, text="lenght").grid(row=3, column=0)  
tk.Label(root, text="width").grid(row=4, column=0)    
entryNum1 = tk.Entry(root, textvariable=leng).grid(row=3, column=1)  
entryNum2 = tk.Entry(root, textvariable=wid).grid(row=4, column=1)  
bi = partial(bi, leng, wid)  
buttonCal = tk.Button(root, text="Calculate", command=bi).grid(row=5, column=0)  
root.mainloop()  
