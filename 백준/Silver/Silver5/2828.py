import sys
input=sys.stdin.readline

N,M=map(int,input().split())
J=int(input())
cnt=0
start=1
end=M
for i in range(J):
    down=int(input())
    if down>end:
        cnt+=(down-end)
        end=down
        start=end-M+1
    elif down<start:
        cnt+=(start-down)
        start=down
        end=down+M-1
print(cnt)