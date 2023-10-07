n=int(input())
s=n*n
y=0
while s!=0:
    r=s%10
    s=s//10
    y=y+r
if(y==n):
    print("Neon Number")
else:
    print("Not Neon Number")