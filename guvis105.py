p,t,r=map(float,input().split())

s=r/100

x=p*(1+(t*s))

z=abs(p-x)

print(int(z))
