a=int(input())
x=a//3600
y=(a%3600)//60
z=a%60
print(f"H:M:S-{x}:{y}:{z}")