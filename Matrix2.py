n=3
arr=[[1,2,3],[4,5,6],[7,8,9]]
result=[]
top=0
side=0
rows=n
columns=n
while side<columns and top<rows:
    for i in range(side,columns):
        result.append(arr[rows-1][i])
    rows=rows-1
    for i in range(rows-1,top-1,-1):
        result.append(arr[i][rows])
    columns=columns-1
    for i in range(columns-1,side-1,-1):
        result.append(arr[top][i])
    top=top+1
    for i in range(top,rows):
        result.append(arr[i][side])
    side=side+1
print(*result,sep=" ") 