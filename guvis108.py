o=int(input())
n=list(map(int,input().split()))
z=sorted(n)
for i in range(0,len(n)):
    if z[i]!=n[i]:
        print(i)
        break