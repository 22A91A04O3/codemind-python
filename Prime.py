n=int(input())
for i in range(2,n):
    if (n % i !=0):
        print("Prime")
        break
    else:
        print("Not Prime")
        break