s1=int(input("digite o seu salário"))
if(s1>7000  ):
    s2=1.1*s1
else:
    if(s1>5000 ):
        s2=1.2*s1
    else:
        if(s1>2000 ):
            s2=1.4*s1
        else:
            s2=1.5*s1
print("o salário reajustado é ", s2)