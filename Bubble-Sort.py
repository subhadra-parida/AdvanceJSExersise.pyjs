# a=[5,4,2,1,3]
# b=a.sort()
# print(b)
# a=[5,4,2,1,3]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

array=[21,12,34,5,7,1,23]
N=7
def rec(array,N):
    for i in range(0,N-1):
        if array[i]>array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
    if N>0:
        rec(array,N-1)
rec(array,N)
print(array)

# In recursion...................
# a=[21,12,34,5,7,1,23]
# N=len(a)
# def rec(a,N):
#     if N==0:
#         return
#     else:
#         for i in range(0,N-1):
#             if a[i]>a[i+1]:
#                 a[i],a[i+1]=a[i+1],a[i]
#     return rec(a,N-1)
# rec(a,N)
# print(a)


