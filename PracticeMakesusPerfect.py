P1,P2,P3,P4=map(int,input().split())
target=0
if P1>=10:
    target+=1
if P2>=10:
    target+=1
if P3>=10:
    target+=1
if P4>=10:
    target+=1
print(target)