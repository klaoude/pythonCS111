import math
from decimal import Decimal, getcontext

def somme(tableau):
    ret = 0
    for i in tableau:
        ret += i
    return ret

def getMax(tableau):
    max = 0
    for i in tableau:
        if(i > max):
            max = i
    return max

def getMaxPos(tableau):
    pos = 0
    max = getMax(tableau)
    for i in tableau:
        if(i == max):
            return pos
        pos+=1

def getMaxPosLast(tableau):
    pos = 0
    max = getMax(tableau)
    for i in tableau:
        pos+=1
        if(i == max and pos-1 != tableau[getMaxPos(tableau)]):
            return pos-1

def allPos(tableau):
    ret = True
    for i in tableau:
        if(i < 0):
            ret = False
            break
    return ret

def isInc(tableau):
    ret = True
    for i in range(len(tableau) - 1):
        if(tableau[i] > tableau[i+1]):
            ret = False
            break
    return ret

def isIn(x, t):
    for i in t:
        if(i == x):
            return True
    return False

def isInDicho(x, t):
    """
    Complexité : 0(log(len(t)))
    """
    found = False
    start = 0
    end = len(t)
    mid = 0
    while((end - start) > 1):
        mid = int((start + end)/2)
        if(t[mid] == x):
            return True
        if(t[mid] > x):
            end = mid
        else:
            start = mid
    return False            

def isSym(mat):
    for i in range(len(mat[0])):
        for j in range(len(mat[i])):
            if(mat[i][j] != mat[j][i]):
                return False
    return True

def transpo(mat):
    ret = []
    x = len(mat[0])
    y = len(mat)
    for i in range(x):
        ret.append([])

    for i in range(x):
        for j in range(y):
            ret[i].append(mat[j][i])

    return ret

"""
Exo sur le rendu de monnaie
"""
def renduDeMonnaie(montantEntre, prix):
    """
    Decimal fix found : http://stackoverflow.com/questions/14120340/python-error-in-basic-subtraction
    """
    def fixDecimal():
        Decimal(1) - Decimal(0.8)
        getcontext().prec = 3

    fixDecimal()
    aRendre = float(Decimal(montantEntre) - Decimal(prix))
    tab = [2, 1, .5, .2, .1, .05, .02, .01]
    rendu = []
    ret = []
    if(aRendre <= 0):
        return 0
    for i in tab:
        while(aRendre >= i):
            rendu.append(i)
            aRendre -= i
    
    def numInTab(num, tab):
        ret = 0
        for i in tab:
            if(i == num):
                ret += 1
        return ret

    for i in tab:
        ret.append(numInTab(i, rendu))

    stri = "Il faut rendre "
    for i in range(len(ret)):
        if(ret[i] != 0):
            stri += str(ret[i]) + " pièce(s) de " + ((str(tab[i]) + " euros") if tab[i] >= 1 else (str(tab[i] * 100)) + " cens ")
    print(stri)

tableau = [4, 5, 2.7, 3.5, 1337]
mat = [[2, 4, 6], [4, 0, 10]]

renduDeMonnaie(5.43, 1.73)