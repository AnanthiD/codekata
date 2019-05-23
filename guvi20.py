s,e=input().split()
l=int(s)
u=int(e)
for i in range(l+1,u):
    if(i%2==0):
        print(i, end=" ")