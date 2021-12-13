n1=int(input("escreva um numero"))
n2=int(input("escreva outro numero"))
print("a soma é ",(n1+n2))
print("a multiplicação é ",(n1*n2))
if(n1>n2):
    menor=n2
    maior=n1
else:
    menor=n1
    maior=n2
print("a subtração é",(maior-menor))
if(menor=0):
    print("divisão impossivel")
else:
    print("a divisão é",(maior/menor))