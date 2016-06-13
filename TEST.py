print 'Hello'
def fibo(a,b):
	if a==0 or b==0:
		print a,b
		return a+b
	else:
		return fibo(a-1,b-1)

print 'As you wish, second version'


d=fibo(5,10)

print d