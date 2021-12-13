i=0,cont=-1,nd=0
n=(input("digite um numero em binário"))
while(n[i]!="\0" ):
    cont=cont+1
    i=i+1
i=0
while(n[i]!="\0" ):
    nd=nd + (int(n))*2^cont)
    cont=cont+1
    i=i+1
print(nd)