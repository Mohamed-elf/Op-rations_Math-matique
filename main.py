import math
def somm(a,b):
    s= a+b
    return s
def Multi(a,b):
    m= a*b
    return m
def Div(a,b):
    d= a/b
    return d
def equaDegr1(a, b, c):
    x = (c-b)/a
    return x
while True:
    print(" Made by Mohamed elfarfachi.\n")
    Menu = {
        "-|Addition (+)                        ": 1,
        "-|multiplication (x)                  ": 2,
        "-|division (÷)                        ": 3,
        "-|Racine carrée (√)                   ": 4,
        "-|équations du première degré (ax+b=c)": 5,
        "-|exit                                ": 0,
    }
    for key, value in Menu.items():
        print(f'{key} : {value}')

    ch=int(input("entrer votre choix :"))
    if ch==1:
        print("---------------------------Addition(+)--------------------------------")
        nb1=int(input("Entre le première Nombre :"))
        nb2= int(input("Entre le deuxième Nombre :"))
        som=somm(nb1, nb2)
        print(nb1,'+',nb2,'=',som)
        print("----------------------------------------------------------------------")
    if ch==2:
        print("----------------------------multiplication(x)-------------------------")
        nb1 = int(input("Entre le première Nombre :"))
        nb2 = int(input("Entre le deuxième Nombre :"))
        prod=Multi(nb1, nb2)
        print(nb1,'x',nb2,'=',prod)
        print("----------------------------------------------------------------------")
    if ch==3:
        print("------------------------------division(÷)-----------------------------")
        nb1 = int(input("Entre le première Nombre :"))
        nb2 = int(input("Entre le deuxième Nombre :"))
        d=Div(nb1,nb2,)
        print(nb1,'÷',nb2,'=',d)
        print("----------------------------------------------------------------------")
    if ch == 4:
        print("--------------------------Racine carrée (√)---------------------------")
        n=float(input("Saisir un nombre:"))
        root = math.sqrt(n)
        print("√",n,"=",root)
        print("----------------------------------------------------------------------")
    if ch == 5:
        print("-----------------équations du première degré (ax+b=c)-----------------")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        X = equaDegr1(a, b, c)
        print(a, "x", "+", b, "=", c, "résulta :", X)
        print("----------------------------------------------------------------------")

    if ch == 0:
        break