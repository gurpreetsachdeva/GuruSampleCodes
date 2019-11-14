def fibonacci(n):
	if n<=1:
		return n
	elif n<0:
		return -10000
	else:
		return fibonacci(n-1)+fibonacci(n-2)
