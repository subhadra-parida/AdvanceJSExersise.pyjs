arr=[1,2,3,4,5]
n=4
k=3
s_arr=[]
for i in range(0,n):
    for j in range(i,n):
        s_arr.append(arr[i:j+1])
modifid_arr=[]
max_len=0
for i in s_arr:
    if (sum(i)%k!=0):
        modifid_arr.append(i)
        if len(i)>max_len:
            max_len=len(i)
            count=0
        if len(i)==max_len:
            count=count+1
print(s_arr)
print(modifid_arr)
print(count)
