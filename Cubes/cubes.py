def makeTower(cubes,tower=[],index=0):
#Function to find the max length tower you can make out of n cubes(that have an edge length and a color) based on following rules
    # - No two adjacent cubes can have same color
    # - any cube that is on top of another cube mast have an edge length smaller than the one below

    #--------------------------------------------------------------------------------------
    
    #If we scanned all elements, check if the current tower is bigger than the current max tower
    #If yes, towered(Global variable where we store the biggest tower) becomes a copy of that tower

    if index==len(cubes):
        global maxTower
        if len(tower)>len(maxTower):
            maxTower = tower.copy()
        return None
    #-------------------------------------------------------------------------------------------
    
    #Count how many cubes share the same edge length as the one at cube[index]
    newIndex=index
    while newIndex<len(cubes) and cubes[newIndex]["length"]==cubes[index]["length"]:
        newIndex+=1
    #-------------------------------------------------------------------------------------------
        
    #If there are no elements in tower, add one cube from those with max edge length
    if len(tower)==0:
        for k in range(index,newIndex):
            makeTower(cubes,tower+[cubes[k]],newIndex)
    #-------------------------------------------------------------------------------------------
            
    #if tower not empty, compare to the last element in tower(by color).If color different, add it
    #to the tower and call the function again with index==the first cube with length less than
    #current cube.
    else:
        added=False
        for k in range(index,newIndex):
            if  cubes[k]["color"]!=tower[len(tower)-1]["color"]:
                added=True
                makeTower(cubes,tower+[cubes[k]],newIndex)
                
    #if no element can be added from those with edge length second in sequence to the last tower
    #element edge length, then go to the set of cubes with next edge length
        if not added:
            makeTower(cubes,tower,newIndex)


#Main()
        
        
    
#--------------------------------------------------------------------------
                
#Input N(nr of cubes), and each cube by color and length.
#Store as a list of dictionaries with keys length and color
while True:
    try:
        n=int(input("How many cubes: "))
        if n>0:
            break
        else:
            print("must be positive integer!Try again!")
            continue
    except ValueError:
        print("Must be integer! Try again!")
        continue
    
cubes=[{} for i in range(n)]

for i in range(n):
    print("Cube nr. %d: "%(i+1))
    cubes[i]["color"]=input("Color: ")
    while True:
        try:
            cubes[i]["length"]=int(input("Length: "))
            if cubes[i]["length"]>0:
                break
            else:
                print("must be positive integer!Try again!")
                continue
        except ValueError:
            print("Must be integer! Try again!")
            continue
    
#---------------------------------------------------------------------------
    
#Sort the cubes in descending order based on edge length
    
cubes=sorted(cubes,key=lambda k: k["length"],reverse=True)       #O(nlogn)--merge sort
#---------------------------------------------------------------------------

maxTower=[]

#call the function here. the function will store the max tower in the global variable maxTower

makeTower(cubes)
#---------------------------------------------------------------------------

#Print tower and max length of tower. Print tower in reverse order

print("\n"*10)
print("Max Length: %d"%(len(maxTower)))
print("TOWER: (bottom piece is the base, printed as a tower standing)\n")
for i in range(len(maxTower)-1,-1,-1):
    print(maxTower[i])
    print("-----------------------------------")
#----------------------------------------------------------------------------
