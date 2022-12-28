T = int(input())
for i in range(T):
    A,B = map(int, input().split())
    Result=str(A+B)
    Count = 0
    for i in Result:
        if i == '0':
            Count=Count+6
        elif i == '1':
            Count=Count+2
        elif i == '2':
            Count=Count+5
        elif i == '3':
            Count=Count+5
        elif i == '4':
            Count=Count+4
        elif i == '5':
            Count=Count+5
        elif i == '6':
            count=Count+6
        elif i == '7':
            Count=Count+3
        elif i == '8':
            Count=Count+7
        elif i == '9':
            Count=Count+6
    print(Count)
    