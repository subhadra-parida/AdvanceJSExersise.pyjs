a=[39,27,11,4,24,32,32,1]
b=[]
i=0
while i<len(a):
    if a[i]<a[i-1]:
        b.append(-1)
    elif a[i]==a[i-1]:
        b.append(a[i-1-1])
    else:
        b.append(a[i-1])
    i=i+1
print(b)



# # Using stack.......

# array=[31,19,21,2,9,3,1,7,10]
# array2=[]
# i=0
# while i<len(array):