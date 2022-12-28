T=int(input())
for i in range(T):
    L,R=map(int,input().split())
    Count=0
    for j in range(L,R+1):
        if j % 10 in[2,3,9]:
            Count=Count+1
    print(Count)