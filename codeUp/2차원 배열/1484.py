n,m=map(int,input().split())
check=[[0]*m for _ in range(n)]
cnt=0
x=0
y=0
X=n
Y=m

while True:
    while y<Y-1:
        if cnt>=(n*m):
            break
        else:
            cnt+=1
        check[x][y]=cnt
        y+=1
    Y=x
    while x<X-1:
        if cnt>=(n*m):
            break
        else:
            cnt+=1
        check[x][y]=cnt
        x+=1
    while y>Y:
        if cnt>=(n*m):
            break
        else:
            cnt+=1
        check[x][y]=cnt
        y-=1
    X=y
    while x>X:  
        if cnt>=(n*m):
            break
        else:
            cnt+=1
        check[x][y]=cnt
        x-=1
    x+=1
    y+=1
    X=n-x
    Y=m-y

    if x==y and X==Y and X-x==1:
        check[x][y]=cnt+1
        break
    if cnt>=(n*m):
            break

for i in range(n):
    print(*check[i],end=' ')
    print()
