def search(array):
    if array[0]=="Ritu":
        return ""
    else:
        result.append(array[0])
        return search(array[1:],result)
array=["Subha","Barsha","Ritu","Rinu","Lisha"]
# result=[]
print(search(array,result))
print(result)












# array=["A","B","C","D","E","F"]
# i=0
# while i <len(array):
#     if array[i]=="D":
#         print(array[i],array[1:"D"])
#     i=i+1








    
# def recursion_print(n):
#     if n==0:
#       print(n)
#     else:
#       recursion_print(n-1)
#       print(n)


# recursion_print(9)