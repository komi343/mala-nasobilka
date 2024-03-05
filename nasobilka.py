import random 

def nasobeni(a, b):
    vysledek = a * b
    return vysledek 

def kontrola(vysledek,vyslede_zak):
    body = False
    if vysledek == vysledek_zak: 
        print("jsi šikula,máš to správně")
        body = (body+1)
        print(body)
    else:
        print("Jejda,spletl jsi se,zkus to znova ")
        body = (body-1)
        print(body)
for nasobilka in range (1,11):

    x =random.randint(1,10)
    y =random.randint(1,10)
    vysledek_zak = int(input(f"{x} * {y}"))

    vysledek = nasobeni(x,y)
    kontrola(vysledek,vysledek_zak)


