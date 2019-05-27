z=input()
i=0
print(z[i].upper(),end="")
i=1
while i <len(z):
    if z[i]==" ":
        print(z[i],end="")
        i=i+1
        print(z[i].upper(),end="")
        i=i+1
    else:
        print(z[i],end="")
        i=i+1