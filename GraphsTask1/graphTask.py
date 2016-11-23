class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Queue():
    #a LinkedList that simulates a queue..used for bfsTraversal
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
    def push(self,node):
        if self.head==None:
            self.head=self.tail=node
            node.next=None
        else:
            self.tail.next=node
            node.next=None
            self.tail=node
        return None
        
    def pop(self):
        if self.head==None:
            return None
        else:
            buffer=self.head.next
            self.head.next=None
            val=self.head.value
            self.head=buffer
            
        return val

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
    

    
class Stack():
    #regular stack used by dfsTraversal
    def __init__(self):
        self.__stack=[]
        self.__top=-1

    def push(self,value):
        self.__stack.append(value)
        self.__top+=1
        return None

    def pop(self):
        val=self.__stack.pop()
        self.__top-=1
        
        return val

    def empty(self):
        if self.__top==-1:
            return True
        else:
            return False
    def top(self):
        return self.__stack[self.__top]
    
class Graph():
    '''Building a graph data structure, whose vertices represent integer
       numbers.

        vertexInsert - insert a vertex in the graph. Must be an integer

        edgeInsert((a,b)) - inserts an edge between integer values a and b

        __str__ - displays the graph as an adjacency list

        dfsTraversal(v,w=None) - Performs a depth first traversal on the graph
                                 and returns a list with all the vertices visitedd
                                 starting with v.
                                 If w is given, the dfsTraversal will stop once
                                 w is reached

        isConnected() - Prints 'yes' or 'no if the graph is strongly connected

        isPath(v,w)  - Prints to 'isPath.txt' wethere there is a path between
                       vertices v and w in the graph. If a path is found, it will be
                       printed in the file.'''
    def __init__(self):
        self.adjList={}
        self.vertices=[] #holding the vertices in ascending order
        
    def vertexInsert(self,val):
        #if the val is integer and not in the graph already, then a key is created with that val
        #the val is also added in the vertices list, vertices list will always be sorted asccending
        if val not in self.adjList.keys():
            if type(val) == int:
                self.adjList[val]=[]
                if len(self.vertices)==0:
                    self.vertices.append(val)
                else:
                    added=False
                    for i in range(len(self.vertices)):
                        if self.vertices[i]>=val:
                            self.vertices=self.vertices[:i]+[val]+self.vertices[i:]
                            added=True
                            break
                    if not added:
                        self.vertices.append(val)
            else:
                return False
        return True
    
    def edgeInsert(self,edge):
        #the parameter is a tuple
        #error checking, if both elements are equal or any of them is not a vertex, return False
        #if not, the adjacency list is updated to include the new edge
        i,j=edge
        if i==j:
            return False
        if i not in self.adjList.keys() or j not in self.adjList.keys():
            return False
        elif j not in self.adjList[i]:
            self.adjList[i]+=[j]
            self.adjList[j]+=[i]
        return True
    
    def __str__(self):
        s="Adjacency List: \n"
        for i in self.vertices:
            s+="%d: "%i +str(sorted(self.adjList[i]))
            s+="\n"
        return s
    
    def dfsTraversal(self,v,w=None):
        #uses a stack
        #will go down a path until the end, then return to where another path can be found
        if v not in self.adjList.keys():
            return None
        vis=[]
        s=Stack()
        s.push(v)
        vis+=[v]
        while not s.empty():
            v=s.top()
            added=False
            for i in self.adjList[v]:
                if i not in vis:
                    vis+=[i]
                    if i == w:
                        return vis
                    added=True
                    s.push(i)
                    break
            if not added:
                s.pop()
        return vis

    def bfsTraversal(self,v,w=None):
        #uses a queue
        #displays all neighbours of the current node, then iterates over all the children to do the same thing
        if v not in self.adjList.keys():
            return None
        vis=[]
        q=Queue()
        q.push(Node(v))
        vis+=[v]
        while not q.isEmpty():
            v=q.pop()
            for i in self.adjList[v]:
                if i not in vis:
                    vis+=[i]
                    if i== w:
                        return vis
                    q.push(Node(i))
        return vis
        
            

    def isConnected(self):
        #if dfs traversal returns a list of all the vertices of the graph, then the graph is
        #strongly connected
        if len(self.vertices)==0:
            return False
        vis=self.dfsTraversal(self.vertices[0])
        if len(vis)==len(self.adjList.keys()):
            print("yes")
        else:
            print("no")
        
    def isPath(self,v,w):
        #simply do a dfs traversal strating from v, if w is found in the list, then there is a path
        #between the two.
        #the output is displayed in the file ispath.txt
        file=open("ispath.txt",'a')
        file.write("\nLooking for a path from %d to %d:"%(v,w))
        vis=self.dfsTraversal(v,w)
        if w not in vis:
            file.write(" no path")
            file.close()
            return None
        else:
            file.write( " path: " + str(vis))
            file.close()
            return None
        

s=input("Read from file or keyboard?\n1.File(graph.txt)\n2.Keyboard\n(write 1 or 2)\n").strip()
#File graph.txt is used to read from file should you wish to input this way
#
#   - First line contains a list of integers separated by space, these values are inserted in the graph
#       as vertices. Only distinct values will be counted
#
#   - On each line after the first, there should be a pair of numbers i,j separated by comma,
#       representing an edge from i to j (undirected, so j from i too)
#
#   - Any mistake in the way the input is taken will result in a ValueError or File related Error
#
########################################
g=Graph()
if s=='1':
    f=open('graph.txt','r')
    vertices=list(map(int,f.readline().strip().split(" ")))
    for i in vertices:
        g.vertexInsert(i)
    while True:
        line=f.readline()
        if not line:
            break
        i,j=map(int,line.strip().split(","))
        g.edgeInsert((i,j))
    f.close()
else:
    while True:
        try:
            vertices=list(map(int,input("Enter list of integers separated by space(vertices): ").strip().split(" ")))
            break
        except ValueError:
            print("You must enter integers separated by space. Try again!")
            continue
    print("To enter edges, simply enter a pair of numbers i,j separated by comma. To stop, enter anything else")
    for  i in vertices:
        g.vertexInsert(i)
    print(g.vertices)
    while True:
        try:
            edge=tuple(map(int,input("Enter edge: ").strip().split(",")))
            g.edgeInsert(edge)
            continue
        except ValueError:
            break
    print(g)

#print(g.dfsTraversal(1))
#print(g.bfsTraversal(1))
#print(g)
#g.isConnected()
#g.isPath(6,8)
#g.vertexInsert(0)
#g.edgeInsert((0,8))
#print(g)
#g.isConnected()
#g.isPath(0,8)
                  
    
    
