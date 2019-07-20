w=int(input())
x1=list(map(int,input().split()))
y1=0
for i in range(w):
  for j in range(i,w):
      for k in range(j,w):
          if(x1[i]<x1[j]<x1[k]):
            y1+=1
print(y1)

