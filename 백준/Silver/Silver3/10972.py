import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
l_check=sorted(l, reverse=True)

if l==l_check:
    print(-1)
else:    
    for i in range(N-2,-1,-1):
        cut=l[i:]
        cut_check=sorted(cut, reverse=True)
        if cut!= cut_check:
            tmp=l[i]
            front=l[:i]
            back=sorted(cut)
            num=back.index(tmp)
            center=back[num+1]
            back.remove(center)
            print(*(front+[center]+back))
            break



