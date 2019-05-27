try:
	n=int(input())
	if(n%2==0):
		print(n//2)
	else:
		print(n)
except ValueError:
	print("invalid")