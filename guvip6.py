v,m=map(str,input().split())
if(len(v)!=len(m)):
    print("no")
else:
    s1=[vr.count(i) for i in v]
    s2=[my.count(i) for i in m]
if(s1==s2):
    print("yes")
else:
    print("no")