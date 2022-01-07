# pb1 biti...
'''''''''
def putere2(n):
    nr = -1
    if (n & (n - 1) == 0):
        while (n & 1 == 0):
            n = n >> 1
            nr = nr + 1
    if (nr == -1):
        return 0
    else:
        return nr + 1
'''''
#pb6 biti
import math

"""
#citim numarul de elemente
n=int(input())

#definim functia ce afiseaa submultimea corespunzatoare fiecarui numar de la 1 la 2^n-1


def submultime(x):
    contor=0
    while(x!=0):
        contor=contor+1
        if(x&1==1):
            print(contor,end=" ")
        x=x>>1
    print()

n=1<<n
for i in range(n):
    submultime(i)
"""""
#pb3 biti
'''''
n=int(input())
cn=n

#var1
nr=0
while(n!=0):
    if(n&1==1):
        nr=nr+1
    n=n>>1
print(nr)

#var2
nr=0
while(cn!=0):
    cn=cn&(cn-1)
    nr=nr+1

print(nr)
'''

#pb4 biti
''''''''''
n=int(input())
nr=0
while(n!=0):
    nr=nr+1
    n=n&(n<<1)

print(nr)
'''

#pb2 limbaj
'''
n=int(input())
x=float(input())
y=float(input())

Max=-10
zi=0
for i in range(2,n):
    dif=y-x
    if(Max<dif):
        Max=dif
        zi=i
    x=y
    y = float(input())

print ('%.2f'%Max)
print(int(y)-1)
print(int(y))
'''
6
4.25
4.05
4.25
4.48
4.30
4.40
'''

#pb3 limbaj
'''
'''
L1=int(input())
L2=int(input())

def cmmdc(a,b):
    while(a and b):
        if a>b:
            a=a%b
        else:
            b=b%a
    return a+b

CD=cmmdc(L1,L2)
#print(CD)
print("E nevoie de "," placi",sep=str((L1*L2)//(CD*CD)), end="")
print(" de dimensiune ",end=str(CD))
'''
'''

#pb4 limbaj
''
n=int(input())

Max1=int(input())
Max2=Max1
i=2
x=0
while(i<=n):
    x=int(input())
    if(x!=Max1):
        if(x>Max1):
            Max2=Max1
            Max1=x
        else:
            Max2=x

    i=i+1

if(Max1==Max2):
    print("Imposibil")
else:
    print(Max1,Max2)
'''

#pb5 limbaj
'''
a=int(input())
b=int(input())
c=int(input())
delta=(b*b)-(4*a*c)
if(delta<0):
    print("Imposibil")
elif(delta==0):
    print(str((b*(-1))/(2*a)))
else:
    x1=(-1*b+math.sqrt(delta))/(2*a)
    x2=(-1*b-math.sqrt(delta))/(2*a)
    print(x1,x2)
'''

#pb6 limbaj
'''
cifre=[]
n=int(input())
cifre.append(n%10)
n=n//10
Max=0
Min=0

while(n!=0):
    cifre.append(n % 10)
    n = n // 10

print("1pt  minim si 2pt maxim, boss")
raspuns=int(input())
if(raspuns==2):
    for i in range(9,-1,-1):
        while(i in cifre):
            Max=Max*10+i
            cifre.remove(i)

    print(Max)
else:
    for i in range(1,10,1):
        while(i in cifre):
            Min=Min*10+i
            cifre.remove(i)
    while (0 in cifre):
        Min = Min * 10
        cifre.remove(0)

    print(Min)
'''
#pb7 biti
idee1->xor cu 2^k
idee2->(pb lui vlad si toma) cx=x,x=x>>k,x=x<<k,x=cx|xg=