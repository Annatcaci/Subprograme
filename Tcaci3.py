print("Avem fractii de forma: a/b,c/d")
a=int(input("Introduceti a= "))
b=int(input("Introduceti b= "))
c=int(input("Introduceti c= "))
d=int(input("Introduceti d= "))

def fractii_ad(w,x,y,z):
    f=w*z+y*z
    p=x*z
    h=f/p
    return(h)

def fractii_in(w,x,y,z):
    f=w*y
    p=x*z
    h=f/p
    return(h)

print("a)Adunarea=", fractii_ad(a,b,c,d))
print("b)Inmultirea=", fractii_in(a,b,c,d))