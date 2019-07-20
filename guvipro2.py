from itertools import combinations
Si,U=map(int,input().split())
L=len(str(Si))
Lst=list(combinations(str(Si),L-U))
Lst=sorted(Lst)
print(*Lst[0],sep='')