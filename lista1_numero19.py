v=0,menor=0,maior=0
while(v>=0):
    v=int(input("escreva quantos números quiser e digite um negativo para ver o maior e o menor"))
    
    if(v<0):
        break
    else:
        if(v>maior):
            maior=v
        else:
            if(v<menor):
                menor=v
print("o maior é" ,maior," e o menor é ",menor)
            