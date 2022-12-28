list=[2,2,2,2,1,4,3]
n=len(list)
Count1=0
index=-1
for i in range(n):
    count2=0
    for j in range(n):
        if(list[i] == list[j]):
                count2=count2+1
        if(count2>Count1):
            Count1=count2
            index=i
if (Count1>n//2):
    print(list[index]) 
else:
    print(-1)
    
    
    
    
    
    
    
    