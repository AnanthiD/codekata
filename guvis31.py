n,a,d=input().split()
n=int(n)
a=int(a)
d=int(d)
s=0
for i in range(n):
    r=(i*d)+a
    s=s+r
print (s)