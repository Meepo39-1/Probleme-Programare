#pb 1
'''
a=int(input())
b=int(input())

arr=[]
nr=0
x=0
while(x<a and x<100):
    arr.append(x)
    nr=nr+1
    x=x+5
while(x<=b):
    x=x+5
while(x<100):
    arr.append(x)
    nr=nr+1
    x=x+5

for i in range (nr):
    print(arr[i])
for i in range(nr-1,-1,-1):
    print(arr[i])
'''

#pb2
'''
a=int(input())
b=int(input())

x=0
y=1
while(y<a):
    y,x=x+y,y
if(y<=b):
    print(y)
'''
#pb3
'''
n=int(input())

x,y=0,1

while(y<n):
    x,y=y,x+y
if(y==n):
    print(y)
else:
    while(n>0):
        while(y>n):
            x=y-x
            y=y-x
        print(y)
        n=n-y
'''
#pb6

#se citeste un cuvant s, sa verificam daca e palindrom sau semipalindrom(format din doua jumatati egale)
'''
cuvant=input("introduceti cuvantul:")

marime= len(cuvant)

#verific daca e palindrom

i=0
j=marime-1
ok = True
while i<j:
   if cuvant[i]!=cuvant[j]:
       ok=False
       break
   i=i+1
   j=j-1

#afisez daca e palindrom, altfel verific daca e semipalindrom
if ok:
    print("palindrom")

if (cuvant[:(marime // 2)] == cuvant[(marime // 2):]):
    print("semipalindrom")
    ok=True
if (ok==False):
    print("nada")
'''

#pb7
#se citeste un sir s si un numar k. Sterge caracterul de pe pozitia k
'''
s=input("cuvant=")
k=int(input("pozitie="))
print("litera care o sa dispara este:",s[k])
s=s[:k]+s[k+1:]
print(s)

'''
#pb8
#se citeste un cuvant s, sterge prima vocala
'''
pozitie=0
ok=False
cuvant=input("cuvant:")
for i in range(len(cuvant)):
    if (cuvant[i].lower() in "aeiou"):
        pozitie=i
        ok=True
        break
if ok:
    cuvant=cuvant[:pozitie]+cuvant[pozitie+1:]
print(cuvant)
'''
#pb9
'''
DI:
 -un cuvant w
 -un nr natural p
 -un nr natural n
 -n cuvinte

CERINTA:
Sa se afiseze toate cuvintele:
-"p" rime cu w
-au lungime cel putin p+2

exemplu:
w="mere"
p=2
n=4
pere teste are programare
O: pere, programare
'''
'''
w=input("w=")
p=int(input("p="))
n=int(input("n="))
sir=input(f"introduceti {n} cuvinte:")
afisare = ""
def filtrareCuvant(cuvant):
    if len(cuvant)>=p+2:
        if(w[-p:]==cuvant[-p:]):
            return True
    return False


cuvinte=sir.split()
for i in range(len(cuvinte)):
    if(filtrareCuvant(cuvinte[i])):
        afisare=afisare+cuvinte[i]+" "

print(afisare)
'''

#pb10


#citim sirul
'''
s=input("introduceti sirul:")

lungime=len(s)
i=0
t=""
for i in range(lungime//2):
    cs=s[:i+1]*(lungime//(i+1))
    if cs==s:
        t=s[:i+1]

if t!="":
    print(t)
else:
    print("Nu exista")
'''
