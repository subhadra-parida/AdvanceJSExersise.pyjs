# array=[21,12,34,5,7,1,23]
# N=7
# def rec(array,N):
#     for i in range(0,N-1):
#         if array[i]>array[i+1]:
#             array[i],array[i+1]=array[i+1],array[i]
#     if N>0:
#         rec(array,N-1)
# rec(array,N)
# print(array)
# Recursion.......
def selection(array,result):
    if array2==0:
        return ""
    else:
        j=array.index(min(array))
        array[0],array[j]=array[j],array[0]
        result.append(array[0])
        return selection(array[1:],result)
array=[5,2,4,3,1]
array2=5
result=[]
selection(array,result)
print(result)

