def printMat(mat,n):
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()
def isSafe(mat,row,col):
    # check same column
    for i in range(0,row):
        if mat[i][col]==1:
            return False
    #check right upper diagonal
    for i,j in zip(range(row-1,-1,-1), range(col+1,n)):
        if mat[i][j]==1:
            return False
    #check left upper digonal
    for i,j in zip(range(row-1,-1,-1), range(col-1,-1,-1)):
        if mat[i][j]==1:
            return False
    return True
def n_queen(mat,row,n):
    global count
    if row==n:
        count+=1
        print("Solution", count)
        printMat(mat,n)
        return
    for i in range(n):
        if(isSafe(mat,row,i)==True):
            mat[row][i]=1
            n_queen(mat,row+1,n)
            mat[row][i]=0

n=int(input("Enter no of queens:"))
mat=[[0]*n for _ in range(n)]
#mat[0][0]=1
row=int(input("Enter row no. to place:"))
col=int(input("Enter column no. to place:"))
mat[row][col]='Q1'
count=0
n_queen(mat,1,n)
if count==0:
    print("No solution for n=",n)
else:
    print("total sultions :", count)