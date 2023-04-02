print ("Qual a progressão que você quer?")
print ("1 - Progressão Aritmética")
print ("2 - Progressão Geométrica")
a = int(input())

def proggeometrica(a1, q, n):
    d = 0
    pg = list()
    while d != n:
        an = a1*q**(d)
        pg.append(an)
        d += 1
    
    return print(pg)

def progaritmetica(a1, r, n):
    d = 0
    pa = list()
    while d != n:
        an = a1 + (d)*r
        pa.append(an)
        d += 1
    return print(pa)

if a == 1:
    a1 = int(input("Digite o primeiro termo:"))
    r = int(input("Digite a razão:"))
    n = int(input("Até qual termo (o valor de enésimo do termo):"))
    progaritmetica(a1, r, n)
    
    if r < 0:
        print("Esta é uma progressão descrescente, pois o valor da razão é negativo")
    else:
        print("Esta é uma progressão crescente, pois o valor da razão é positivo")
    if r == 0:
        print("Esta é um progressão constante")

if a == 2:
    a1 = int(input("Digite o primeiro termo da progressão:"))
    q = int(input('Digite a razão:'))
    n = int(input("Até que termo (digite o valor enésimo do termo):"))
    proggeometrica(a1, q, n)
    if q < 0:
        print("Esta é uma progressão descrescente, pois o valor da razão é negativo")
    else:
        print("Esta é uma progressão crescente, pois o valor da razão é positivo")
    if q == 0:
        print("Esta é um progressão constante")



