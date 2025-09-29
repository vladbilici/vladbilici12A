x,y=int(input('a=')), int(input('b='))

def suma_ab(a,b):
    return a+b

def produs_ab(a,b):
    return a*b

def min_ab(a,b):
    return min(a,b)

def media_ab(a,b):
    return (a+b)/2
    
def maxim_ab(a,b):
    return max(a,b)
    
def cmmdc_ab(a, b):
    while b!= 0:
        a,b = b, a%b
    return a
    
def cmmmc_ab(a,b):
    return abs(a * b) // cmmdc_ab(a, b)

def divizori_comuni(a,b):
    divizor=[]
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            divizor.append(i)
    return divizor

def multipli_comuni(a,b):
    m = cmmmc_ab(a,b)
    return [m*i for i in range(1,6)]

def cifre_comune(a,b):
    return sorted(set(str(abs(a))) & set(str(abs(b))))

def cifre_diferenta(a,b):
    return sorted(set(str(abs(a))) - set(str(abs(b))))

def divizori(n):
    return [i for i in range(1,n+1) if n%i==0]

def prietene(a,b):
    return len(divizori(abs(a))) == len(divizori(abs(b)))


print('a) Suma numerelor =', suma_ab(x,y))
print('b) Produsul numerelor = ', produs_ab(x, y))
print('c) Media numerelor = ', media_ab(x,y))
print('d) Cel mai mare divizor comun =', cmmdc_ab(x,y))
print('e) Cel mai mic multiplu comun =', cmmmc_ab(x,y))
print('f) Minimul numerelor = ', min_ab(x, y))
print('g) Maximul numerelor=', maxim_ab(x,y))
print('h)', x,'+',y,'=',suma_ab(x,y))
print('i)', x,'*',y,'=',produs_ab(x,y))
print('j) Divizorii comuni:', divizori_comuni(x,y))
print('k) 5 multipli comuni:', multipli_comuni(x,y))
print('l) Cifre comune:', cifre_comune(x,y))
print('m) Cifre in primul si nu in al doilea:', cifre_diferenta(x,y))
print('n)', "PRIETENE" if prietene(x,y) else "NU SUNT PRIETENE")