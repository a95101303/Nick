while True:
	n=int( input(">"))
	for i in range(n):
		if i<n-1:
			for j in range(n):
				for m in range(2):	
					print(" "*n,end="") if (m==0 and i<n-1) else()
					print(" "*n*(n-2-i),end=".")
					for k in range(i+1):
						print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j) , end=" ")
					print(" "*n*(n-2-i), end="")
				print()
				#print(" "*((n-(i+1)))*1, end="/")
		else:
			for j in range(n):
				print((" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j)+" ")*(2*n-1))			
			
	print()
