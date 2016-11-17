class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
class CircularLinkedList():
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
    def prepend(self,node):
        #this method will add the Node just before the head
        if not isinstance(node,Node):
            node=Node(node)
        node.next=self.head
        self.tail.next=node
        self.head=node
    def insert(self,node,where=None):
        #inserts the Node right after the node Where. If where is not specified
        #the node is appended to the list
        if not isinstance(node,Node):
            node=Node(node)
            
        if self.head==None:
            node.next=node
            self.head=node
            self.tail=node
            
        elif where==None or self.tail==where:
            node.next=self.head
            self.tail.next=node
            self.tail=node
            
        else:
            node.next=where.next
            where.next=node
            
    def delete(self,node):
        #deletes a specified Node in the list
            
        if self.head==None:
            return None
        elif self.head==node:
            self.tail.next=self.head.next
            self.head=self.head.next
        else:
            step=self.head
            while step.next not in (node,None):
                step=step.next
            if node == self.tail:
                self.tail=step
            step.next=node.next
            node.next=None
            
            

    def __str__(self):
        s=' '
        if self.head!=None:
            point=self.head
        else:
            return "empty List"
      
        while True:
            s+=str(point.value)+" "
            if point.next==self.head:
                break
            point=point.next
        return s

#getting the number of names
while True:
    try:
        n=int(input("Enter n: "))
        if n>0:
            break
        else:
            print("should be apositive integer!")
            continue
    except ValueError:
        print("should be integer!")
        continue
#-------------------------------
#getting the names
while True:
    aList=input("Enter all %d names split by comma: "%n).strip().split(",")
    if len(aList)==n and "" not in aList:
        break
    else:
        print("You didn't enter %d names! Try again!"%n)
        continue
#--------------------------------


cr=CircularLinkedList()
for i in aList:
    cr.insert(i)

#eliminating people until one is left
#because the person counting also counts itself, in order to find the person
#that needs to be eliminated, we iterate over the list n-1 times
while cr.head!=cr.tail:
    #the algorithm stops when there is only one element in the list
    itr=cr.head
    #the person that starts the count is always the first person in the list
    for i in range(n-1):
        itr=itr.next
    print("Eliminating "+itr.value)
    
    cr.delete(itr)
    
print("Winner: "+cr.head.value)
        


        

        
