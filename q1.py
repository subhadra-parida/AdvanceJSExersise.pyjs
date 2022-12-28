arr=[1,10,3,2,7,4]
N=6
def rec(arr,N):
    for i in range(0,N-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    if N>0:
        rec(arr,N-1)
rec(arr,N)
print(arr)
