def medain(a,b,c):
	big = biggest(a,b,c)
	if big == a:
		return bigger (b , c)
	if big == b:
		return bigger (a ,c )
	else:
		return bigger (a ,b)
