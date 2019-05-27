z=int(input())
v=0
b = 1
c= 1
count = 0
if(z==1):
    print("1")
else:
    if z<= 0:
        v=0
    elif z == 1:
        v=0
    else:
        while count < z:
            print(b,end=" ")
            nth = b + c
            b= c
            c = nth
            count += 1