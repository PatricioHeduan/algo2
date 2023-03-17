
class PriorityQueue:
    head=None

class PriorityNode:
    value_L=None
    nextNode=None
    priority=None

class Node:
  value_L=None
  nextNode=None

class LinkedList:
  head=None
def ImprimirListasDeListas(L):
  currentnode=L.head
  while currentnode!=None:
    currentnode2=currentnode.value_L.head
    print("[",end=" ")
    while currentnode2!=None:
      print (currentnode2.value_L.value,end=" ")
      currentnode2=currentnode2.nextNode
    print("]")
    currentnode=currentnode.nextNode



def ImprimirCola(L):
  currentnode=L.head
  print("[",end="")
  while (currentnode!=None):
    print (currentnode.value_L,end=" ")
    currentnode=currentnode.nextNode
  print("]")

def ImprimirCola_A(L):
  currentnode=L.head
  print("[",end="")
  while (currentnode!=None):
    print (currentnode.value_L.value,end=" ")
    currentnode=currentnode.nextNode
  print("]")

def ImprimirPila(L):
  currentnode=L.head
  for i in range (length(L)):
      print (currentnode.value_L)
      currentnode=currentnode.nextNode

def add_priority(L,element,priority):
  Nodo=PriorityNode()
  Nodo.value_L=element
  Nodo.priority=priority
  Nodo.nextNode=L.head
  L.head=Nodo


def length(L):
  currentnode=L.head
  Long=0
  while (currentnode!=None):
    Long=Long+1
    currentnode=currentnode.nextNode
  return Long


def search_priority(L,prioridad):
  currentnode=PriorityNode()
  currentnode=L.head
  Position=0
  noencontrado=False
  if length(L)==0:
    noencontrado=True
  while(currentnode!=None):
    if (currentnode.priority==prioridad):
      return Position
    else:
      noencontrado=True
    Position=Position+1
    currentnode=currentnode.nextNode
  if (noencontrado==True):
   Position=None
  return Position



def insert_priority(L,element,priority,position):
  currentnode=PriorityNode()
  currentnode=L.head
  if position<0 or position>length(L):
    return None
  else:
    if position==0:
      add_priority(L,element,priority)
      return 0
  currentnode=L.head
  NuevoNodo=PriorityNode()
  NuevoNodo.value_L=element
  NuevoNodo.priority=priority
  Pos=0
  while currentnode!=None:
    if Pos==position-1:
      NuevoNodo.nextNode=currentnode.nextNode    
      currentnode.nextNode=NuevoNodo
      currentnode.nextNode.nextNode=NuevoNodo.nextNode

    currentnode=currentnode.nextNode
    Pos=Pos+1
  return position


def delete_priority (L,position):
  currentnode=PriorityNode()
  currentnode=L.head
  i=-1
  X=access_priority(L,position)
  if length(L)==1:
    L.head=None
  if position==None:
    return None
  else:
    while currentnode!=None:
      i=i+1
      if i>=position and i<((length(L))):
        if currentnode!=None and currentnode.nextNode!=None:
          currentnode.value_L=currentnode.nextNode.value_L
          currentnode.priority=currentnode.nextNode.priority
      if i==((length(L)-2)):
        currentnode.nextNode=None
      currentnode=currentnode.nextNode
  return X


def access_priority(L,Position):
  currentnode=PriorityNode()
  currentnode=L.head
  if Position<0 or (Position>=(length(L))):
    return None
  Pos=0
  while Pos<=(length(L)-1):
    if Pos==Position:
      return currentnode.value_L
    currentnode=currentnode.nextNode
    Pos=Pos+1


def update (L,element,position):
 currentnode=PriorityNode()
 currentnode=L.head
 if position<0 or position>=length(L):
   return None
 else:
    Pos=0
    while Pos<(length(L)):
        if Pos==position:
          currentnode.value_L=element
        currentnode=currentnode.nextNode
        Pos=Pos+1
 return position



def add(L,element):
  Nodo=Node()
  Nodo.value_L=element
  Nodo.nextNode=L.head
  L.head=Nodo
def add_nodo(L,node):
  Nodo=Node()
  Nodo.value=node.value
  Nodo.nextNode=L.head
  L.head=Nodo

def length(L):
  currentnode=L.head
  Long=0
  while (currentnode!=None):
    Long=Long+1
    currentnode=currentnode.nextNode
  return Long

def search_Node(L,element):
  currentnode=Node()
  currentnode=L.head
  Position=0
  noencontrado=False
  if length(L)==0:
    noencontrado=True
  while(currentnode!=None):
    if (currentnode==element):
      return Position
    else:
      noencontrado=True
    Position=Position+1
    currentnode=currentnode.nextNode
  if (noencontrado==True):
   Position=None
  return Position
def search(L,element):
  currentnode=Node()
  currentnode=L.head
  Position=0
  noencontrado=False
  if length(L)==0:
    noencontrado=True
  while(currentnode!=None):
    if (currentnode.value_L==element):
      return Position
    else:
      noencontrado=True
    Position=Position+1
    currentnode=currentnode.nextNode
  if (noencontrado==True):
   Position=None
  return Position



def insert(L,element,position):
  currentnode=Node()
  currentnode=L.head
  if position<0 or position>length(L):
    return None
  else:
    if position==0:
      add(L,element)
      return 0
  currentnode=L.head
  NuevoNodo=Node()
  NuevoNodo.value_L=element
  Pos=0
  while currentnode!=None:
    if Pos==position-1:
      NuevoNodo.nextNode=currentnode.nextNode    
      currentnode.nextNode=NuevoNodo
      currentnode.nextNode.nextNode=NuevoNodo.nextNode

    currentnode=currentnode.nextNode
    Pos=Pos+1
  return position
def insert_node(L,node,position):
  currentnode=Node()
  currentnode=L.head
  if position<0 or position>length(L):
    return None
  else:
    if position==0:
      add_nodo(L,node)
      return 0
  currentnode=L.head
  NuevoNodo=Node()
  NuevoNodo.value=node.value
  Pos=0
  while currentnode!=None:
    if Pos==position-1:
      NuevoNodo.nextNode=currentnode.nextNode    
      currentnode.nextNode=NuevoNodo
      currentnode.nextNode.nextNode=NuevoNodo.nextNode

    currentnode=currentnode.nextNode
    Pos=Pos+1
  return position


def delete (L,element):
  currentnode=Node()
  currentnode=L.head
  Pos=search(L,element)
  i=-1
  
  if Pos==None:
    return None
  else:
    while currentnode!=None:
      i=i+1
      if i>=Pos and i<((length(L))):
        currentnode.value_L=currentnode.nextNode.value_L
      if i==((length(L)-2)):
        currentnode.nextNode=None
      currentnode=currentnode.nextNode
      
  return Pos

def delete_position (L,position):
  currentnode=Node()
  currentnode=L.head
  i=-1
  X=access(L,position)
  if length(L)==1:
    L.head=None
  if position==None:
    return None
  else:
    while currentnode!=None:
      i=i+1
      if i>=position and i<((length(L))):
        currentnode.value_L=currentnode.nextNode.value_L
      if i==((length(L)-2)):
        currentnode.nextNode=None
      currentnode=currentnode.nextNode
  return X

def access(L,Position):
  currentnode=Node()
  currentnode=L.head
  if Position<0 or (Position>=(length(L))):
    return None
  Pos=0
  while Pos<=(length(L)-1):
    if Pos==Position:
      return currentnode.value_L
    currentnode=currentnode.nextNode
    Pos=Pos+1
  
def access_node(L,Position):
  currentnode=Node()
  currentnode=L.head
  if Position<0 or (Position>=(length(L))):
    return None
  Pos=0
  while Pos<=(length(L)-1):
    if Pos==Position:
      return currentnode
    currentnode=currentnode.nextNode
    Pos=Pos+1

def invertirLista(L):
  Inversa=LinkedList()
  Icnode=Inversa.head
  longitud=length(L)
  for i in range ((longitud-1),-1,-1):
    nodoL=access(L,i)
    insert(Inversa,nodoL,(length(Inversa)))
  return Inversa


      
def imprimirarrays(A):
  print("[",end="")
  for i in range (len(A)):
    print(A[i],end=" ")
  print("]")


def swap(L,origin, destiny):
    if destiny < origin: #Si el origin es mayor al destino intercambio valores
        vuelta = origin
        cambio = destiny
        origin = cambio
        destiny = vuelta
    if origin == destiny:
        return None
    punteroorigin = access_node(L,origin)
    punterodestiny = access_node(L,destiny)
    antdestiny = access_node(L,destiny-1)
    nextorigin = punteroorigin.nextNode
    if origin == 0 and destiny == 1:
        punteroorigin.nextNode = punterodestiny.nextNode
        punterodestiny.nextNode = punteroorigin
        L.head = punterodestiny
        return True
    if destiny - origin == 1: #Si los nodos estan al lado
        anteriororigin = access_node(L,origin-1)

        punteroorigin.nextNode = punterodestiny.nextNode
        punterodestiny.nextNode = nextorigin
        anteriororigin.nextNode = punterodestiny
        nextorigin.nextNode =punteroorigin
        return True
    if destiny == length(L)-1 and origin != 0: #si destino es el final 
        anteriororigin = access_node(L,origin-1)
        punteroorigin.nextNode = None
        punterodestiny.nextNode = nextorigin
        antdestiny.nextNode = punteroorigin
        anteriororigin.nextNode = punterodestiny
    if origin != 0 and destiny != length(L) -1 : #si el origen es distinto de cero y no es la posicion final
        anteriororigin = access_node(L,origin-1)

        punteroorigin.nextNode = punterodestiny.nextNode
        punterodestiny.nextNode = nextorigin
        anteriororigin.nextNode = punterodestiny
        antdestiny.nextNode =punteroorigin
    if origin == 0: #Si el origen esta en 0, la logica cambia
        punteroorigin.nextNode = punterodestiny.nextNode
        punterodestiny.nextNode = nextorigin
        antdestiny.nextNode = punteroorigin
        L.head = punterodestiny
        