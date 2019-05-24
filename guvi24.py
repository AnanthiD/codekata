start,end=input().split()
start=int(start)
end=int(end)
for num1 in range(start,(end+1)):
    s=0
    temp=num1
    while(temp>0):
        rev=temp%10
        s=s+(rev**3)
        temp=temp//10
    if(num1==end):
        break
    elif(num1==s):
        print(num1,end=' ')