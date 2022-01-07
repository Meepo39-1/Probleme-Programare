#PB DE LIMBAJ#
#1
'''
def id(n):
   return n
def suma(*numere, f=int):
    s=0
    for i in range(len(numere)):
        s += f(numere[i])

    return s

def radica(x):
    return x**0.5

input_file=open("C:/Users/Edi/PycharmProjects/Ciorna/input.txt")
s=0
for linie in input_file:
    numere=[int(x) for x in linie.rstrip().split()]
    s+= suma(*numere,f=radica)
print(s)
#print(suma(*[4,9,16],f=radica))
'''
#2
'''
def id(n):
    return True
def pozitiv (x):
    return x>0
#a)
def filtreaza(*parametri, functie=id):
    lista=[]
    for element in parametri:
        if functie(element)==True:
            lista.append(element)
    return lista
a=filtreaza(3,-1,6,8,-3, functie=pozitiv)
print(a)
a=filtreaza(3,-1,6,8,-3)
print(a)
a=filtreaza("ana","are","10","mere", functie=str.isalpha)
print(a)

#b)
def filtreaza2(*parametri, functie=id):
    generator=[]
    generator=(x for x in parametri if functie(x)==True)
    return generator
a= filtreaza2(3,-1,6,8,-3, functie=pozitiv)
print(a)
print(sum(a))
print(*a)
#c)
def filtreaza3(lista=[],functie=id):
    lista=[x for x in lista if functie(x)==True]
    return lista

a= filtreaza3(2,3,4, functie=pozitiv)
print(a)
'''
#3
#a)

def cmpValori(x,y):
    return x==y
def cautare(x,L,cmpValori):
    up=None
    for index in range(len(L)):
        if cmpValori(L[index],x):
            up=index
    return up;
#print(cautare(3,[2,2,1,1,1],cmpValori))
#b)
##Testeaza-l intr un nou file
'''
input_file=("input.txt","r")
perechi=[]
for linie in input_file:
    global perechi=[]
    linie=linie.rstrip().split("-")
    pereche=(linie(0)+linie(1),linie(1)+linie(0))
    perechi.append(pereche)
x=int(input())
y=int(input())

cautare((x+y,y+x),perechi,cmpValori)
'''

#c)0   1    2   3 4  5  6    7   8
L=[101,17,-101,13,-13,101,17,-101]
for index in range(len(L)):
    if L[index]<0:
        L[index] *= -1

#0 1 2 3

def e_Palindrom(L):
    lungime=len(L)
    i=0
    j=len(L)-1
    while i<j:
        poz_pereche=cautare(L[i],L[i:(j+1)],cmpValori)

        if poz_pereche != j :
           return False
        i+=1
        j-=1
        L=L[i:(j+1)]
        i =0
        j =len(L)-1
    return True

