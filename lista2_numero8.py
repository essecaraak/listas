h=float(input("digite sua altura"))
s=input("digite seu sexo sendo f para feminino e m para masculino")
if(s=="f") or (s=="F"):
    p=(62.1*h)-44.7
else:
    p=(72.7*h)-58
print("seu peso ideal é ",p)
