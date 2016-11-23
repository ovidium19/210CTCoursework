
class Node():
    '''
    In this case, the Node will have two values associated with it

    word -a string which represents a word
    freq -how many times that word appears in the text
    '''
    def __init__(self,word='',freq=0):
        self.word=word
        if word!='' and freq==0:
            self.freq=1
        else:
            self.freq=freq
        self.left=None
        self.right=None

###############################
# - Here, we define the BST data structure, modelled for this problem
# - The tree's key is the word, not the frequency, meaning that when I
#   insert in the tree, I maintain the BST properties by using the word.
#   This means the inOrder traversal would give me an alphabetical list
# - I chose this because finding a word becomes O(logn).

# - If we want to work with the frequencies, we need to define another class
# - that would take the tree from this class and make a BST with the key freq
################################
class BSTWords():
       
    def __init__(self,root=None):
        self.root=root

    def insert(self,node):
        ##########################
        # same thought process as when inserting in a normal BST
        # however, if we reach a node with the same word value as
        # the node we want to insert, then we just increase the
        #freq of that word
        ###########################
        if not isinstance(node,Node):
            node=Node(node)
            
        if self.root==None:
            self.root=node
            return None

        itr=self.root
        while True:
            if itr.word==node.word:
                itr.freq+=1
                return None
            elif itr.word<node.word:
                if itr.right!=None:
                    itr=itr.right
                else:
                    itr.right=node
                    return None
            else:
                if itr.left!=None:
                    itr=itr.left
                else:
                    itr.left=node
                    return None
    def findWord(self,word):
        #same as looking for a value in a normal BST
        itr=self.root
        
        while True:
            print(itr.word+"->",end="") #printing the path traversed by the function 
            if itr.word==word:
                print("\nThe word \"%s\" is here, it has frequency: %d"%(itr.word,itr.freq))
                return True
            elif itr.word<word:
                if itr.right==None:
                    print("\nWord is not here")
                    return False
                else:
                    itr=itr.right
            else:
                if itr.left==None:
                    print("\nWord is not here")
                    return False
                else:
                    itr=itr.left
    def preOrder(self,itr=None):
        if itr==None:
            itr=self.root
            
        print("%s | Frequency: %d"%(itr.word,itr.freq))
        if itr.left!=None:
            self.preOrder(itr.left)
        if itr.right!=None:
            self.preOrder(itr.right)
            
    def inOrder(self,itr=None):
        if itr==None:
            itr=self.root
            
        if itr.left!=None:
            self.inOrder(itr.left)
        print("%s | Frequency: %d"%(itr.word,itr.freq))
        if itr.right!=None:
            self.inOrder(itr.right)

            
#reading from the file    
f=open("paragraph.txt")
s=f.read().strip()
f.close()
#----------------------------------

#elminating all punctuation from the string
from string import punctuation as puncts
puncts+="\"\“\”"
s=s.translate(s.maketrans("","",puncts))
#----------------------------------------


#insert word by word the paragraph in the BST
sList=s.splitlines()
tree=BSTWords()
for i in sList:
    i=i.strip().lower()
    wList=i.split(" ")
    for j in wList:
        tree.insert(j)
#------------------------------------------
tree.preOrder()
tree.findWord('oliver')
        

            
