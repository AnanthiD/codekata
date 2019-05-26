k=int(input())
l=0
for i in range(2,k//2+1):
    if(k%i==0):
        l=1
if(l==0):
    print("yes")
else:
    print("no")