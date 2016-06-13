print 'Hello'
def fibo(a,b):
	if a or b:
		return a+b
	else:
		return fibo(a-1,b-1)