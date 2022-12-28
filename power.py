# # Take a number and check it is a Number of power or not.............


# Number=int(input("enter a number="))
# for i in range(1,4):
#     if (2**Number)>16:
#         print("NO")
#         break
#     if (2**Number)==16:
#         print("YES")
#         break  
    
    
arr=[2]
while arr[-1]<16:
    if arr[-1]==16:
        print("Yes")
        break
    else:
        arr.append(2*arr[-1])
print(arr)
    