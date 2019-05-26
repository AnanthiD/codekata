k=input().split()
l=len(k)
min=k[0]
for i in range(1,l):
    if(min>k[i]):
        min=k[i]
print(min)