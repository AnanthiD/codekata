a,d,n=map(int,input().split())
z=0
i=0
while n>i:
    z=z+a
    a=d+a
    i=i+1
print(z)