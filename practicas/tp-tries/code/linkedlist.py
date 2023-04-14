import random
class Node:
  value=None
  nextNode=None
class LinkedList:
  head=None


def ImprimirLista(L):
  currentnode=L.head
  while (currentnode!=None):
    print (currentnode.value,",", end= " ")
    currentnode=currentnode.nextNode
  print("")

def add(L,element):
  Nodo=Node()
  Nodo.value=element
  Nodo.nextNode=L.head
  L.head=Nodo


def Azar(L,m):
  for i in range (m):
    add(L,random.randint(0, 20))
  return L


def length(L):
  currentnode=L.head
  Long=0
  while (currentnode!=None):
    Long=Long+1
    currentnode=currentnode.nextNode
  return Long


def search(L,element):
  currentnode=Node()
  currentnode=L.head
  Position=0
  noencontrado=False
  if length(L)==0:
    noencontrado=True
  while(currentnode!=None):
    if (currentnode.value==element):
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
  NuevoNodo.value=element
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
        currentnode.value=currentnode.nextNode.value
      if i==((length(L)-2)):
        currentnode.nextNode=None
      currentnode=currentnode.nextNode
  return Pos


def access(L,Position):
  currentnode=Node()
  currentnode=L.head
  if Position<0 or (Position>=(length(L))):
    return None
  Pos=0
  while Pos<=(length(L)-1):
    if Pos==Position:
      return currentnode.value
    currentnode=currentnode.nextNode
    Pos=Pos+1


def update (L,element,position):
 currentnode=Node()
 currentnode=L.head
 if position<0 or position>=length(L):
   return None
 else:
    Pos=0
    while Pos<(length(L)):
        if Pos==position:
          currentnode.value=element
        currentnode=currentnode.nextNode
        Pos=Pos+1
 return position

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