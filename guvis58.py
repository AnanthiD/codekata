try:
	n=int(input())
	ar=list(map(int,input().split()))
	s=0
	for i in range(0,n):
		s=s+ar[i]
	print(s//n)
except ValueError:
	print("invalid")
