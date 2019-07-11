d=input()
d=list(d)
res=""
for i in range(0,len(d)-1,2):
    temp=d[i+1]
    d[i+1]=d[i]
    d[i]=temp
print(res.join(d))