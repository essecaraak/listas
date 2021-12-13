vet=[0]*100
i=0
total=0
n=0
while(n>=0):
    n=int(input("escevra números de 1 a 100, para ver a frequência digite um negativo"))
    if(n<0):
       break
    else:
        if(n>=1) and (n<=100):
            vet[n]=vet[n]+1
            total=total+1
            
while(i<=99):
    if(vet[i]>0):
        freq=(vet[i]*100)/total
        print("o numero ",i+1," teve uma frequência de ",freq,"%")
        i=i+1
    else:
        i=i+1
