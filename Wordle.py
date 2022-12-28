t=int(input())
for i in range(t):
    S=input()
    T=input()
    M=str()
    for i in range(len(S)):
        S.upper()
        T.upper()
        if S[i]==T[i]:
            M=M+'G'
        else:
            M=M+'B'
    print(M)