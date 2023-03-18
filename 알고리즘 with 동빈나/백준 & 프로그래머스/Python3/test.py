m=int(input())
n=int(input())
l=[1]*(n+1)
l[1]=0
for i in range(2, int(n**(0.5))+1):
    if l[i]:
        for j in range(i*i, n+1,i):
            l[j]=0

l=[i for i in range(m,n+1) if l[i] == 1]
if sum(l)==0:
    print(-1)
else:    
    print(sum(l))
    print(min(l))