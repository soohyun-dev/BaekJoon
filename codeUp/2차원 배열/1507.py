check=[[0]*100 for _ in range(100)]

for i in range(4):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            check[i][j]=1
            
sum=0
for i in range(100):
    sum+=check[i].count(1)
print(sum)