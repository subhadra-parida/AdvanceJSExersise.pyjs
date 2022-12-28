T=int(input())
for i in range(T):
    N=int(input())
    List=list(map(str,input().split()))
    C_START38=0
    C_LTIME108=0
    for i in List:
        if i=="START38":
            C_START38+=1
        else:
            C_LTIME108+=1
    print(C_START38,C_LTIME108)
    
    