
rpt="s"
while(((rpt==”s”)or(rpt==”S” )) and ((rpt!=”n” ) or (rpt!=”N” )) ):
    a=int(input("digite o valor do coeficiente a"))
    b=int(input("digite o valor do coeficiente b"))
    c=int(input("digite o valor do coeficiente c"))
    d=(b**2)-(4*a*c)
    if(d<0):
        print("não há raízes reais")
    else:
        if(d==0):
            print("não há raízes reais")
        else:
            if(d==0):
            x1=-b/(2*a)
            print("a raiz da equação é ",x1)
            else:
                x1=(-b+(d**(1/2))/(2*a)  
                x2=(-b-(d**(1/2))/(2*a)  
            print("as raízes da equação são", x1, "e", x2)
    rpt=input("quer repetir o processo S/N")
    
    