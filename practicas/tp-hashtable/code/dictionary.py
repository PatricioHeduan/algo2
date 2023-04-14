from algo1 import *
from linkedlist import *

		
	

class dictionary:
	head=None
class dictionaryNode:
	key=None
	value=None
	nextNode=None

def HashCodPost(D,key):
	return (ord(key[0]) -65)

def HashInt(D,key):
	modl=len(D)
	return key%len(D)
def HashAscii(D,key):
	n=0
	for i in range (len(key)):
		n=n+(ord(key[i])-48)
	modl=len(D)
	return n % modl

def insert_Dict(D,key,value,H):
	if search_Dict(D,key,H)!=None:
		return None
	newKey=H(D,key)
	if newKey==None:
		return None
	
	newNode=dictionaryNode()
	newNode.value=value
	newNode.key=key
	
	if D[newKey]==None:
		D[newKey]=dictionary()
		D[newKey].head=newNode
	else:
		add_nodo(D[newKey],newNode)
		return D
	
def search_Dict(D,key,H):
	searchkey=H(D,key)
	if D[searchkey]==None:
		return None
	else:
		node=D[searchkey].head
		while node!=None:
			if node.key==key:
				return node.value
			else:
				node=node.nextNode
		return None
		
		
		
def delete_Dict(D,key,H):
	if search_Dict(D,key,H)==None:
		return
	newKey=H(D,key)
	node=D[newKey].head
	prevNode=None
	while node!=None:
		print(node.key)
		if node.key==key:
			if node==D[newKey].head:
				if node.nextNode==None:
					D[newKey]=None
				else:
					D[newKey].head = node.nextNode
			else:
				if node.nextNode==None:
					prevNode.nextNode=None
				else:
					prevNode.nextNode=node.nextNode
			break
		else:
			if prevNode==None:
				prevNode=node
			else:
				prevNode=prevNode.nextNode
			node=node.nextNode
	return D
			
				
		
		
def EsPermutacion(D,S1,S2):
	if len(S1)!=len(S2):
		return False
#	D=Array((len(S1)),dictionary())
	for i in range (len(S1)):
		ch=S1[i]
		insert_Dict(D,ch,ch)
	printDictionary(D)
	for i in range (len(S1)):
		print(S2[i])
		printDictionary(D)
		if search_Dict(D,S2[i])!=None:
			delete_Dict(D,S2[i])
		else:
			return False
	return True

		
def add_nodo(L,node):
	Nodo=dictionaryNode()
	Nodo.value=node.value
	Nodo.key=node.key
	Nodo.nextNode=L.head
	L.head=Nodo
		
		
def printDictionary(D):
	for i in range (len(D)):
		print (i," ",end="")
		if D[i]!=None:
			ImprimirKeyList(D[i])
		else:
			print (None)
		
		
def ImprimirKeyList(L):
	currentnode=L.head
	print("[",end="")
	while (currentnode!=None):
	    print (currentnode.value,end=", ")
	    currentnode=currentnode.nextNode
	print("]")
	
def isUnique(D,L):
	cnode=L.head
	for i in range (length(L)):
		if insert_Dict(D,cnode.value_L,cnode.value_L)==None:
			return False
		cnode=cnode.nextNode
	return True
	
	
	
def postalCode(D,key):
	key = key.upper()
	if len(key)!=8:
		return None
	for i in range (8):
		if i==0 or i>=5:
	
			if ord(key[i])<65 or ord(key[i])>90:
				return None
		else:
			if ord(key[i])<48 or ord(key[i])>57:
				return None
			
	if key[0]=="I" or key[0]=="O" or key[0]=="Ñ":
		return None	
	insert_Dict(D,key,key,HashCodPost)
	return True
def LetterCount(D,S):
	cont=0
	contadorLetras=1
	insert_Dict(D,cont,(S[0]+str(contadorLetras)),HashInt)
	for i in range (1,len(S)):
		if S[i]!=S[i-1]:
			cont=cont+1
			contadorLetras=1
			insert_Dict(D,cont,(S[i]+str(contadorLetras)),HashInt)
		else:
			contadorLetras+=1
			delete_Dict(D,cont,HashInt)
			insert_Dict(D,cont,(S[i]+str(contadorLetras)),HashInt)
	returnString=""
	for i in range (len(D)):
		if D[i]!=None:
			returnString=returnString+D[i].head.value
		else:
			return returnString
	return ReturnString

def isSubString(S1,S2):
	D=Array(len(S1),dictionary())
	cont=0
	for i in range (len (S1)):
		if S1[i]==S2[0]:
			cont+=1
	for i in range (len(S1)):
		if S1[i]==S2[0]:
			if (len(S2)+i)<=len(S1):
				stri=substr(S1,i,i+(len(S2)))
				insert_Dict(D,i,stri,HashInt)
			else:
				break
	printDictionary(D)
	for i in range (len(D)):
		if D[i]!=None:
			if S2==str(D[i].head.value):
				return i
def isSubGroup(AS,AT):
	if len(AS)>len(AT):
		return False
	D=Array(len(AT),dictionary())
	for i in range (len(AT)):
		insert_Dict(D,AT[i],AT[i],HashInt)
	printDictionary(D)
	for i in range (len(AS)):
		if search_Dict(D,AS[i],HashInt)==None:
			return False
	return True