soma=0,v=0
while(v>=0):
    v=int(input("escreva quantos números quiser e digite um negativo para ver a soma"))
    if(v<0):
        break
    else:
        soma=soma+v
print(soma)

