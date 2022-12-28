# def fibbonacci(N):
#     a=0
#     b=1
#     c=a+b
#     while c<=N:
#         print(c)
#         a=b
#         b=c
#         c=a+b
# fibbonacci(5)

def fibbonacci(N):
    if N==0:
        return 0
    if N==1:
        return 1
    else:
        return(fibbonacci(N-1)+fibbonacci(N-2))
# for i in range(1,10):
#     print(fibbonacci(i))
print(fibbonacci(10))

