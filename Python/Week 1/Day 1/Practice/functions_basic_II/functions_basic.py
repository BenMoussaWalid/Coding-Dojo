def condawn(num):
    list=[]
    for i in range ( num,-1,-1):
        list.append(i)
    return list      
def list(a,b):
    print(a)
    return b
def list():
    return list[0]+len(list)
print(list[1,2,4,7])
def deuxval(list):
    if len(list) < 2 :
        return False
    newlist =[]
    for i in range (0,len(list)):
        if list[i]>list[1] :
            newlist.append(list(i))
    print(len(newlist))
    return newlist        
def langeur(taille,valeur):
    list=[]
    for i in range (0,taille):
        list.append(valeur)
    return list
print(langeur (5,7))
