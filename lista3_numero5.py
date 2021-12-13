cad=input("digite a cadeia de caracteres")
s=int(input("digite o valor do salto"))
i=0
while(cad[i]!="\0"):
    cadascii=ord(cad[i])
    if(cadascii==32):
        i=i+1
        continue
    else:
        if((cadascii>=65) and (cadascii<=90) ):
            cadascii=cadascii+32
    if((cadascii+s)>122 ):
        cad[i]= chr(((cadascii+s)%26)+96)
        i=i+1
    else:
        cad[i]=chr(cadascii+s)
        i=i+1
print(cad)