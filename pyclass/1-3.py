while True:
	n=int( input(">"))
	for i in range(n):
		if i<=n-1:
			for a in range(n):
				print(" "*((n-(i+1)))*n,end=" ")
				for j in range(i+1):					
					print(" "*(n-1-a)+str(a+1)*(2*a+1)+" "*(n-1-a) , end=" " )
			print()
		else:
			for j in range (n):
				print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j) , end=" " )
			print()
	print()
		
