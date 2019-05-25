k=int(input())
x=0
y=0
while(k>0):
    x=k%10
    y=y+x
    k=k//10
print(y)