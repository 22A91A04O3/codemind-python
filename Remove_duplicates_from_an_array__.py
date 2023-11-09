n=int(input())
s=set(map(int,input().split()))
l=list(set(s))
for i in range(len(l)):
    print(l[i],end=' ')