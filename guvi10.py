num=int(input())

if(num>1):

    for i in range(2,num):
        
	if((num%i)==0):
            
		print(num,"its is not a prime number")
            
		break

    else:
        
	print(num, "num is a prime number")

else:
    
	print("is not a prime number")
            