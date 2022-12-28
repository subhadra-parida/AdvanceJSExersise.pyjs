def subarray(array,start,end):
    if len(array)==end:
        return 
    elif start>end:
        return subarray(array,0,end+1)
    else:
        print(array[start:end+1])
        return subarray(array,start+1,end)
array=[1,2,3,4,5]
sublist=[]
subarray(array,0,0)





