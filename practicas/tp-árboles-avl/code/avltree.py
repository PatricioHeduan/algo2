from algo1 import *
from linkedlist import *


class AVLTree:
    root = None


class AVLNode:
    parent = None
    leftNode = None
    rightNode = None
    key = None
    value = None
    balanceFactor = None


def bt_search(B, element):
    if B.root == None:
        return None
    else:
        return (searchR(B, B.root, element))


def searchR(B, node, element):
    j = None
    if element == node.value:
        j = (node.key)
    if node.leftNode != None and j == None:
        j = searchR(B, node.leftNode, element)
    if node.rightNode != None and j == None:
        j = searchR(B, node.rightNode, element)
    return j


def bt_deletekey(B, key):
    node = bt_access_node(B, key)
    if node == None:
        return None
    else:
        ELIMINARnode(B, node)
        return key



def ELIMINARnode(B, node):
    #Caso sin hijos
    if node.leftNode == None and node.rightNode == None:
        if node.parent.rightNode == node:
            node.parent.rightNode = None
        elif node.parent.leftNode == node:
            node.parent.leftNode = None
#Caso un solo hijo
    elif node.leftNode != None and node.rightNode == None or node.rightNode != None and node.leftNode == None:
        if node.leftNode != None and node.rightNode == None:
            if node == B.root:
                B.root = node.leftNode
            else:
                node.leftNode.parent = node.parent
                if node.parent.rightNode == node:
                    node.parent.rightNode = node.leftNode
                elif node.parent.leftNode == node:
                    node.parent.leftNode = node.leftNode
        elif node.rightNode != None and node.leftNode == None:
            if node == B.root:
                B.root = node.rightNode
            else:
                node.rightNode.parent = node.parent
                if node.parent.rightNode == node:
                    node.parent.rightNode = node.rightNode
                elif node.parent.leftNode == node:
                    node.parent.leftNode = node.rightNode


#Caso de dos hijos
    elif node.leftNode != None and node.rightNode != None:
        if node.key < B.root.key:
            Aux = Mayor_de_los_menores(B, node.leftNode)
            Mayordemenores = Aux
            ELIMINARnode(B, Aux)
            if Mayordemenores == node.leftNode:
                Mayordemenores.rightNode = node.rightNode
                Mayordemenores.leftNode = None
            else:
                Mayordemenores.rightNode = node.rightNode
                Mayordemenores.leftNode = node.leftNode
            node.rightNode.parent = Mayordemenores
            node.leftNode.parent = Mayordemenores
            Mayordemenores.parent = node.parent
            if node.parent.rightNode == node:
                node.parent.rightNode = Mayordemenores
            elif node.parent.leftNode == node:
                node.parent.leftNode = Mayordemenores
        else:
            Aux = Menor_de_los_mayores(B, node.rightNode)
            Menordelosmayores = Aux
            ELIMINARnode(B, Aux)
            if Menordelosmayores == node.rightNode:
                Menordelosmayores.leftNode = node.leftNode
                Menordelosmayores.rightNode = None
            else:
                Menordelosmayores.rightNode = node.rightNode
                Menordelosmayores.leftNode = node.leftNode
            node.rightNode.parent = Menordelosmayores
            node.leftNode.parent = Menordelosmayores
            if B.root == node:
                B.root = Menordelosmayores
            else:
                Menordelosmayores.parent = node.parent
                if node.parent.rightNode == node:
                    node.parent.rightNode = Menordelosmayores
                elif node.parent.leftNode == node:
                    node.parent.rightNode = Menordelosmayores


def Mayor_de_los_menores(B, nodo):
    if nodo.rightNode != None:
        return (Mayor_de_los_menores(B, nodo.rightNode))
    else:
        return nodo


def Menor_de_los_mayores(B, nodo):
    if nodo.leftNode != None:
        return (Menor_de_los_mayores(B, nodo.leftNode))
    else:
        return nodo


def avl_delete(B, element):
    key = bt_search(B, element)
    if key == None:
        return None
    else:
        bt_deletekey(B, key)
        calculateBalance(B)
        reBalance(B)
        return key


def reBalance(Tree):
    node = Tree.root
    if node == None:
        return None
    else:
        if node.leftNode == None and node.rightNode == None:
            return
        else:
            reBalanceR(Tree, node)


def reBalanceR(Tree, node):
    if node.rightNode != None:
        reBalanceR(Tree, node.rightNode)
    if node.leftNode != None:
        reBalanceR(Tree, node.leftNode)

    elif node.balanceFactor < -1:
        if node.rightNode.balanceFactor > 0:
            rotateRight(Tree, node.rightNode)
            rotateLeft(Tree, node)
        else:
            rotateLeft(Tree, node)
    if node.balanceFactor > 1:
        if node.leftNode.balanceFactor < 0:
            rotateLeft(Tree, node.leftNode)
            rotateRight(Tree, node)
        else:
            rotateRight(Tree, node)

    calculateBalance(Tree)
    return


def avl_insert(B, element, key):
    currentnode = B.root
    newNode = AVLNode()
    newNode.value = element
    newNode.key = key
    newNode.balanceFactor = None
    if B.root == None:
        B.root = newNode
        KEY = B.root.key
    else:
        KEY = InsertR(currentnode, newNode)
        newNode.key
    calculateBalance(B)
    reBalance(B)
    return KEY




def InsertR(currentnode, newNode):
    if newNode.key > currentnode.key:
        if currentnode.rightNode != None:
            return (InsertR(currentnode.rightNode, newNode))
        else:
            currentnode.rightNode = newNode
            newNode.parent = currentnode
            return newNode.key
    elif newNode.key < currentnode.key:
        if currentnode.leftNode != None:
            return (InsertR(currentnode.leftNode, newNode))
        else:
            currentnode.leftNode = newNode
            newNode.parent = currentnode
            return newNode.key
    elif currentnode.key == newNode.key:
        return None


def bt_access(B, key):
    node = B.root
    return (accessR(node, key))


def accessR(node, key):
    if node.key == key:

        return node.value
    elif key < node.key:
        if node.leftNode == None:
            return None
        else:
            return (accessR(node.leftNode, key))
    else:
        if node.rightNode == None:
            return None
        else:
            return (accessR(node.rightNode, key))


def bt_access_node(B, key):
    node = B.root
    return (accessR_Node(node, key))


def accessR_Node(node, key):
    if node.key == key:
        return node
    elif key < node.key:
        if node.leftNode == None:
            return None
        else:
            return (accessR_Node(node.leftNode, key))
    else:
        if node.rightNode == None:
            return None
        else:
            return (accessR_Node(node.rightNode, key))


def bt_update(B, element, key):
    node = B.root
    nodeactualizado = bt_access_node(B, key)
    if nodeactualizado != None:
        nodeactualizado.value = element
        return key
    else:
        return None


def imprimirarbol(B, node):
    print("____________________________________________________________")
    if node == B.root:
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\"")
        print("()La raiz con key {", node.key, "} con element[", node.value,
              "]")
    else:
        print("ººdesde key {", node.key, "} con element [", node.value,
              " ]con parent=", node.parent.key)
    imprimirsubnodes(B, node)
    if node.leftNode != None:
        imprimirarbol(B, node.leftNode)
    if node.rightNode != None:
        imprimirarbol(B, node.rightNode)


def imprimirsubnodes(B, node):
    if node.leftNode != None:
        print("\ node de la izquierda de key {", node.leftNode.key,
              "} de element", node.leftNode.value)
    else:
        print("\ no hay node de la izquierda")
    if node.rightNode != None:
        print("/ node de la derecha key {", node.rightNode.key, "} de element",
              node.rightNode.value)
    else:
        print("/ no hay node de la derecha")


#AVL WEAS


def calculateBalance(Tree):
    calculateBalanceRec(Tree, Tree.root)


def calculateBalanceRec(Tree, node):
    profder = 0
    profizq = 0
    if node.rightNode != None:
        profder = calculateBalanceRec(Tree, node.rightNode)
    if node.leftNode != None:
        profizq = calculateBalanceRec(Tree, node.leftNode)
    if node.rightNode == None and node.leftNode == None:
        node.balanceFactor = 0
        return 1
    node.balanceFactor = profizq - profder

    if profizq <= profder:
        return profder + 1
    else:
        return profizq + 1


#rotates
def rotateLeft(Tree, node):
    rootAux = node.rightNode
    if rootAux.leftNode == None:
        node.rightNode = None
        rootAux.leftNode = node
        if node.parent == None:
            Tree.root = rootAux
            rootAux.parent = None
        else:
            rootAux.parent = node.parent
            linkParent(node, rootAux)
        node.parent = rootAux

    else:
        nodeAux = rootAux.leftNode
        node.rightNode = nodeAux
        nodeAux.parent = node
        rootAux.leftNode = node
        if node.parent == None:
            Tree.root = rootAux
            rootAux.parent = None
        else:
            rootAux.parent = node.parent
            linkParent(node, rootAux)

        node.parent = rootAux
    return rootAux


def rotateRight(Tree, node):
    rootAux = node.leftNode
    if rootAux.rightNode == None:
        node.leftNode = None
        rootAux.rightNode = node
        if node.parent == None:
            Tree.root = rootAux
            rootAux.parent = None
        else:
            rootAux.parent = node.parent
            linkParent(node, rootAux)
        node.parent = rootAux
    else:
        nodeAux = rootAux.rightNode
        node.leftNode = nodeAux
        nodeAux.parent = node
        rootAux.rightNode = node
        if node.parent == None:
            Tree.root = rootAux
            rootAux.parent = None
        else:
            rootAux.parent = node.parent
            linkParent(node, rootAux)
        node.parent = rootAux
    return rootAux


def linkParent(node, newRoot):
    if node.parent.rightNode == node:
        node.parent.rightNode = newRoot
    elif node.parent.leftNode == node:
        node.parent.leftNode = newRoot

def getDepth(Tree, node):
    if node == None:
        return 0
    else:
        leftLength = getDepth(Tree, node.leftNode)
        rightLength = getDepth(Tree, node.rightNode)
        if leftLength > rightLength:
            return leftLength + 1
        return rightLength + 1
        

#function that returns a node pointer to the node who has the profsearch below it
def checkLeftProf(Tree, node,prof):
    if node == None:
        return None
    else:
        depht = getDepth(Tree, node)
        if depht != prof:
            return checkLeftProf(Tree,node.leftNode, prof)
        elif depht == prof:
            return node

def putXandA(Tree, node, Xkey, Atree):
    xNode = AVLNode()
    xNode.key = Xkey
    node.Parent.leftNode= xNode
    node.Parent = xNode
    if node.Parent ==Tree.root:
        Tree.root = xNode
    xNode.leftNode = Atree.root
    xNode.rightNode = node

def A_X_B(Atree, Xkey, Btree):
    maxADepth = getDepth(Atree,Atree.root)
    maxBDepth = getDepth(Btree,Btree.root)
    print(maxADepth)
    print(maxBDepth)
    if maxADepth >= maxBDepth:
        NewTree = AVLTree()
        avl_insert(NewTree, Xkey, Xkey)
        NewTree.root.leftNode = Atree.root
        NewTree.root.rightNode = Btree.root
        Atree.root.parent = NewTree.root
        Btree.root.parent = NewTree.root
        Atree.root = None
        Btree.root = None
        return NewTree
    nodePivotB = checkLeftProf(Btree, Btree.root, maxADepth)
    print(nodePivotB.key)
    if nodePivotB == None:
        return None
    putXandA(Btree,nodePivotB,Xkey,Atree)   
    return Btree
