b,c=map(int,input().split())
m=list(map(int,input().split()))
a=0
for i in range(0,len(m)):
    if(m[i]==c):
        a+=1
print(a)