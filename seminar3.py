#exemple
#1
#a)
'''
import re
propozitie="ala,,bala,..porto....,.,.,cala!!!"
propozitie=re.split("[.,!]+",propozitie)
print(propozitie)
#propozitie=sorted(propozitie) creeaza inca un obiect
propozitie.sort()

propozitie.remove("")
print(propozitie)

propozitie=" ".join(propozitie)
print(propozitie)
'''
#b)
'''
s="ablala"

nr=int(s[:2])
print(nr)
'''
# pb cu siruri si liste, comprehensiune
#1)
'''
vocale="aeiouAEIOU"
test="aceasta e o propozitie de test"
lista_cuvinte=test.split(" ")
ls=[cuvant for cuvant in lista_cuvinte if(cuvant[0] in vocale)]
print(ls)
'''
#2)
'''
ls=[[4,7,3],[3,1,20],[5,2,11]]
for lista in ls:
    for element in lista:
        lista_m.append(element)

lista_m=sorted([element for lista in ls for element in lista])
print(lista_m)
'''

#3)
'''
#a)
alfabet=[chr(cod_asci) for cod_asci in range(97,123)]
cuvant="".join(alfabet)
# print(cuvant)
#b)
text_de_criptat="abcdefgh"
k=1
ls_aux=[chr(97+((ord(caracter)-97+k)%26)) if(ord(caracter)>=ord('a') and ord(caracter)<=ord('z')) else caracter for caracter in text_de_criptat]
text_criptat="".join(ls_aux)
print(text_criptat)

ls_aux=[chr(97+((ord(caracter)-97-k)%26)) if(ord(caracter)>=ord('a') and ord(caracter)<=ord('z')) else caracter for caracter in text_criptat]
text_original="".join(ls_aux)
print(text_original)
'''
#OPERATII LISTE

#1)
'''
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]

n=len(l1)
pas=1
while pas<n:
    l1=l1[:pas]+l2[pas:pas+1]+l1[pas+1:]
    pas +=2
print(l1)
'''
#2)
'''
lista=[2,3,4,0,4,5,6,2,5,2,0]

index1=0
index2=0
for index in range(len(lista)):
    if lista[index]==0:
        index1=index
        index2=index
        break
index +=1
while lista[index]!=0:
    index+=1

    index2=index

lista=lista[:index1]+lista[index2+1:]
print(lista)
'''
