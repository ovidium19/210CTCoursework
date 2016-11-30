def binarySearch(seq,val,start,end):
    #used to quickly search through the vertices in the graph and
    #in the neighbour arrays to look for the pointer to the vertex that
    #holds value val
    
    #returns the index of that pointer in the array
    #returns -1 when it fails to find
    mid=int((start+end)/2)
    if start>end:
        return -1
    if val==seq[mid]:
        return seq[mid]
    elif val<seq[mid]:
        return binarySearch(seq,val,start,mid-1)
    else:
        return binarySearch(seq,val,mid+1,end)

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

    def isEmpty(self):
        if self.__top==-1:
            return True
        else:
            return False
    def top(self):
        return self.__stack[self.__top]

    


class Queue():
    class Node():
        #elements of the queue
        def __init__(self,value):
            self.value=value
            self.next=None
    #a LinkedList that simulates a queue..used for bfsTraversal
    #queue - because it is more efficient to remove items from the front
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
    def enqueue(self,node):
        node=self.Node(node)
        if self.head==None:
            self.head=self.tail=node
            node.next=None
        else:
            self.tail.next=node
            node.next=None
            self.tail=node
        return None
        
    def dequeue(self):
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

    




class Graph():
    class Vertex():
        #the vertex class that represents a node in the graph
        #holds the data in the node and the neighbours of that node
        def __init__(self,val):
            self.data=val
            self.neighbours=[]

        def __eq__(self,val):
            return self.data==val
        def __lt__(self,val):
            return self.data<val
        def __le__(self,val):
            return self.data<=val
        def __gt__(self,val):
            return self.data>val
        def __ge__(self,val):
            return self.data>=val
            
        def addNeighbour(self,v):
            #adding neighbours will be done in order
            if self.neighbours==[]:
                self.neighbours.append(v)
                if self not in v.neighbours:
                    v.addNeighbour(self)
                return True
            else:
                added=False
                for i in range(len(self.neighbours)):
                    if self.neighbours[i]>=v:
                        self.neighbours=self.neighbours[:i]+[v]+self.neighbours[i:]
                        added=True
                        break
                if not added:
                    self.neighbours.append(v)
                if self not in v.neighbours:
                    #because the graph is undirected, we have to add the head in the tail's
                    #neighbour list as well
                    v.addNeighbour(self)
                return True
        
    def __init__(self):
        #the graph only holds the list of vertices
        self.vertices=[]

    def findVertex(self,val):
        #finds the pointer to the vertex that holds the value val(calls binarySearch)
        if isinstance(val,self.Vertex):
            val=val.data
        if self.vertices==[]:
            return False
        else:
            return binarySearch(self.vertices,val,0,len(self.vertices)-1)

    def addVertex(self,v):
        #adds a vertex to the list of vertices. It is done in order
        v=self.Vertex(v)
        if self.vertices==[]:
            self.vertices.append(v)
            return True
        else:
            added=False
            for i in range(len(self.vertices)):
                if self.vertices[i]>=v:
                    self.vertices=self.vertices[:i]+[v]+self.vertices[i:]
                    added=True
                    break
            if not added:
                self.vertices.append(v)
            return True
        
    def addEdge(self,h,t):
        #adds an edge from head to tail. It simply calls head's addNeighbour function
        #the user does not have to input pointers as parameters, can simply do it with values
        head=self.findVertex(h)
        tail=self.findVertex(t)
        if head not in self.vertices or tail not in self.vertices:
            return False
        else:
            head.addNeighbour(tail)
            return True
    def __str__(self):
        #printing the adjacency list
        s=''
        for i in self.vertices:
            s+=str(i.data)+": "
            for j in i.neighbours:
                s+=str(j.data)+" "
            s+="\n"
        return s

    def dfsTraversal(self,v):
        #uses a stack
        #will go down a path until the end, then return to where another path can be found
        v=self.findVertex(v) 
        if v not in self.vertices:
            return None
        vis=[]
        s=Stack()
        s.push(v)
        traversal=[]
        while not s.isEmpty():
            v=s.pop()
            traversal+=[v.data]
            vis+=[v]
            for i in v.neighbours:
                if i not in vis:
                    vis+=[i]
                    s.push(i)
        return traversal

    def bfsTraversal(self,v):
        #uses a queue
        #displays all neighbours of the current node, then iterates over all the children to do the same thing
        v=self.findVertex(v) 
        if v==-1:
            return None
        vis=[]
        q=Queue()
        q.enqueue(v)
        vis+=[v]
        while not q.isEmpty():
            v=q.dequeue()
            for i in v.neighbours:
                if i not in vis:
                    vis+=[i]
                    q.enqueue(i)
        for i in range(len(vis)):
            #we replace the pointers with the values they hold and return the list to the user(same above if w is given)
            vis[i]=vis[i].data
        return vis

    def isConnected(self):
        #if dfs traversal returns a list of all the vertices of the graph, then the graph is
        #strongly connected
        if len(self.vertices)==0:
            return False
        vis=self.dfsTraversal(self.vertices[0].data)
        if len(vis)==len(self.vertices):
            return "yes"
        else:
            return "no"

    def isPath(self,v,w):
        #similar to dfsTraversal
        # We go down a path until we find target vertex or its a dead end. Then we return to a previous
        # vertice where another path might be available
        file=open("ispath.txt",'w')
        file.write("\nLooking for a path from %d to %d:"%(v,w))
        s=Stack()
        v=self.findVertex(v)
        w=self.findVertex(w)
        if v not in self.vertices or w not in self.vertices:
            return False
        s.push(v)
        vis=[v]
        found=False
        while not s.isEmpty() and not found:
            added=False
            v=s.top()
            for i in v.neighbours:  
                if i not in vis:
                    if i == w:
                        found=True
                    s.push(i)
                    vis+=[i]
                    added=True
                    break
            if not added:
                garbage=s.pop()
        if found:
            printable=''
            while not s.isEmpty():
                printable=str(s.pop().data)+"->"+printable
            file.write("path: "+printable.strip("->"))
            file.close()
        else:
            file.write(" no path ")
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
        g.addVertex(i)
    while True:
        line=f.readline()
        if not line:
            break
        i,j=map(int,line.strip().split(","))
        g.addEdge(i,j)
    f.close()
else:
    #keyboard input. Self-explanatory input prompts
    while True:
        try:
            vertices=list(map(int,input("Enter list of integers separated by space(vertices): ").strip().split(" ")))
            break
        except ValueError:
            print("You must enter integers separated by space. Try again!")
            continue
    print("To enter edges, simply enter a pair of numbers i,j separated by comma. To stop, enter anything else")
    for  i in vertices:
        g.addVertex(i)
    while True:
        try:
            i,j=(map(int,input("Enter edge: ").strip().split(",")))
            g.addEdge(i,j)
            continue
        except ValueError:
            break

print(g.isConnected())
print("DFS: " + str(g.dfsTraversal(1)))
print("BFS: " + str(g.bfsTraversal(1)))
g.isPath(1,8)


            
    
                
                
