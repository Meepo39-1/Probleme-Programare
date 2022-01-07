#SEMINAR4

#1)
'''
input_file=open("numere_comune.in","r")

elem_comune=set()
nr=0
for linie in input_file:
    multime=set([int(x) for x in linie.split()])
    print(multime)
    if nr==0:
        elem_comune=multime
    else:
        elem_comune=elem_comune.intersection(multime)
    nr+=1

output_file=open("numere_comune.out","w")

output_file.write(" ".join([str(x) for x in elem_comune]))
'''
#2)
'''
file1=open("caractere1.in","r")
file2=open("caractere2.in","r")
d1={}
d2={}
str1=file1.read()
str2=file2.read()
for c in str1:
    if c in d1:
        d1[c]+=1
    else:
        d1[c] = 1
for c in str2:
    if c in d2:
        d2[c] += 1
    else:
        d2[c] =1
c_file1=set(d1.keys())
c_file2=set(d2.keys())
intersection=c_file1.intersection(c_file2)
def cheie(x):
    if x in "0123456789":
        return ord(x)-1000
    return ord(x)
ls=[x for x in intersection]
ls.sort(key=cheie)
print(ls)
'''
#3)
'''
file_puncte=open("puncte.in","r")
file_interog=open("interogari.in","r")
file_afisare=open("interogari.out","w")
punct={}
#citire pcte
for linie in file_puncte:
    l=linie.split(maxsplit=2)
    coord=(int(l[0]),int(l[1]))
    punct[coord]=l[2].rstrip()
#operatii pcte, 1=afisare, 0 stergere
for linie in file_interog:
    l=linie.split()
    coord=(int(l[0]),int(l[1]))
    operatie=l[2]
    if operatie=='1':
        try:
            file_afisare.write(str(coord)+": "+punct[coord]+"\n")
        except:
            file_afisare.write(str(coord)+": nu exista"+"\n")
    else:
       try:
           del punct[coord]
       except:
           pass

file_afisare.write("pcte ramase:\n")
for key in dict.keys(punct):
    file_afisare.write(str(key)+" "+str(punct[key])+"\n")
'''
#4)
'''
input_file=open("input.txt",'r')
output_file=open("output.txt","w")
cuvinte=input_file.read().split()
d={}
for cuvant in cuvinte:
    multime=frozenset(cuvant)
    if multime in d:
        d[multime].append(cuvant)
    else:
        d[multime]=[cuvant]
def cheie(x):
    return (len(x),x)
for multime in sorted(d,key=len, reverse=True):
    if len(d[multime])>1:
        message=" ".join(sorted(d[multime],key=cheie))+"\n"
        output_file.write(message)
'''
#5)
'''
import random
import time

n=int(input())
m=int(input())
input_file=open("matrice.in","w")
output_file=open("matrice.out")
for i in range(n):
    for j in range(m):
        message=str(random.randrange(0, 101))+" "
        input_file.write(message)
    input_file.write("\n")
input_file.close()

input_file=open("matrice.in","r")
matrice=[]
for linie in input_file:
    matrice.append([int(nr) for nr in linie.split()])
for linie in matrice:
    print(linie)

input_file.close()
for i in range(n):
    for j in range(i+1 ,m):
        matrice[i][j]=matrice[i][j]^matrice[j][i]
        matrice[j][i]=matrice[i][j]^matrice[j][i]
        matrice[i][j]=matrice[i][j]^matrice[j][i]

print()
for linie in matrice:
    print(linie)
def inter(matrice,i,j):
    l1=matrice[i]
    l2=matrice[j]
    aux=l1
    l1=l2
    l2=aux
    matrice[i]=l1
    matrice[j]=l2

for i in range(n):
    for j in range(i+1,n):
        if matrice[j][n-1]<matrice[i][n-1]:
            inter(matrice,i,j)
print()
for linie in matrice:
    print(linie)
'''
#l_magazine=[magazin={'123',nume:'magazin1''mere':5,'pere':7,'banane:10']}]
nume={}
magazin={}
input_file=open("produse.in")
nr=1
recent_cod=''
for linie in input_file:
    cuv=linie.split()
    if cuv[0]=='Magazin':
        magazin[cuv[1]]={}
        nume[cuv[2]]=cuv[1]
        recent_cod=cuv[1]
    else:
        magazin[recent_cod][cuv[1]]=float(cuv[0])
#print(magazin)
#a)
def interogare(cod_magazin,nume_produs):
    print(magazin[cod_magazin][nume_produs])
def actualizeaza(cod_magazin,nume_produs,marfa_vanduta):
        magazin[cod_magazin][nume_produs] -=marfa_vanduta
#interogare('221','banane')
#actualizeaza('221','banane',5)
#interogare('221','banane')
#b)
#lista de tupluri (nume_mag,cantitate_marfa), ordonata dupa (cantitatea de marfa,nume_magazin)
for nume_magazin in nume.keys():
    total_marfa=0
    for value in magazin[nume[nume_magazin]].values():
        total_marfa+=value
    nume[nume_magazin]=total_marfa

names=list(nume.keys())
values=list(nume.values())
l_magazine=[]
for i in range(len(values)):
    l_magazine.append((names[i],values[i]))
def cheie(x):
    return (x[1],x[0])
# print(sorted(l_magazine,key=cheie))
#c)
tipuri_produse=set()
for cod in magazin.keys():
    prod_mag=set(magazin[cod].keys())
    #print(prod_mag,end='U')
    tipuri_produse=tipuri_produse.union(prod_mag)
    #print(tipuri_produse)
print(tipuri_produse)