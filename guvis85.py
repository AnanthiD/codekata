a=str(input())
l=len(a)
m=l//2
if l%2!=0:
    for i in range(0,l):
        if i==m:
            print("*",end="")
        else:
            print(a[i],end="")
else:
    for i in range(0,l):
        if i==m-1 or i==m:
            print("*",end="")
        else:
            print(a[i],end="")