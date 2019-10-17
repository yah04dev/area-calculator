import tkinter as tk  
from subprocess import Popen
def b1():   
    Popen('python b1.py')
    return  
def b2():   
    Popen('python b3.py')
    return 
def b3():   
    Popen('python b4.py')
    
def b4():   
    Popen('python b2.py')
    
   
root = tk.Tk()  
root.title('Calculator of area')  

tk.Label(root, text="welcome in my  calculator of 2d area By yah04").grid(row=1, column=0)  
tk.Label(root, text="Observation the calculator use just cm (cm2) for calculate ").grid(row=2, column=0)   
tk.Button(root, text="Calculate area of triangle ", command=b1).grid(row=3, column=0)
tk.Button(root, text="Calculate area of circle", command=b2).grid(row=3, column=1)  
tk.Button(root, text="Calculate area of Rectangle", command=b3).grid(row=4, column=0)
tk.Button(root, text="Calculate area of Square", command=b4).grid(row=4, column=1) 
root.mainloop()  
