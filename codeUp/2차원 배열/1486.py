n,m=map(int,input().split())

check=[[0]*m for _ in range(n)]
check[0][m-1]=1
cnt=1
x=0
y=m-1
while True:
    if cnt>n*m:
        break
    if y+1>=m or check[x][y+1]!=0: # 오른쪽
        while True: # 밑으로 내리기
            cnt+=1
            x+=1
            if x+1>=n or cnt>n*m:
                break
            if check[x+1][y]!=0:
                break
            check[x][y]=cnt
        if cnt<=n*m:
            check[x][y]=cnt
    if x+1>=n or check[x+1][y]!=0: # 아래
        while True: # 왼쪽으로
            cnt+=1
            y-=1
            if y-1<0 or cnt>n*m:
                break
            if check[x][y-1]!=0:
                break
            check[x][y]=cnt
        if cnt<=n*m:
            check[x][y]=cnt
    if y-1<0 or check[x][y-1]!=0: # 왼쪽
        while True: # 위로 올리기
            cnt+=1
            x-=1
            if x-1<0 or cnt>n*m:
                break
            if check[x-1][y]!=0:
                break
            check[x][y]=cnt
        if cnt<=n*m:
            check[x][y]=cnt
    if x-1<0 or check[x-1][y]!=0: # 위
        while True: #오른쪽으로 돌리기
            cnt+=1
            y+=1  
            if y+1>=m or cnt>n*m:
                break
            if check[x][y+1]!=0:
                break
            check[x][y]=cnt
        if cnt<=n*m:
            check[x][y]=cnt
                    
for i in range(n):
    print(*check[i], end=' ')
    print()