arr=[1,2,3,4,5,6]
n=6
max_len=0
obj={}
for i in range(1,n+1):
    obj[str(i)]=[]
print(obj)
for i in range(0,n):
    for j in range(i,n):
        a=arr[i:j+1]
        obj[str(len(a))].append(a)
print(obj)







# for i in range(1,2**n):                                                                           
#     a=str(bin(i)[2:])[::1]
#     print(a)
#     sub_arry=[]
#     for i in range(0,len(a)):
#         if a[i]=="1":
#             sub_arry.append(int(arr[i]))
#     result.append(sub_arry)
# print(result)
