def sum(array):
    if len(array)==0:
        return 0
    else:
        return array[0]+sum(array[1:len(array)])
    # print(array)
array=[1,2,3,4,5]
print(sum(array))

