while True:
	n=int(input(">"))
	for i in range(n):
		for j in range(-n+1,n):
			s=abs(j)
			h=n-s
			w=2*(n-abs(j))
			t=i-s

			if i<s:
				print(" "*w, end="")
			else :
				print(" "*(n-1-i)+"/"+"*"*(2*t)+"\\"+" "*(n-1-i), end="")
		print()
	for i in range(2):
		for j in range(-n+1,n):
			w=2*(n-abs(j))
			print("!"*w,end="")
		print()
	print()
