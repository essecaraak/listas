p1=0,p2=0,p3=0,p4=0,soma=0,cod=1
while(cod>0):
    cod=int(input("digite um dos códigos para pedir, se digite um numero negativo para ver a conta total"))
    if(cod<0):
        break
    else:
        if(cod==100 ):
            soma =soma+4.5
            p1=p1+1
        else:
            if(cod==101 ):
                soma =soma+5
                p2=p2+1
            else:
                if(cod==102):
                    soma =soma+2
                    p3=p3+1
                else:
                    if(cod==103):
                       soma =soma+6
                       p4=p4+1
                    else:
                        print("codigo inválido")
print("sua compra foi de ",p1," mistos quentes, ",p2," refrigerantes, ",p3," pães de queijo e ",p4," sucos,  somando um total de",soma)