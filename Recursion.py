def recursion(a):
    if a==1:
        return 1
    else:
        return a*recursion(a-1)
print(recursion(5))