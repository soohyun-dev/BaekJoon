L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())
d1=0
d2=0
if(A%C==0):
  d1=A//C
else:
  d1=(A//C)+1
if(B%D==0):
  d2=B//D
else:
  d2=(B//D)+1
print(L-(max(d1,d2)))