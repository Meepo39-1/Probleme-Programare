#pb3
'''
lista =[0,1,2,3,5,0]
while (0 in lista):
    lista.remove(0)
print(lista)
'''

#pb4
'''
k=2
lista =[24,23,42,32,12,5,0,0]

index=0
suma=sum(lista[index:index+k])
Min=suma
MinIndex=0
while index<=len(lista)-k:
    suma=sum(lista[index:index+k])
    if suma<Min:
        Min=suma
        MinIndex=index
    index +=1
lista=lista[0:MinIndex]+lista[MinIndex+k:]
print(lista)
'''
#pb5

'''
string=input("elementele vectorului:")
vector_sortat_cresc=string.split(" ")
vector_sortat_cresc=[int(x) for x in vector_sortat_cresc]

index=0
while index<len(vector_sortat_cresc):
    try :
        while vector_sortat_cresc[index]==vector_sortat_cresc[index+1]:
            vector_sortat_cresc=vector_sortat_cresc[:index]+vector_sortat_cresc[index+1:]
    except:
        pass
    index +=1
print(vector_sortat_cresc)
'''
#pb6
'''
lista=[-3,4,2,-3,4]

index=0
while index<len(lista):
    if lista[index]<0:
        lista=lista[:index+1]+[0]+lista[index+1:]
    index +=1
print(lista)
'''


#SORTARI
#pb1)
'''
prop=input()
lista=[cuvant for cuvant in prop.split() if len(cuvant)>1]
lista.sort(reverse=True,key=len)
print(lista)
'''
#pb2)
'''
inp=input()
vector=[int(x) for x in inp.split()]

#11 45 20 810 179 81 1000

def cheie(x):
    cx=x
    suma_cifre=0
    while x!=0:
        suma_cifre += x % 10
        x = x // 10
    return (suma_cifre, -cx)

vector.sort(key=cheie)
print(vector)
'''

#pb3)
#n=int(input())
#date=input().split()
'''
elev=[]
elev.append(date[0])
elev.append(date[1])
elev.append(int(date[2]))
note=[date[indice] for indice in range(3,len(date))]
elev.append(note)
print(elev)
'''
'''
n=int(input("n="))
catalog=[]
#a) memorare date
for indice_elev in range(n):
    elev=[]
    date=input().split(maxsplit=3)
    #nume
    elev.append(date[0])
    #prenume
    elev.append(date[1])
    #grupa
    elev.append(int(date[2]))
    #Note
    note=[int(x) for x in date[3].split()]
    elev.append(note)
    catalog.append(elev)

#b) adaugare situatie promovabilitate
for elev in catalog:
    promovat=True
    for nota in elev[3]:
        if nota<5:
            promovat=False
            break
    elev.append(promovat)

#c)
def c_sort(elev):
    grupa=elev[2]
    nume=elev[0]
    prenume=elev[1]
    return (grupa,nume,prenume)

catalog.sort(key=c_sort)

#d)
def crit2(elev):
    promovat=elev[4]
    note = elev[3]
    if promovat==True:
        medie = sum(note) / len(note)
        return -medie
    else:
        restante=0
        for nota in note:
            if nota<5:
                restante +=1
        return restante

def d_sort(elev):
    nume=elev[0]
    prenume=elev[1]
    grupa=elev[2]
    promovat=elev[4]
    return (grupa,not(promovat),crit2(elev),nume,prenume)


catalog.sort(key=d_sort)
print(catalog)
'''
#pb4)
'''
lista=[2,6,4,7,3,19,25,40]
def cheie(element):
    paritate=element%2
    if paritate==1:
        element=element*(-1)
    return(paritate,element)

lista.sort(reverse=True,key=cheie)
print(lista)
'''

# MATRICE, VECTORI
#pb1
'''
2 2
1 2
3 4
'''
'''
# citire matrice
matrix=[]
m,n=[int(x) for x in input().split()]
matrix=[[int(x) for x in input().split()] for i in range(m)]


# construire matrice transpusa
# varianta fara comprehension
matrixT=[]
for linie in range(m):
    linieT=[]
    for coloana in range(n):
        linieT.append(matrix[coloana][linie])
    matrixT.append(linieT)
# varianta cu comprehension
matrixT=[[matrix[coloana][linie] for coloana in range(n)] for linie in range(m)]
# afisare matrice originala
for linie in matrix:
    for element in linie:
        print(element,end=' ')
    print()

#afisare matrice transpusa
for linie in matrixT:
    for element in linie:
        print(element,end=' ')
    print()
'''
#pb2
'''
m=int(input())
n=int(input())
matrice=[]
'''
#citire matrice
'''
3
3
8 5 6
14 2 3
6 5 4
'''
'''
matrice=[[int(element) for element in input().split()] for linie in range(m)]

# afisare matrice originala
print("MATRICE ORIGINALA:")
for linie in matrice:
    for element in linie:
        print(f"{element:4}",end=' ')
    print()

# sortare elemente de pe prima coloana
def schimba(i,j):
    aux=matrice[i]
    matrice[i]=matrice[j]
    matrice[j]=aux
for i in range(m):
    for j in range(i,m):
        if matrice[i][0]>matrice[j][0]:
            schimba(i,j)

print("MATRICE SORTATA:")
for linie in matrice:
    for element in linie:
        print(f"{element:4}", end=' ')
    print()
'''
#pb 3
'''
BN=[[1],[1,1]]
n=int(input())
lungime=2
for i in range(2,n):
    lungime +=1
    list=[1]
    for j in range(1,lungime-1):
        list.append(BN[i-1][j-1]+BN[i-1][j])
    list.append(1)
    BN.append(list)

def max_char(matrice):
    list = []
    for linie in matrice:
        max_nr=max(linie)
        nr_c=1
        while max_nr>9:
            nr_c += 1
            max_nr= max_nr//2
        list.append(max_nr)
    return max(list)

c = max_char(BN) + 1
for linie in BN:
    for x in linie:
       print(f'{x:c}',end=" ")
    print()
'''''' ??????? '''
# pb 4
#a)
'''
N=int(input())
matrice=[]
nr=1
for i in range(N):
    list=[]
    for j in range(N):
        list.append(nr)
        nr+=1
    matrice.append(list)

matrice=[[i*N+j+1 for j in range(N)] for i in range(N)]
print(matrice)
#b)
c_st=0
c_dr=N-1
c_sus=0
c_jos=N-1
lista_poz=[]
for i in range(N//2+1):
    # stanga->dreapta
    for coloana in range(c_st,c_dr+1):
       # print(matrice[c_st][coloana],end=' ')
        lista_poz.append((c_st,coloana))
    c_sus+=1
    #sus->jos
    for linie in range(c_sus,c_jos+1):
        #print(matrice[linie][c_dr],end=' ')
        lista_poz.append((linie,c_dr))
    c_dr= c_dr-1
    # dreapta->stanga
    for coloana in range(c_dr,c_st-1,-1):
        #print(matrice[c_jos][coloana],end=' ')
        lista_poz.append((c_jos,coloana))
    c_jos=c_jos-1

    # jos->sus
    for linie in range(c_jos,c_sus-1,-1):
       # print(matrice[linie][c_st],end=' ')
        lista_poz.append((linie,c_st))
    c_st+=1

#c)
for linie,coloana in lista_poz:
    print(matrice[linie][coloana],end=" ")
'''
#5) Ciurul lui Erostastene
'''
list=[2]
N=int(input())
for nr in range(3,N+1,2):
    list.append(nr)
def prim(n):
    if n==2:
        return True
    if n%2==0:
        return False
    for nr in range(3,n*n+1):
        if n%nr==0:
            return False
    return True

for nr in list:
    if prim(nr)==True:
        for nr2 in list:
            if nr2!=nr and nr2%nr==0:
                list.remove(nr2)

print(list)
'''

#6)
''''''
l=[0]
v=[0]
c=[]
ci=[]
u=max(l)+1
i,j=0,0
while i<len(l) and j<len(v):
    if l[i]<v[j]:
        if u != l[i]:
            c.append(l[i])
            u=l[i]
        i+=1
    else:
        if u!=v[j]:
            c.append(v[j])
            u=v[j]
        j+=1
while i<len(l):
    if u != l[i]:
        u = l[i]
        c.append(l[i])
    i+=1

while j<len(v):
    if u != v[j]:
        u=v[j]
        c.append(v[j])
    j+=1
print("reuniunea:",c)

i,j=(0,0)
while i<len(l) and j<len(v):
    if l[i]<v[j]:
        i+=1
    elif l[i]>v[j]:
        j+=1
    else:
        ci.append(v[j])
        i+=1
        j+=1
print("intersectia",ci)