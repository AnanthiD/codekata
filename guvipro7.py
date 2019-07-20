x1=int(input())
z=0
for i in range(0,x1):
  if(pow(2,i)>x1):
    break
  z=x1-pow(2,i)
print(z)
