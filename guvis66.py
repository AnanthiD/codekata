a=list(map(str,input()))
d=0
c=0
for j in range(0,len(a)):
    if a[j].isdigit()==True:
        d=d+1
    elif a[j].isalpha()==True:
        c=c+1
if c>0 and d>0:
    print("Yes")
else: print("No")