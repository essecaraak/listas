i=0
n=input("escreva o seu nome ")
while(i!="\0"):
    if(i==0 or n[i-1]==" "):
        n[i]=chr(ord(n[i])-32)
        i=i+1
    else:
        i=i+1
print(n)
