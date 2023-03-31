from linkedlist import *


def OrdenPorIzquierda(L, desde):
    longituds2 = length(L) // 2
    mitad = access(L, length(L) // 2)
    cnode = L.head
    c = 0
    for i in range(longituds2):
        if cnode.value < mitad:
            c += 1
        cnode = cnode.nextNode
    if c < longituds2 // 2:
        if buscarmayor(L, mitad, desde) != None:
            mayor = buscarmayor(L, mitad, desde)
            ubicacionmayor = search(L, mayor)
            L = swichValores(L, longituds2, ubicacionmayor)
            OrdenPorIzquierda(L, desde + 1)
    if c > longituds2 // 2:
        if buscarmenor(L, mitad, desde) != None:
            menoraux = buscarmenor(L, mitad, desde)
            ubicacionmenor = search(L, menoraux)
            L = swichValores(L, longituds2, ubicacionmenor)
            OrdenPorIzquierda(L, desde + 1)


def buscarmayor(L, n, m):
    for i in range(m, length(L) // 2):
        if access(L, i) > n:
            return access(L, i)
    return None


def buscarmenor(L, n, m):
    for i in range(m, length(L) // 2):
        if access(L, i) < n:
            return access(L, i)
    return None


def swichValores(L, n, m):
    pr = access(L, n)
    seg = access(L, m)
    update(L, pr, m)
    update(L, seg, n)
    return L


def Contiene_Suma(A, n):
    cnode = A.head
    for i in range(length(A)):
        cnode2 = cnode.nextNode
        for j in range(i + 1, length(A)):
            if (cnode.value + cnode2.value) == n:
                return True
            cnode2 = cnode2.nextNode
        cnode = cnode.nextNode
    return False
