import pandas as pd
import numpy as np

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

print(a,'',b)