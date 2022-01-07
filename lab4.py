# 1)
# numar variabil de nume de fisiere, returneaza un dictionar cu frecventele
# a)
'''
def frecventa(*fisiere):
    freq={}
    for fisier in fisiere:
        file=open(fisier,'r')
        text=file.read().split()
        for cuvant in text:
            if cuvant in freq:
                freq[cuvant]+=1
            else:
                freq[cuvant]=1
    return freq
#frecventa("caractere1.in","caractere2.in")
#b)
def cuvinte(*fisiere):
    l_cuvinte=[]
    for fisier in fisiere:
        file=open(fisier,'r')
        text=file.read().split()
        l_cuvinte.extend(text)
    print(sorted(l_cuvinte,key=lambda x: x))
#cuvinte("caractere1.in","caractere2.in")
#c)
def c(fisier):
    dict=frecventa(fisier)
    ls=[]
    for key in dict.keys():
       ls.append((key,dict[key]))
    print(sorted(ls,key=lambda x: x[1],reverse=True))
c("caractere1.in")
#d)
''''''
def d(fisier):
    dict=frecventa(fisier)
    print(dict)
    pereche_max= (-1,'a')
    for key in dict.keys():
        if max(dict[key],pereche_max[0])==pereche_max[0] and max(dict[key],pereche_max[0])==dict[key]:
            pereche_max=(dict[key],min(key,pereche_max[1]))
        else:
            pereche_max=max((dict[key],key),pereche_max)
    print(pereche_max)
#d("caractere2.in")
#e)
def dcos(fisier1,fisier2):
    f1=frecventa(fisier1)
    f2=frecventa(fisier2)

    suma_numarator = 0
    for cuvant in f1.keys():
        if cuvant not in f2:
            suma_numarator+=0
        else:
            suma_numarator += f1[cuvant]*f2[cuvant]
    import math
    rad1,rad2=(0,0)
    for cuvant in f1.keys():
        rad1 += f1[cuvant]*f1[cuvant]
    for cuvant in f2.keys():
        rad2 +=f2[cuvant]*f2[cuvant]
    rad1=math.sqrt(rad1)
    rad2=math.sqrt(rad2)
    return suma_numarator/(rad1*rad2)
#print("{:.2f}".format(dcos("caractere1.in","caractere2.in")))
print("%.2f"%dcos("caractere1.in","caractere2.in"))
print(dcos("caractere1.in","caractere2.in"))
#???
'''
# 2)
'''
file=open("caractere1.in","r")
output=open("rime.txt","w")
p=2
text=file.read().split()
d={}
for cuvant in text:
    sufix=cuvant[-p:]
    if sufix in d:
        d[sufix].append(cuvant)
    else:
        d[sufix]=[cuvant]
for sufix in d.keys():
    output.write(" ".join(d[sufix])+"\n")
'''
# 3)
'''
input_file = open("test.in", 'r')
output_file= open("test.out",'w')
nota = 1
import re

for line in input_file:
    exercitiu = line.rstrip()
    exercitiu=re.split(r'\*|=', exercitiu)
    m1=int(exercitiu[0])
    m2=int(exercitiu[1])
    r=int(exercitiu[2])
    if m1*m2==r:
        print(f"Corect: {m1}*{m2}={r}")
        nota+=1
    else:
        print(f"GRESIT: {m1}*{m2}={r}")

print(f"Nota:{nota}")
'''
#4)
'''
input_file=open("date.in","r")
output_file=open("date.out","w")
elevi=[]
for linie in input_file:
    text=linie.rstrip().split(maxsplit=1)
    elevi.append((text[0],text[1]))
adrese=[]
parole=[]
import random
import string
for elev in elevi:
    adresa=elev[1]+"."+elev[0]+"@s.unibuc.ro"
    adrese.append(adresa)
    parola = ""
    #litera mare
    litera_mare=random.choice(string.ascii_uppercase)
    #3 litere mici
    litere_mici="".join(random.choices(string.ascii_lowercase,k=3))
    #4 cifre
    cifre=[]
    for i in range(4):
        cifre.append(str(random.randint(0,9)))
    cifre="".join(cifre)
    parola=litera_mare+litere_mici+cifre
    parole.append(parola)

for index_elev in range(len(elevi)):
    output_file.write(str(adrese[index_elev])+","+str(parole[index_elev])+"\n")
'''
#5)
'''
def negative_pozitive(numere):

    pozitive=[x for x in numere if x>0]
    negative=[x for x in numere if x<0]

    return(negative,pozitive)

input_file=open(input(),'r+')
numere=[]
for line in input_file:
    numere.extend([int(x) for x in line.rstrip().split()])
numere_poz=negative_pozitive(numere)[1]
numere_neg=negative_pozitive(numere)[0]
input_file.writelines(['\n'+" ".join(str(x) for x in numere_poz)+'\n', " ".join(str(x) for x in numere_neg)])
'''
#6)
#a)
input_file=open("elevi.in","r")
catalog={}
for line in input_file:
    elev=line.rstrip().split(maxsplit=3)
    catalog[elev[0]]={"nume":elev[1],"prenume":elev[2],"note":[int(nota) for nota in elev[3].split()]}
    #print(elev)
#print(d)
#b)
def marire_elev(CNP,catalog):
    if CNP in catalog.keys():
        catalog[CNP]['note'][0]+=1
        print(catalog[CNP]['note'][0])
    else:
        print(None)
#marire_elev(input(),catalog)
#c)
def update_note(CNP,note,catalog):
    if CNP in catalog.keys():
        catalog[CNP]['note'].extend(note)
        print(catalog[CNP]['note'])
    else:
        print(None)
lista1_note=[10,8]
#print(catalog)
#update_note(input(),lista1_note,catalog)
#d)
def stergere(CNP,catalog):
    if CNP in catalog.keys():
        del catalog[CNP]
        print(catalog)
#stergere(input(),catalog)
#e)
l_elevi=[]
for cnp in catalog.keys():
    elev=[]
    elev.append(catalog[cnp]['nume'])
    elev.append(catalog[cnp]['prenume'])
    elev.append(catalog[cnp]['note'])
    l_elevi.append(elev)
#print(l_elevi)
def cheie(elev):
    note=elev[2]
    medie=sum(note)/len(note)
    nume=elev[0]
    return(medie,nume)
#descrescator dupa medie, nume
l_elevi.sort(key=cheie,reverse=True)
output_file=open("elevi.out","w")
#for elev in l_elevi:
    #elev.append("\n")
    #output_file.write(" ".join(str(x) for x in elev))
#f)
import random
import string
def genereaza_coduri(catalog):
    for cnp in catalog.keys():
        parola=""
        litere=random.choices(string.ascii_letters,k=3)
        cifre=random.choices(string.digits,k=3)
        parola+="".join(litere)+"".join(cifre)
        catalog[cnp]['cod']=parola
genereaza_coduri(catalog)
#print(catalog)
#7)
def citire_lista(lista=[]):
    #nr_elemente=int(input())
    elemente=input().split()
    lista=elemente
    return(lista)
#a()
def b(s,x,i=0,j=0):
    cs=s[i:j]
    position=i
    for value in cs:
        if value>x:
            return position
        position+=1
    return -1
#t=(0,1,2,3)
#print(b(t,-1))
#c)
'''
lista=citire_lista()
descrescator=True
for index in range(1,len(lista)):
    if b(lista,lista[index],0,len(lista))!=0:
        descrescator=False
if descrescator:
    print('Da')
else:
    print('Nu')
'''
#8)
def liste_x(x,*liste):
    nr=0
    for lista in liste:
        if x in lista:
            nr+=1
    return nr
nr=liste_x(3,[1,5,7],[3],[1,8,3],[])
#print(nr)
#b)
rez=None
def liste_x2(x,*liste):
    nr=0
    for lista in liste:
        if x in lista:
            nr+=1
    global rez
    rez=nr

liste_x2(3,[1,5,7],[3],[1,8,3],[])
#print(rez)
#9)
def chad_number(*numere):
    chad_nr=0
    for numar in numere:
        max_c=0
        while numar!=0:
            max_c=max(max_c,numar%10)
            numar=numar//10
        chad_nr=chad_nr*10+max_c
    return chad_nr
#print(chad_number(5251,73,8,133))
def based_2(a,b,c):
    if chad_number(a,b,c)==111:
        return True
    return False
print(based_2(1001,11,100))
print(based_2(1001,17,100))

#10)
import re
def cauta_cuvant(cuvant,name_output_file,*nume_fisiere):
    output_file=open(name_output_file,'w')
    for nume in nume_fisiere:

        output_file.write(nume+" ")
        fisier=open(nume,'r')
        nr_linie=0
        apare_fisier=False
        for linie in fisier:
            nr_linie+=1
            text=re.split(" |-|!",linie.rstrip())
            apare_linie=False
            for cuv in text:
                if cuv.lower()==cuvant.lower():
                    apare_linie=True
                    apare_fisier=True
            if apare_linie==True:
                output_file.write(str(nr_linie)+" ")
        if apare_fisier==False:
            output_file.write("nu apare")
        output_file.write("\n")




cauta_cuvant('floare','rez.txt','eminescu.txt','paunescu.txt')
def twoSum(nums,target):
    d = {}
    rez = []
    for index in range(len(nums)):
        if nums[index] in d.keys():
            rez = [d[nums[index]], index]
            return rez
        else:
            d[target - nums[index]] = index

print(twoSum([3,3],6))
