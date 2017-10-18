import pandas as pd
import numpy as np
import os

q=[]
q.append([1,2,3])
q.append([4,5,6])
#q = np.array([[1,2,3],[4,5,6]])
q = np.array(q)
print(q.shape)
data = pd.DataFrame(q, columns=['a','b','c'])
print(data)
a = 1
b =2
print(str(a)+str(b))

a = 2
b = 1

def switch(a,b):
    if (a>b):
        t = a
        a=b
        b=a
    return True, False

print(switch(a,b))

if a > 0:
    m = 3

print(m)

import tkinter as tk

current_dir = os.getcwd()
top = tk.Tk()
photo = tk.PhotoImage(file=current_dir + r'\resource\picture\delta_l.png')
label = tk.Label(top, image=photo)
label.pack()
tk.mainloop()