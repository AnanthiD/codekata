k=str(input())
s=0
for i in range(0,len(k)):
    if(k[i]!='0')and(k[i]!='1'):
        s+=1
if(s>0):
    print("no")
else:
    print("yes")