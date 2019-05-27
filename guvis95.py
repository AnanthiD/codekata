z=input()
l=''
m=''
for i in range(0,len(z),1):
    if i%2==0:
        l+=z[i]
    if i%2==1:
        m+=z[i]
print(l,m)