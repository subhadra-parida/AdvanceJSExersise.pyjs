def mergeSort(array):
    if len(array)>1:
        middle=len(array)//2
        left=array[:middle]
        right=array[middle:]
        mergeSort(left)
        mergeSort(right)
        leftIndex=0
        rightIndex=0
        position=0
        while leftIndex<len(left) and rightIndex<len(right):
            if left[leftIndex]<right[rightIndex]:
                array[position]=left[leftIndex]
                leftIndex=leftIndex+1
            else:
                array[position]=right[rightIndex]
                rightIndex=rightIndex+1
            position=position+1
        while leftIndex<len(left):
            array[position]=left[leftIndex]
            position=position+1
            leftIndex=leftIndex+1
        while rightIndex<len(right):
            array[position]=right[rightIndex]
            position=position+1
            rightIndex=rightIndex+1
array=[12,4,3,5,1,8,18,2]
mergeSort(array)
print(array)

