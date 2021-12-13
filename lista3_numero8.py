i=0,rpt="s"
while(rpt!="n")and(rpt!="N"):
    c=int(input("escreva um componente do vetor numérico"))
    v1.append(c)
    rpt=input("para passar para o proximo vetor digite n, para continuar aperte qualquer coisa")
rpt="s"
while(rpt!="n")and(rpt!="N"):
    c=int(input("escreva um componente do vetor numérico"))
    v2.append(c)
    rpt=input("para parar digite n, para continuar aperte qualquer coisa")
c1=len(v1)
c2=len(v2)
if(c1!=c2):
    print("vetores de tamanhos diferentes")
else:
    while(c1!=0):
        v3.append((v1[i])+(v2[i]))
        i=i+1
        c1=c1-1
print(v3)
    