n=int(input("digite um numero natural para ver o fatorial "))
if(n<2):
	print(n)
else:
	f=n
	while(n>=2):
		f=f*(n-1)
		n=n-1
print(f)
