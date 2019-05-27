try:
    n,k=map(int,input().split())
    z=input().split()
    c=0
    for i in z:
        if int(i)%2!=0:
            c+=1
        if c==k:
            print(i)
            break
except:
    print("Invalid")     