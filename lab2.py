#pb 5
#trebuie sa inlocuim toate aparitiile unui cuvant s cu cuvantul t
'''
prop=input("propozitia:")
s=input("cuvant ce trebuie inlocuit:")
t=input("noul cuvant ce va fi inlocuit:")

lc=prop.split(" ")

for i in range(len(lc)):
    if len(lc[i])==len(s):
        lc[i]=lc[i].replace(s,t)
prop=" ".join(lc)
print(prop)
'''

#pb6
#a)
#trebuie sa decodificam textul
'''
cuvantCifrat=input()
def descifrareCuvant(s):
    n = ""
    i = 0
    cifre = "123456789"
    while i<len(s):
        j=i
        try:
            multiplicator=int(s[i:j+2])
            n=n+multiplicator*s[i+2]
            i=i+3
        except:
            multiplicator=int(s[i])
            n=n+multiplicator*s[i+1]
            i=i+2

    return n
print(descifrareCuvant(cuvantCifrat))
'''

#b)
#trebuie sa codam textul
'''
cuvant=input()
def cifrareCuvant(s):
    i=0
    n=""
    while i<len(s):
        nr=1
        j=i+1
        while j<len(s) and s[i]==s[j]:
            nr=nr+1
            j=j+1
        n=n+str(nr)+s[i]
        i=j
    return n
print(cifrareCuvant(cuvant))
'''

#pb7
'''
Test input:
Astazi am cumparat paine de 5 RON, pe lapte am dat 10 RON, iar de 15 RON am cumparat niste cascaval.De asemenea, mi-am cumparat si niste papuci de 50 RON"
O: 80 RON
'''
'''
fraza=input("SIRUL:")
i=0
j=0
suma=0
while(i<len(fraza)):

    if(fraza[i] in "0123456789"):
        j=i+1
        while(j<len(fraza) and fraza[j] in "0123456789"):
            j=j+1
        suma=suma+int(fraza[i:j])
        i=j
    else:
        i=i+1
print(f"Ana a cheltuit suma de {suma} RON")

'''

#pb8,9 ->am mai facut-o pe undeva, n-o mai fac

#pb10
#se citesc 2 siruri, sa verificam daca sunt anagrame
'''
sir1=input("sir1=")
sir2=input("sir2=")
ok=True
if len(sir1)==len(sir2):
    for litera in sir1:
        if litera not in sir2:
            ok=False
else:
    ok=False

if(ok):
    print("anagrame")
else:
    print("nu sunt anagrame")
'''

#pb11
#a)
'''
sir="Ana are mere"
dict={"A":"Apa","a":"apa","e":"epe"}
trans_tabel=sir.maketrans(dict)
sir_tradus=sir.translate(trans_tabel)
#print(sir_tradus)
dict2={"Apa":"A","apa":"a","epe":"e"}
sir_original=[]

litera=0
while litera<len(sir_tradus):
        cheie=sir_tradus[litera+0]+sir_tradus[litera+1]+sir_tradus[litera+2]
        if cheie in dict2.keys():
            pas=3
            sir_original.append(dict2[cheie])
        else:
            pas=1
            sir_original.append(sir_tradus[litera])
        litera += pas
print("".join(sir_original))
'''
#b)acelasi lucru + despartire in silabe
import re
'''
sir="A-na a-re mul-te me-re ro-sii si de-li-cioa-se"
lista_cuvinte=sir.split()
new_lista_cuvinte=[]

for cuvant in lista_cuvinte:
    lista_silabe_cuvant=cuvant.split("-")
    new_lista_silabe_cuvant = []
    for silaba in lista_silabe_cuvant:
        new_silaba= silaba + "p" + silaba[len(silaba)-1].lower()
        new_lista_silabe_cuvant.append(new_silaba)
    new_lista_cuvinte.append("-".join(new_lista_silabe_cuvant))
#new_cuvant=" ".join(lista_cuvinte)
print(" ".join(new_lista_cuvinte))
'''
dict={}
dict['a']
print(dict)
