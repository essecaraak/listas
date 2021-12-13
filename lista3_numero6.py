t=1
n=int(input("escreva um numero decimal"))
nb=n%2
n=n//2
while(n>=2):
    nb=nb+((n%2)*10^t)
    n=n/2
    t=t+1
nb=nb+((n%2)*10^t)
print(nb)