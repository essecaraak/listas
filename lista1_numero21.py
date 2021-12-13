rpt="s"
while((rpt=="s") or (rpt=="S")) and ((rpt!="n") or (rpt!="N")):
    n1=int(input("digite sua primeira nota"))
    n2=int(input("digite sua segunda nota"))
    n3=int(input("digite sua terceira nota"))
    n4=int(input("digite sua quarta nota"))
    nome=input("escreva seu nome")
    m=(n1+n2+n3+n4)/4
    if(m>6):
        print(nome,"você foi aprovado e sua media é ",m)
    else:
        print(nome,"você foi reprovado e sua media é ",m)
    rpt=input("quer repetir o processo S/N")