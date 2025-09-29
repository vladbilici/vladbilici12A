def suma(a, b, c, d):
    return a+b+c+d

def media_nr(g, h, j, k):
    return (g+h+j+k)/4

def minim(a1, b1, c1, d1):
    return min(a1, b1, c1, d1)

def radacina(a, b):
    if a == 0:
        return "Nu exista solutie (a=0)"
    return -b/a

def cmmd(n):
    d = 2
    while d <= n:
        if n % d == 0:
            return d
        d += 1

def cmmdc_ab(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def cmmmc_ab(a,b):
    return abs(a * b) // cmmdc_ab(a, b)

def ultima_cifra(n):
    return n % 10

def nr_cifre(n):
    nr_c = 0
    while n > 0:
        nr_c += 1
        n //= 10
    return nr_c

def cifra_sup(n):
    while n >= 10:
        n //= 10
    return n

a,b,c,d=int(input('a=')),int(input('b=')),int(input('c=')),int(input('d='))
n=int(input('n='))
print('a) Suma numerelor',a, '+', b, '+',c,'+',d, '=',suma(a,b,c,d))
print('b) Media numerelor (' ,a, '+', b, '+',c,'+',d,')/4=',media_nr(a,b,c,d))
print('c) Minimul dintre numerele ',a,', ' ,b,',',c,',',d, 'este',minim(a,b,c,d))
print('f) Radacina ecuatiei ax+b=0 ' ,radacina(a,b))
print('g) Cel mai mic divizor al nr n' ,cmmd(d))
print('h) Cel mai mare divizor comun dintre', a, 'si',b, 'este', cmmd(d))
print('i) Cel mai mic multiplu comun al numerelor ', a, 'si',b, 'este', cmmmc_ab(a,b))
print('j) Ultima cifra din notatia zecimala al nr n este', ultima_cifra(n))
print('k) Numarul de cifre in notatia zecimala al nr n este', nr_cifre(n))
print('l) Cifra superioara in notatia zecimala al nr n este', cifra_sup(n))