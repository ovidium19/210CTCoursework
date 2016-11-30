def binarySearch(seq,val,start,end):
    #used to quickly search through the vertices in the graph and
    #in the neighbour arrays to look for the pointer to the vertex that
    #holds value val
    
    #returns the pointer to the vertice that contains the value searched
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
    #regular stack used by pre and post order traversal of graph
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
        if not self.isEmpty():
            return self.__stack[self.__top]
        else:
            return None

class Graph():
    edgeSum=0
    class Vertex():
        #the vertex class that represents a node in the graph
        #holds the data in the node and the neighbours of that node
        #we also have tw - used in dijkstra and MST algorithms - holds tentative weight of v
        #parent - will store the parrent of v in dijkstra and MST algorithms
        def __init__(self,val):
            self.data=val
            self.neighbours=[]
            self.tw=0
            self.parent=None

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
            
        def addNeighbour(self,v,w):
            #neighbours will be stored in order, based on edge length, for the purpose of
            # of preOrder and postOrder traversals
            if self.neighbours==[]:
                self.neighbours.append((v,w))
                if (self,w) not in v.neighbours:
                    v.addNeighbour(self,w)
                return True
            else:
                added=False
                for i in range(len(self.neighbours)):
                    if self.neighbours[i][1]>=w:
                        self.neighbours=self.neighbours[:i]+[(v,w)]+self.neighbours[i:]
                        added=True
                        break
                if not added:
                    self.neighbours.append((v,w))
                if (self,w) not in v.neighbours:
                    #because the graph is undirected, we have to add the head in the tail's
                    #neighbour list as well
                    v.addNeighbour(self,w)
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
        #adds a vertex to the list of vertices. It is done in order(based on data)
        if not isinstance(v,self.Vertex):
            v=self.Vertex(v)
        if self.vertices==[]:
            self.vertices.append(v)
            return True
        elif v in self.vertices:
            return False
        else:
            added=False
            for i in range(len(self.vertices)):
                if self.vertices[i]>v:
                    self.vertices=self.vertices[:i]+[v]+self.vertices[i:]
                    added=True
                    break
            if not added:
                self.vertices.append(v)
            return True
        
    def addEdge(self,h,t,w):
        #adds an edge from head to tail. It simply calls head's addNeighbour function
        #the user does not have to input pointers as parameters, can simply do it with values
        if not isinstance(h,self.Vertex):    
            h=self.findVertex(h)
        if not isinstance(t,self.Vertex):
            t=self.findVertex(t)
        if h not in self.vertices or t not in self.vertices:
            return False
        else:
            self.edgeSum+=w
            h.addNeighbour(t,w)
            return True

    def dijkstra(self,h,t):
        #               dijkstra's algorithm
        #find the shortest path from vertex h to vertex t
        #
        #- a vertex object will have fields tw and parent. tw field will keep the tentative
        #  weight of the vertex, while vertex.parent will remember who is the parent of the
        #  vertex
        #
        #- we have a list visited which will contain all vertices that have been solved
        #
        #- at each iteration, we see how the recently visited vertex affects the tw's of
        #  unsolved vertices. Then, we go through all unsolved vertices and pick the one
        #  with the minimum tw
        #
        #- h will always be the unsolved vertex with minimum tw(except first iteration).
        #  At the end of the iteration, h is added to visited.
        #
        #- algorithm will finish when either all vertices have been solved(connected graph)
        #-  or when nothing has been solved in an iteration(disconnected graph)
        #################################################################################
        if not isinstance(h,self.Vertex):
            h=self.findVertex(h)
        if not isinstance(t,self.Vertex):
            t=self.findVertex(t)
        for i in self.vertices:
            i.tw=self.edgeSum+1
        h.tw=0
        visited=[h]
        added=True
        while len(visited)!=len(self.vertices) and added:
            for i,w in h.neighbours:
                if i not in visited:
                    if i.tw>h.tw+w:
                        i.tw=h.tw+w
                        i.parent=h
            minTw=self.edgeSum
            for j in self.vertices:
                if j not in visited:
                    if minTw>j.tw:
                        minTw=j.tw
                        h=j
            if minTw==self.edgeSum:
                added=False
            else:    
                visited+=[h]

        #visited=sorted(visited)
        #for i in visited:
        #    if i.parent!=None:
        #        print(str(i.data)+" "+str(i.tw)+" "+str(i.parent.data))
        #    else:
        #        print(str(i.data)+" "+str(i.tw)+" "+"-1")
        if t.tw==self.edgeSum+1:
            print("no path")
        else:
            print("Shortest path: %d"%t.tw)
            s=''
            while t!=None:
                s+=str(t.data)+"-"
                t=t.parent
            s=s.strip("-")
            for i in range(len(s)-1,-1,-1):
                print(s[i],end='')
            print()

   
    def maxST(self,h):
        #              Finding the maximum spanning tree (h is a value,not pointer)
        #
        #  very similar to dijkstra
        #
        #- in this case, the end result will be the preOrder and postOrder traversal printing of
        #  a new graph which will be the mst containing vertex h
        #
        #- in this situation, we initialize each vertex tw with -1 and parent with None
        #
        #- the relaxation formula changes here, as we are not interested in the total weight of
        #  a vertice, we are only interested in the weight of the edge connecting that vertex
        #  Therefore, from i.tw = h.tw+w(dijkstra) we simply do i.tw = w
        #
        #-because we are doing the maximum spanning tree, we have to scan for maximum weight,
        # not minimum
        head=h
        if not isinstance(h,self.Vertex):
            h=self.findVertex(h)
        for i in self.vertices:      #O = |V|
            i.tw=-1
            i.parent=None
        h.tw=0
        visited=[h]
        added=True
        while len(visited)!=len(self.vertices) and added:
            for i,w in h.neighbours:    #O = |E|
                if i not in visited:
                    if i.tw<w:
                        i.tw=w
                        i.parent=h
            maxTw=-1
            for j in self.vertices:     #O= |V|
                if j not in visited:
                    if maxTw<j.tw:
                        maxTw=j.tw
                        h=j
            if maxTw==-1:
                added=False
            else:    
                visited+=[h]
                                    #O(n) = |V| + |E|
        ##########################################################
        #visited=sorted(visited)
        #for i in visited:
        #    if i.parent!=None:
        #        print(str(i.data)+" "+str(i.tw)+" "+str(i.parent.data))
        #    else:
        #        print(str(i.data)+" "+str(i.tw)+" "+"-1")
        if len(visited)!=len(self.vertices):
            print("Disconnected graph does not have a spanning tree")
            print("Returning maximum spanning tree for sub-graph containing vertex %d. "%(head))
        g=Graph()
        for i in visited:
            g.addVertex(i.data)
        for i in visited:
            if i.parent!=None:
                g.addEdge(i.data,i.parent.data,i.tw)
        print("Maximum spanning tree containing vertex %d: "%head)
        print(g)
        #print("total edge sum: " +str(g.edgeSum))
        print("pre-order: " + g.preOrder(self.findVertex(head)))
        print("post-order: " + g.postOrder(self.findVertex(head)))
        return None

        

    def preOrder(self,h):
        #- because the spanning tree is not necessarily binary, we can store it as a
        #  graph, where we sort the neighbours based on edge length
        #
        #- preOrder:
        #           -pop from stack into h
        #           -print value of h
        #           -iterate through all neighbours of h and add them to the stack in
        #            descending order(edge length)
        #           -repeat until stack is empty 
        #
        ######################################################################
        pre=''
        s=Stack()
        s.push(h)
        visited=[h]
        while not s.isEmpty():
            h=s.pop()
            pre+=str(h.data)+"->"
            for i in range(len(h.neighbours)-1,-1,-1):
                if h.neighbours[i][0] not in visited:
                    s.push(h.neighbours[i][0])
                    visited+=[h.neighbours[i][0]]
        return pre.strip("->")

    def postOrder(self,h):
        #- because the spanning tree is not necessarily binary, we can store it as a
        #  graph, where we sort the neighbours based on edge length
        #
        #- postOrder:
        #       -get top value of stack into h
        #       -add all neighbours to the stack in descending order that have not been visited
        #       -mark all neighbours added as visited
        #       -if none was added, pop from stack and print
        #########################################################
        post=''
        s=Stack()
        s.push(h)
        visited=[h]
        while not s.isEmpty():
            h=s.top()
            added=False
            
            for i in range(len(h.neighbours)-1,-1,-1):
                if h.neighbours[i][0] not in visited:
                    s.push(h.neighbours[i][0])
                    visited+=[h.neighbours[i][0]]
                    added=True

            if not added:
                h=s.pop()
                post+=str(h.data)+"->"
            
        return post.strip("->")
        

    def __str__(self):
        #printing the adjacency list
        s=''
        for i in self.vertices:
            s+=str(i.data)+": "
            for j in i.neighbours:
                s+=str(j[0].data)+"(%d) "%j[1]
            s+="\n"
        s+="Edge sum: "+str(self.edgeSum)
        return s

################################################
#File graph.txt is used to read from file should you wish to input this way
#
#   - First line contains a list of integers separated by space, these values are inserted in the graph
#       as vertices. Only distinct values will be counted
#
#   - On each line after the first, there should be a pair of numbers i,j,w separated by comma,
#       representing an edge from i to j (undirected, so j from i too) with weight w
#
#   - Any mistake in the way the input is taken will result in a ValueError or File related Error
#
#################################################

g=Graph()
f=open('graph.txt','r')
vertices=list(map(int,f.readline().strip().split(" ")))
for i in vertices:
    g.addVertex(i)
while True:
    line=f.readline()
    if not line:
        break
    i,j,w=map(int,line.strip().split(","))
    g.addEdge(i,j,w)
f.close()

g.dijkstra(3,9)
g.maxST(1)


