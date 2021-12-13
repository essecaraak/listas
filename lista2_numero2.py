x0=int(input("digite o valor x da primeira coordenada"))
y0=int(input("digite o valor y da primeira coordenada"))
x1=int(input("digite o valor x da segunda coordenada"))
y1=int(input("digite o valor y da segunda coordenada"))
if(y0==y1):
    if(x0<0 and x1>0)or(x0==x1):
        x0=x0*-1
        
    if(x0>0 and x1<0):
        x1=x1*-1
    d=( (x1+x0)**2)**1/2
    print(d)
else:
    if(x0==x1):
        if(y0<0 and y1>0):
            y0=y0*-1
        if(y0>0 and y1>0):
            y1=y1*-1
    d=( (y1+y0)**2)**1/2
    print(d)
    else:
        d=((((x1-x0)**2)+((y1-y0)**2))**1/2)
        print(d) 
