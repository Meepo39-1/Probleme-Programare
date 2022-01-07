#1)
'''
def min_max(lista):
    return(min(lista),max(lista))
f=open("textFile.txt",'r')

# print(min_max([3,-3,1,7,3,2]))
def incarca_file(file):
    lista=[]
    for linie in file:
        lista.append([int(x) for x in linie.rstrip().split(" ")])
    return lista

#print(incarca_file(input_file))
name=input()
input_file=open(name,'r')
output_file=open("egale.txt","w")
lista=incarca_file(input_file)
for index in range(len(lista)):
    limite=min_max(lista[index])
    if limite[0]==limite[1]:
        output_file.write(str(index))
        output_file.write("\n")

max_global,min_global=(None,None)
#lista=incarca_file(input_file)
#textFile.txt
#print(lista)
listaMax=[]
listaMin=[]
for index in range(len(lista)):
    #print(lista[index])
    pereche=min_max(lista[index])
    listaMin.append(pereche[0])
    listaMax.append(pereche[1])
   # print(listaMin,"hm")

pereche=min_max(listaMin)
min_global=pereche[0]
pereche=min_max(listaMax)
max_global=pereche[1]
a=min_global
b=max_global
print(a,b)
'''
#2)
'''
def deviruseaza(prop):
    #inversare litere
    lista=prop.split(" ")
    #print(lista)
    for index in range(len(lista)):
        if(len(lista[index]))>1:
            lista[index]=lista[index][len(lista[index])-1]+lista[index][1:(len(lista[index])-1)]+lista[index][0]
    newLista=[]
    for index in range(len(lista)-1,-1,-1):
        #print(index)
        newLista.append(lista[index])
    return " ".join(newLista)
#print(deviruseaza("aorectc aropozitip este aceasta"))

#b)
def prim(n):
    if n==2:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3,n//2+1,2):
        if n%i==0:
            return False
    return True


def prime(n,numar_maxim=0):
    l=[]

    if numar_maxim==0:
        nr=n
    else:
        nr=numar_maxim

    for i in range(n):
        if prim(i) and nr!=0:
            l.append(i)
            nr-=1
    return l
#print(prime(2))
input_file=open("intrare.in","r")
output_file=open("intrare_devirusata.out","w")
nr=1
for linie in input_file:
    linie=linie.rstrip()
    if prim(nr)==True:
        output_file.write(deviruseaza(linie))
        #print(deviruseaza(linie))
    else:
        output_file.write(linie)
    output_file.write("\n")
    nr+=1

def cifra_control(n):
    r=n%9
    if r==0:
        return 9
    return r
def insereaza_cifra_control(lista):
    newLista=[]
    for nr in lista:
        newLista.append(nr)
        newLista.append(cifra_control(nr))
    lista=newLista
c=[2,3,4,18]
#insereaza_cifra_control(c)
#print(c)
def egale(*liste):
    aux=liste[0]
    for index in range(len(liste)):
        if aux!=liste[index]:
            return False
    return True
#print(egale([22],[1],[1],[22]))
input_file=open("numere.in")
output_file=open("numere.out","w")
for linie in input_file:
    numere=[int(x) for x in linie.rstrip().split(" ")]
    for nr in numere:
        output_file.write(str(nr)+" ")
        output_file.write(str(cifra_control(nr))+"\n")

file1=open("numere.in")
file2=open("numere2.in")

nr_file1=[]
nr_file2=[]
for linie in file1:
    numere=[int(x) for x in linie.rstrip().split()]
    for nr in numere:
        if nr not in nr_file1:
            nr_file1.append(nr)
for linie in file2:
    numere=[int(x) for x in linie.rstrip().split()]
    for nr in numere:
        if nr not in nr_file2:
            nr_file2.append(nr)
nr_file1.sort()
nr_file2.sort()
sir_f1=[]
sir_f2=[]
for nr in nr_file1:
    sir_f1.append(cifra_control(nr))
for nr in nr_file2:
    sir_f2.append(cifra_control(nr))
if egale(sir_f1,sir_f2):
    print("Da")
else:
    print("Nu")
'''

#a)
input_file=open("intrare.in")
d={}
for linie in input_file:
    date=linie.rstrip().split(" ")
    cod=date[0]
    cantitate=int(date[1])
    jucarie=date[2]

    if cod in d:
        if jucarie in d:
            d[cod][jucarie]+=cantitate
        else:
            d[cod][jucarie]=cantitate
    else:
        d[cod]={}
        d[cod][jucarie]=cantitate
print(d)

#b)
# descrescator dupa cantitate si crescator dupa nume
def cheie(pereche):
    nume=pereche[0]
    cantitate=pereche[1]

    return(cantitate*-1,nume)

def interogare(d,cod):
    jucarii=d[cod].keys()
    perechi=[]

    for jucarie in jucarii:
        cantitate=d[cod][jucarie]
        perechi.append((jucarie,cantitate))
    perechi.sort(key=cheie)
    return perechi

#print(interogare(d,'S1'))
def jucarii(d):
    multime=set()
    for spiridus in d.keys():
        multime2=set(d[spiridus].keys())
        multime=multime.union(multime2)
    return multime

for jucarie in jucarii(d):
    print(jucarie,end=',')
print()

#descrescator dupa nr de jucarii diferite, descrescator dupa cantitatea de jucarii, crescator dupa cod
def cheie2(triplet):
    nr=triplet[1]
    cod=triplet[0]
    cantitate=triplet[2]
    return(-1*nr,-1*cantitate,cod)
def spiridusi(d):
    lista=[]
    for cod in d.keys():
        numar_jucarii=len(d[cod].keys())
        cantitate=0
        for jucarie in d[cod].keys():
            cantitate+=d[cod][jucarie]
        lista.append((cod,numar_jucarii,cantitate))
    lista.sort(key=cheie2)
    return lista
    # return lista (cod, numar jucarii, cantitate), ord dupa criteriile de mai sus
for triplet in spiridusi(d):
    print(triplet)
def actualizare(d,cod,jucarie):

#daca sunt cel putin 2 tipuri de jucarii stergem info despre jucarie
#altfel, vom returna false
    if len(d[cod].keys())>=2:
        del d[cod][jucarie]
        return True
    else:
        return False
actualizare(d,'S1','trenulet')
print(interogare(d,'S1'))
