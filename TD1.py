##Code de Clément Étoré

from math import *

##Problème 16

def sum_puiss_2(a):
    """fonction qui fait la somme des chiffres de 2^a"""
    b=2**a
    somme=0
    i=0 #compteur
    while b>0:
        somme+=b%10
        b=b//10
    return somme

assert sum_puiss_2(15)==26
print("Problème 16 : ",sum_puiss_2(1000),"\n")

##Problème 22

#Impossible d'ouvrir un fichier à partir de son chemin sur mon ordinateur sur Windows 10.
print("Problème 22 : Error","\n")

##Problème 55

def miroir(a):
    """int->int : retourne le miroir du nombre a"""
    m=0
    l=int(log10(a))+1 #longueur de l'entier
    for i in range (1,l+1):
        m=m*10
        m+=a%10
        a=a//10
    return m

assert miroir(1325)==5231

def palyndrome(a):
    """int->bool : vérifie si un nombre est un palyndrome et renvoie True si oui"""
    if a==miroir(a) :
        return True
    else :
        return False

assert palyndrome(1331)==True

def nb_Lychrel(a):
    """int->bool : vérifie si a est un nombre de Lychrel"""
    i=1 #compteur de nombre d'itérations, il ne doit pas excéder 50.
    while i<=50 :
        a=a+miroir(a)
        if palyndrome(a)==True:
            return False
        i+=1
    return True

assert nb_Lychrel(349)==False
assert nb_Lychrel(196)==True

def nb_lychrel_jusqua(a):
    """donne le nombre de nombre de Lychrel jusqua a"""
    cpt=0 #compteur sachant que 0 n'est pas un nombre de Lychrel.
    for i in range (1,a):
        if nb_Lychrel(i)==True:
            cpt+=1
    return cpt

assert nb_lychrel_jusqua(197)==1
print("Problème 55 : ",nb_lychrel_jusqua(10000))