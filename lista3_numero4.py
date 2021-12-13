kmt=0,gt=0,km=0
while(km>=0):
    km=int(input("digite a quilometragem percorrida, para parar o programa digite um valor negativo"))
    g=int(input("digite a gasolina abastecida"))
    if(km==0):
        break
    else:
        kmt=kmt+km
        gt=gt+g
        m=kmt/gt
        print("contagem numero ",i,": até agora você fez ",m," km por litro de gasolina")
        i=i+1