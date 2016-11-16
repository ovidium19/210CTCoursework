def printAPath(path):
    #fancy way of printing a path
    for i in path:
        print("-> %d,%d "%(i[0]+1,i[1]+1),end="")
    print()
    return None

def findPaths(lab,ents,end,pos=0,path=[]):
#if pos not zero, then we are in the labyrinth
    if pos!=0:
        #if we are in the labyrinth, we have to check if we are at our endpoint
        if pos==end:
            #then we found a path, increase nrOfPaths and print path, then return to look for more
            global nrOfPaths
            nrOfPaths+=1
            printAPath(path)
            return None
        else:
            #from one point, you can go in 4 directions. Check if any of those directions has a one and is not in the path
            #if so, then go there and call the function again

            #Note: first we check the elements of pos. The first statement in all the following IF's ->
            #is there to avoid IndexError on the 2nd statement
            if pos[1]>0 and lab[pos[0]][pos[1]-1]==1 and (pos[0],pos[1]-1) not in path:
                findPaths(lab,ents,end,(pos[0],pos[1]-1),path+[(pos[0],pos[1]-1)])
            
            if pos[1]<m-1 and lab[pos[0]][pos[1]+1]==1 and (pos[0],pos[1]+1) not in path:
                findPaths(lab,ents,end,(pos[0],pos[1]+1),path+[(pos[0],pos[1]+1)])
            
            if pos[0]>0 and lab[pos[0]-1][pos[1]]==1 and (pos[0]-1,pos[1]) not in path:
                findPaths(lab,ents,end,(pos[0]-1,pos[1]),path+[(pos[0]-1,pos[1])])
                
            if pos[0]<m-1 and lab[pos[0]+1][pos[1]]==1 and (pos[0]+1,pos[1]) not in path:
                findPaths(lab,ents,end,(pos[0]+1,pos[1]),path+[(pos[0]+1,pos[1])])
            
            return None
        
#if pos is zero, we have to enter the labyrinth first        
    else:
        for i in ents:
            if lab[i[0]][i[1]]==1:
                findPaths(lab,ents,end,i,path+[i])
                
    
    
s=input("Choose:\n1.Enter variables from keyboard\n2.Read maze from file\nEnter 1 or 2\n")
if s=='1':
    #keyboard input        
    #rows and colums of labyrinth       
    n=int(input("Nr of rows: "))
    m=int(input("Nr of columns: "))

    #coordinates of exit point
    exitN,exitM=map(int,input("Enter exit coordinates (x,y): ").split(","))

    #establishing on which part of the labyrinth the person can enter
    entrances=[]
    entrance=input("On which part of the labyrinth is the entrance? Left, Right, Top or Bottom?\n").strip().lower()
    
    #entering all the 1's in the labyrinth
    print("Enter pairs of numbers (x,y) x in 1 to %d and y in 1 to %d, separated by comma.This represents a walkable space in the labyrinth"%(n,m))
    print("End by writing anything other than the specified way of input")
    lab=[[0]*m for i in range(n)]
    while True:
        try:
            i,j=map(int,input("Enter pair: ").split(","))
            lab[i-1][j-1]=1
            continue
        except ValueError:
            s=input("Have you finished inputting the labyrinth(Enter 1 or 2)?\n1.Yes\n2.No\n")
            if s=='2':
                continue
            else:
                break
        except IndexError:
            print("That position is not available. Try again! ")
            continue
else:
    #input from lab.txt
    #first line contains n and m
    #next n lines contain the n rows of the maze
    #next line contains coordinates of the exit point
    #next line contains one of "top,left,right,bottom" indicating where a person can enter the maze
    inpFile=open("lab.txt")
    print(inpFile)
    n,m=map(int,inpFile.readline().split(" "))
    lab=[0 for i in range(n)]
    for i in range(n):
        lab[i]=list(map(int,inpFile.readline().split(" ")))
    exitN,exitM=map(int,inpFile.readline().split(" "))
    entrance=inpFile.readline().lower()
    inpFile.close()

if entrance=="left":
        entrances=[(i,0) for i in range(n)]
elif entrance=="right":
        entrances=[(i,m-1) for i in range(n)]
elif entrance=="top":
        entrances=[(0,i) for i in range(m)]
elif entrance=="bottom":
        entrances=[(n-1,i) for i in range(m)]

    
        
    
    
    
#remembering the end point
endPoint=(exitN-1,exitM-1)

#calling the function
nrOfPaths=0
findPaths(lab,entrances,endPoint)

#print how many paths were found
print("Total number of paths: %d"%nrOfPaths)
       
    
