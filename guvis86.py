s=int(input())
m=0
for i in range(2,s):
    if s%i==0:
        m=1
if(m==0):
    print("no")
else:
    print("yes")