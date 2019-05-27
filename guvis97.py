n,m=map(int,input().split())
s=0
x=max(n,m)
for i in range(1,x+1):
    if n%i==0 and m%i==0:
        s=i
print(s)
