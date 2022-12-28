from operator import ne
from tkinter import N


i=0
new=[1]
while i<=100:
    square=new[-1]+3+2*i
    new.append(square)
    i=i+1
print(new)
    
    