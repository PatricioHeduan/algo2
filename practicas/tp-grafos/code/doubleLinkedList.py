from dictionary import *
from algo1 import *
from linkedlist import *

class doubleLinkedList:
	head=None
class doubleNode:
	value=None
	key=None
	nextNode=None
	prevNode=None
	redirect=None
	deleted=False

def dependentList(D):
	L=doubleLinkedList()
	for i in range (len(D)-1,-1,-1):
		node=doubleNode()
		node.redirect=LinkedList()
		D[i]=node
		addNode(L,node)
	print(length(L))
	return L


def addNode(L,node):
	node.nextNode=L.head
	if L.head!=None:
		L.head.prevNode=node
	L.head=node
		

def createList(N,L):
	for i in range (N):
		add_double(L,None,None)


def add_double(L,value,key):
	newNode=doubleNode()
	newNode.value=value
	newNode.key=key
	if L.head==None:
		L.head=newNode
	else:
		newNode.nextNode=L.head
		L.head.prevNode=newNone
		L.head=newNode
		
def dictInsertOpen(D,L,key,value,H):
	n=H(D,key)
	if D[n].key==None or D[n].deleted!=False:
		D[n].key=key
		D[n].value=value
		if n==0:
			L.head=D[n].nextNode
		else:
			D[n].prevNode.nextNode=D[n].nextNode
			if n<len(D)-1:
				D[n].nextNode.prevNode=D[n].prevNode
			D[n].nextNode=L.head
			D[n].prevNode=L.head.prevNode
			if L.head.prevNode!=None:
				L.head.prevNode.nextNode=D[n]
			L.head.prevNode=D[n]
	else:
		L.head.value=value
		L.head.key=key
		add(D[n].redirect,L.head)
		if L.head.nextNode!=None:
			L.head=L.head.nextNode
			
def dictDeleteOpen(D,L,key,H):
	n=H(D,key)
	ImprimirCola(D[n].redirect)
	if D[n].key==key:
		putNextHead(D[n],L)
		D[n].key=None
		D[n].value=None
		D[n].deleted=True
	else:
		nodoDel=delete(D[n].redirect,key)
		print("nodoeliminado",nodoDel.key)
		putNextHead(nodoDel,L)
		nodoDel.key=None
		nodoDel.value_L=None
	
def putNextHead(node,L):
	node.nextNode=L.head.nextNode
	node.prevNode=L.head
	if L.head.nextNode!=None:
		L.head.nextNode.prevNode=node
	L.head.nextNode=node
	
	
	
def printDictionaryOpen(D):
	for i in range (len(D)):
		print (i,"->",end="")
		if D[i]!=None:
			print(D[i].key)
		else:
			print (None)
		
