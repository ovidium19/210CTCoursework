#using a double linked list
class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class LinkedList():
    '''This class simulates a linked list.

       Attributes: head - Node
                   tail - Node

       Methods: valOf(self,n) - returns value of the nth element inside the linked list

                prepend(self,node) - prepends a node to the list(add before head)

                insert(self,node,where) - inserts a Node in the list right after the Node WHERE, or if node is not a Node, then
                                    it inserts a Node with the value of node. WHERE has to be a Node

                delete(self, node) - deletes a specified node, or deletes a node with the specified value(if node is not a Node)

                __str__(self) - prints the linked list as a string of values separated by space
        '''

                
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
        
    def valOf(self,n):
        #function to return the value of the nth node in the list
        
        if n<0:
            return None
        #elif n==0 and self.head!=None:
        #    return self.head.value
        elif self.head!=None:
            elem=self.head
            for i in range(n):
                elem=elem.next
            return elem.value
        return None

    def prepend(self,node):
        #prepend to a linked list
        if not isinstance(node,Node):
            node=Node(node)
        if self.head!=None:
            self.head.prev=node
            node.next=self.head
            self.head=node
            node.prev=None
        else:
            self.head=self.tail=node
            node.prev=node.next=None
        return None
            
    def insert(self,node,where=None):
        #if where is not sepcified, this function appends the node at the end
        #where has to be an instance of Node
        if not isinstance(node,Node):
            node=Node(node)
            
        if self.head==None:
            self.head=self.tail=node
            node.prev=node.next=None
            
        elif where==None:
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
            node.next=None
           
        else:
            node.next=where.next
            where.next.prev=node
            node.prev=where
            where.next=node
        return None
            
    def delete(self,node):
        if not isinstance(node,Node):
            node=Node(node)
            
        if self.head==None:
            return None
        elif self.head==node:
            self.head=node.next
            self.head.prev=None
            node.next=None
        elif self.tail==node:
            self.tail=node.prev
            node.prev=None
            self.tail.next=None
        else:
            node.next.prev=node.prev
            node.prev.next=node.next
            node.next=node.prev=None
        return None

    def __str__(self):
        s=''
        if self.head!=None:
            point=self.head
        else:
            return ""
      
        while True:
            s+=str(point.value)+" "
            if point.next==None:
                break
            point=point.next
        return s.strip()
    
class Matrix(LinkedList):
    '''
       Inherits LinkedList()
       Simulates a matrix as a linked list of linked lists

       __mul__(self,t) - Returns the product of matrix and t, where t can be a matrix or an integer
       __str__(self) - overdrive, to print all rows
    '''
    def __init__(self,order,head=None,tail=None):
        LinkedList.__init__(self,head,tail)
        self.order=order
        
    def __str__(self):
        s=''
        row=self.head
        while row!=None:
            s+=LinkedList.__str__(row.value)+'\n'
            row=row.next
        return s
    
    def __mul__(self,t):
        if isinstance(t,Matrix):
            res=Matrix(self.order)
            rows=self.head
            
            #same as a normal matrix multiplication, we go over all rows of first matrix, then all columns of second matrix,
            #then all elements of those rows and columns and multiply them.
            while rows!=None:
                l=LinkedList()
                for j in range(self.order):
                    total=0
                    for i in range(self.order):
                        total+=rows.value.valOf(i)*t.valOf(i).valOf(j)
                    l.insert(total)
                res.insert(l)
                rows=rows.next
        return res

#we ask the user if he would like to input from keyboard or from a file matrix.txt    
s=input("1.Read from keyboard\n2.Read from matrix.txt\nChoose 1 or 2\n").strip()

#-------------------------------------------------

if s=='1':
#keyboard input
    #Expecting two positive integers on the first line representing matrix order and power to be raised at
    while True:
        try:
            n,k=map(int,input("Enter matrix order and power: ").strip().split(" "))
            if n>0 and k>0:
                break
            else:
                print("Must be positive integers!")
                continue
        except ValueError:
            print("must be integers")
            continue
    #---------------------------------------------------------------------------------
        
    m=Matrix(n)
    
    #we ask the user to input the matrix, line by line, n times. Values should be inputted by separating the values with space
    for i in range(n):
        while True:
            try:
                print("Enter row: ",end='')
                row=list(map(int,input("").strip().split(" ")))
                if len(row)!=n:
                    print("must enter exactly %d integers separated by space! "%n)
                    continue
                break
            except ValueError:
                print("must be integers!")
                continue   
        l=LinkedList()
        for j in row:
            l.insert(j)
        m.insert(l)
    #-----------------------------------------------------------------------------------

else:
    #file input
    #we don't make error checks here since we expect the file to be organized as stated
    #first line contains 2 numbers separated by space, representing the matrix order and power to be raised at
    #next n lines contain n integers separated by space, representing the matrix
    inpFile=open("matrix.txt")
    n,k=map(int,inpFile.readline().split(" "))
    m=Matrix(n)
    for i in  range(n):
        row=list(map(int,inpFile.readline().strip().split(" ")))
        l=LinkedList()
        for j in row:
            l.insert(j)
        m.insert(l)
    inpFile.close()
    #-------------------------------------------------------------------------------------------

#we calculate the kth power by multiplying the same matrix k times(we use Matrix.__mul__)
resTotal=None
for i in range(k):
    if resTotal==None:
        resTotal=m
    else:
        resTotal*=m
print(resTotal)

    
    
    
        
            
            
