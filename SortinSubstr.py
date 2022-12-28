T=int(input())
for i in range(T):
    N=int(input())
    S=input()
    Count=0
    for i in range(1,N):
        if S[i]=="0" and S[i-1]=="1":
            Count=Count+1
    print(Count)
    

    
    