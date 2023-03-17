from avltree import *
from algo1 import *

AT=AVLTree()
avl_insert(AT, "E", 10)
avl_insert(AT, "C", 5)
avl_insert(AT, "G", 15)
avl_insert(AT, "B", 0)
avl_insert(AT, "D", 7.5)
avl_insert(AT, "A", -5)
avl_insert(AT, "F",12.5)
imprimirarbol(AT,AT.root)
#calculoBF(AT)
# rotateRight(AT,AT.root)
# calculoBF(AT)