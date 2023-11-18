#Basic - Print all integers from 0 to 150.
for i in range(0,151,1):
    print(i)
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(0,1001,5) :
    print(i)
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
for i in range(0,101):
    print(i)
    if i%5==0:
        print("Coding")
    if i%10==0 :
            print("CodingDojo")
    else :
        print(i)             
#Waouh. That Sucker's Huge - Ajoutez des nombres entiers impairs de 0 à 500 000 et imprimez la somme finale.

for i in range(500000):
    if i%2 ==0:
        print(i)
#Compte à rebours par quatre : imprimez des nombres positifs à partir de 2018, en comptant à rebours par quatre.
for x in range (2018,-1,-4):
    print(x)

#Compteur flexible - Définissez trois variables : lowNum, highNum, mult. En commençant par lowNum et en passant par highNum, imprimez uniquement les entiers multiples de mult. Par exemple, si lowNum=2, highNum=9 et mult=3, la boucle doit imprimer 3, 6, 9 (sur des lignes successives)
lowNum=2
highNum=9
mult=3
for i in range (lowNum,highNum,mult):
    if i%mult==0:
        print(i)


