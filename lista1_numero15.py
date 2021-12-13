n1=int(input("digite um numero"))
n2=int(input("digite outro numero"))
if(n1>n2):
    maior=n1
    menor=n2
else:
    maior=n2
    menor=n1
while(menor!=(maior-1)):
    print(menor+1)
    menor=menor+1