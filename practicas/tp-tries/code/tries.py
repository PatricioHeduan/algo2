class Trie:
    root = None


class TrieNode:
    nextNode = None
    parent = None
    children = None
    key = None
    isEndOfWord = False


def insertTrie(T, element):
    if T.root == None:
        T.root = TrieNode()
        T.root.isEndOfWord=False
        T.root.key=""
        T.root.parent=None
    insertTrieR(T,T.root,element,0)   
        
def insertTrieR(T,node,element,i):
    if i == len(element):
        node.isEndOfWord=True 
        return
    currentNode = node.children
    if currentNode == None:
       return insertOnlyDown(node,element,i)
    while currentNode != None:
        if currentNode.key == element[i]:
            return insertTrieR(T,currentNode,element,i+1)
        if currentNode.nextNode ==None:
            newNode = createTrieNode(element[i])
            currentNode.nextNode =newNode
            newNode.parent = currentNode.parent
            return insertOnlyDown(newNode,element,i+1)
        currentNode=currentNode.nextNode

     
def insertOnlyDown(parent,element,i):
    if i==len(element):
        parent.isEndOfWord=True
        return
    newNode = createTrieNode(element[i])
    newNode.parent = parent
    parent.children = newNode
    insertOnlyDown(newNode,element,i+1)


def createTrieNode(key):
    newNode = TrieNode()
    newNode.key = key
    return newNode
        
    

def insertSon(Trie, node, element, c):
    node.children = TrieNode()
    node.children.key = element[c]
    node.children.parent = node
    if c == (len(element) - 1):
        node.children.isEndOfWord = True
    else:
        insertSon(Trie, node.children, element, c + 1)


def SearchTrie(T, element):
    if T.root == None:
        return None
    else:
        return SearchTrieR(T, T.root.children, element, 0)


def SearchTrieR(T, node, element, c):
    if node.nextNode == None:
        if node.key != element[c]:
            return False
        else:
            if len(element) - 1 == c:
                if node.isEndOfWord:
                    return True
                else:
                    return False
            else:
                if node.children == None:
                    return False
                else:
                    return SearchTrieR(T, node.children, element, c + 1)

    else:
        if node.key != element[c]:
            return SearchTrieR(T, node.nextNode, element, c)
        else:
            if len(element) - 1 == c:
                if node.isEndOfWord:
                    return True
                else:
                    return False
            else:
                if node.children == None:
                    return False
                else:
                    return SearchTrieR(T, node.children, element, c + 1)


def delete(T, element):
    if T.root == None:
        return None
    else:
        node = SearchNode(T, element)
        if SearchTrie(T, element):
            return deleteR(T, node, element, 0)
        else:
            return False


def deleteR(T, node, element, c):
    parentN = node.parent
    if node.isEndOfWord and node.children != None:
        node.isEndOfWord = False
        return True
    if parentN == T.root or parentN.isEndOfWord or parentN.children != node or node.nextNode != None:
        linksDeleteR(node)
        return True
    linksDeleteR(node)
    return deleteR(T, parentN, element, c)


def linksDeleteR(node):
    if node.parent.children == node:
        if node.nextNode != None:
            node.parent.children = node.nextNode
            node.nextNode = None
        else:
            node.parent.children = None
    else:
        nodoaux = node.parent.children
        while nodoaux.nextNode != None:
            if nodoaux.nextNode == node:
                nodoaux.nextNode = node.nextNode
                node.nextNode = None
                break
            nodoaux = nodoaux.nextNode

    node.parent = None
    node.isEndOfWord = None


#SearchAuxiliar
def SearchNodeTrie(T, element):
    if T.root == None:
        return None
    else:
        return SearchRNodeTrie(T, T.root.children, element, 0)


def SearchRNodeTrie(T, node, element, c):
    if node.nextNode == None:
        if node.key != element[c]:
            return False
        else:
            if len(element) - 1 == c:
                if node.isEndOfWord:
                    return node
                else:
                    return False
            else:
                if node.children == None:
                    return False
                else:
                    return SearchRNodeTrie(T, node.children, element, c + 1)

    else:
        if node.key != element[c]:
            return SearchRNodeTrie(T, node.nextNode, element, c)
        else:
            if len(element) - 1 == c:
                if node.isEndOfWord:
                    return node
                else:
                    return False
            else:
                if node.children == None:
                    return False
                else:
                    return SearchRNodeTrie(T, node.children, element, c + 1)


def printTries(Trie):
    print("Imprimimos Trie")
    if Trie.root == None:
        print("Está vacio")
    else:
        printrecursivo(Trie.root.children, "")


def printrecursivo(node, palabra):
    if node == None:
        return
    else:
        if node.isEndOfWord:
            print(palabra+node.key)
        printrecursivo(node.nextNode,palabra)
        printrecursivo(node.children,palabra+node.key)


def lengthT(L, N):
    currentnode = N
    Long = 0
    while (currentnode != None):
        Long = Long + 1
        currentnode = currentnode.nextNode
    return Long


def searchPtoN(T, p, n):
    if T == None or n < 1 or (len(p) > n):
        print(len(p))
        return False
    L = LinkedList()
    searchPtoNRec(T, T.root.children, p, n, p, False, L)
    return L


def searchPtoNRec(T, node, p, n, con, i, L):
    cont = 0
    nodea = node
    while nodea.children != None:
        if len(p) == 0:
            i = True
            break
        elif cont == len(p):

            i = True
            break
        elif p[cont] == nodea.key:
            cont += 1
            nodea = nodea.children
        elif p[cont] != nodea.key:
            if nodea.nextNode == None:
                break
            else:
                searchPtoNRec(T, nodea.nextNode, substr(p, cont, len(p)),
                              n - cont, con, False, L)
                break

    if i:
        countsonsPtoN(T, nodea, con, n - 1, cont, L)


def countsonsPtoN(T, node, p, n, cont, L):
    conta = cont
    while node != None:
        if node.nextNode != None:
            countsonsPtoN(T, node.nextNode, p, n, conta, L)
        p = p + node.key
        if (conta < n):
            conta += 1
            node = node.children
        elif conta == n:
            if node.isEndOfWord:
                add(L, p)
                return
            else:
                return
        else:
            return


def searchWordsTrie(T):
    L = LinkedList()
    searchWordsTrieR(T, T.root.children, L, "")
    return L


def searchWordsTrieR(T, node, L, w):
    if node.nextNode != None:
        searchWordsTrieR(T, node.nextNode, L, w)
    w = w + node.key
    if node.isEndOfWord:
        add(L, w)
    if node.children != None:
        searchWordsTrieR(T, node.children, L, w)


def isTrie1inTrie2(T1, T2):
    cond1 = True
    cond2 = True
    L1 = searchWordsTrie(T1)
    L2 = searchWordsTrie(T2)
    c1 = L1.head
    c2 = L2.head
    while c1 != None:
        if SearchTrie(T2, c1.value_L):
            c1 = c1.nextNode
        else:
            cond1 = False
            break
    while c2 != None:
        if SearchTrie(T1, c2.value_L):
            c2 = c2.nextNode
        else:
            cond2 = False
            break
    return (cond1 or cond2)


def haveInverses(T):
    L1 = searchWordsTrie(T)
    cnode = L1.head
    while cnode != None:
        S = inverseString(cnode.value_L)
        print(cnode.value_L, "inv", S)
        if search(L1, S) is not None:
            return True
        cnode = cnode.nextNode
    return False


def inverseString(S):
    returnString = ""
    for i in range(len(S) - 1, -1, -1):
        returnString = returnString + S[i]
    return returnString


def autoComplete(T, string):
    return autoCompleteR(T, T.root.children, string, False)


def autoCompleteR(T, node, p, i):
    cont = 0
    nodea = node
    while nodea.children != None:
        if len(p) == 0:
            i = True
            break
        elif cont == len(p):
            i = True
            break
        elif p[cont] == nodea.key:
            cont += 1
            nodea = nodea.children
        elif p[cont] != nodea.key:
            if nodea.nextNode == None:
                break
            else:
                return autoCompleteR(T, nodea.nextNode,substr(p, cont, len(p)), False)
                break
    if i:
        returnString = ""
        while nodea != None:
            print(returnString)
            if nodea.nextNode != None:
                return returnString
            else:
                returnString = returnString + nodea.key
                nodea = nodea.children
        return returnString
    else:
        return Noneerain
