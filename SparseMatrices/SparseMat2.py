
#Define an error for matrix multiplication. This error will occur
#when a matrix operation is not possible
class MatrixOpError(Exception):
    def __init__(self,val):
        self.value=val
    def __str__(self):
        return (repr(self.value))

    
class SparseMat():
    '''Class SparseMat() documentation:

       Attributes:
            row (int) - number of rows of matrice
            col (int) - number of columns of matrice
            points (dictionary...key:tuple of ints,value:int) - dictionary of all values of the matrice
            sparse (boolean) - True if matrice is sparse, false otherwise
                                                                    

       Methods:
           __init__(self,row=-,col=0,points={})
                             -if no parameters specified, it inputs its values from the keyboard
                             -else, initializes a sparse matrice with the parameters given

           __add__(self,SparseMat)
                             -adds two matrices and produces a third matrice

           __sub__(self,SparseMat)
                             -returns __add__(self,-1*SparseMat)

           __mul__(self,SparseMat)
                             -returns a SparseMat object that represents the multiplication of two
                             sparse matrices. If the result is not a sparse matrice, the result will
                             only be displayed, not saved in memory

           __rmul__(self,int)
                            -returns same matrice multiplied by an int.
           checkSparse(self)
           					-returns True if matrix is sparse.''' 
        
    def __init__(self,row=0,col=0,points={}):
        #If we get parameters, initialize the matrice with those parameters, if they're correct
        if row>0 and col>0:
                self.row=row
                self.col=col
                if isinstance(points,dict):
                    self.points=points
                else:
                    self.points={}
                
                self.checkSparse()
        #---------------------------------------------------------------
        #In all other cases, we input from the keyboard
        else:
            #input rows and cols. If they are not positive integers, repeat until we get there
            while True:
                try:
                    r=int(input("Rows: "))
                    c=int(input("Columns: "))
                    if r>0 and c>0:
                        break
                    else:
                        print("You must enter positive ints! Try again!")
                        
                except ValueError:
                    print("Must be integers!Try again!")
                    continue
            #----------------------------------------------------------------------------
            #input the values. Comes as a tuple of row,col,value. In case the input is anything else other than
            #that, the input process stops. If value==0, it will not be stored, since we dont store 0's
            print("To end adding elements to the matrix, put anything other than a tuple of 3 ints")
            points={}
            while True:
                try:
                    x,y,v=map(int,input("Enter row,column and value, separated by comma: ").split(","))
                    if v==0:
                        print("Cannot store value 0, please enter a different value!")
                        continue
                    else:
                        points[x-1,y-1]=v
                except ValueError:
                    break
           
            self.row=r
            self.col=c
            self.points=points
            self.checkSparse()
            #---------------------------------------------------------------------------------

    def checkSparse(self):
        '''Checks if the current object is a sparse matrice'''
        #compare length of dictionary with row*col/2. If less, then it's sparse
        if len(self.points.keys())<self.row*self.col/2:
            self.sparse=True
        else:
            self.sparse=False
        return None
                
    def __add__(self, mat2):
        '''Returns a new matrice that is the result of mat1+mat2'''
        #adding is straight-forward. It is like a reunion of two sets,however keys that are in both sets
        #have their values added
        #Error can occur if matrices don't have same dimension
        if self.row!=mat2.row or self.col!=mat2.col:
            raise MatrixOpError("The matrices need to have same size to be added! ")
        else:
            addpoints={}
            for i in self.points.keys():
                if i not in mat2.points.keys():
                    addpoints[i]=self.points[i]
                else:
                    addpoints[i]=self.points[i]+mat2.points[i]
            for i in mat2.points.keys():
                if i not in self.points.keys():
                    addpoints[i]=mat2.points[i]
            return SparseMat(self.row,self.col,addpoints)
        
    def __sub__(self,mat2):
        '''return mat1-mat2'''
        #Instead of doing mat1-mat2 we can do mat1 + (-1)*mat2
        return self.__add__(-1*mat2)

    def __mul__(self,num):
        '''multiplication definition between matrice and integer or two matrices. Returns a matrice'''
        if type(num)==int:
            #if num is an integer, then we simply multiply all values in the dictionary by num
            for i in self.points.keys():
                self.points[i]*=num
            return self
        elif isinstance(num,SparseMat):
            #if num is a matrice:
            #-if mat1.col!=mat2.row, matrices cannot be multiplied
            #-for each element at (i,j) in mat1, we check the (j,k) elements of mat2.If (j,k) exists, than
            #   element (i,k) will increase by the product of mat1[i,j] and mat2[j,k]
            #Complexity - O(n^3)
            if self.col!=num.row:
                raise MatrixOpError("multiplication not possible")
            else:
                newpoints={}
                for (i,j) in self.points.keys():
                    for k in range(num.col):
                        if (j,k) in num.points.keys():
                            if (i,k) not in newpoints.keys():
                                newpoints[(i,k)]=self.points[(i,j)]*num.points[(j,k)]
                            else:
                                newpoints[(i,k)]+=self.points[(i,j)]*num.points[(j,k)]
                    
                return SparseMat(self.row,num.col,newpoints)
            
    def __rmul__(self,num):
        #So that mat * x is the same as x * mat
        if type(num)==int:
            return self.__mul__(num)
            
        
    def printMat(self):
        '''Prints matrice in natural form'''
        for i in range(self.row):
            for j in range(self.col):
                if (i,j) not in self.points.keys():
                    print("0 ",end="")
                else:
                    print("%d "%self.points[(i,j)],end="")
            print("")
        return None

newMat1=SparseMat()
newMat2=SparseMat()
newMat1.printMat()
print()
newMat2.printMat()
print()
newMat3=newMat1*newMat2

newMat4=newMat1-newMat2

newMat5=newMat3*newMat4

newMat3.printMat()
print(newMat3.sparse)
newMat4.printMat()
print(newMat4.sparse)
newMat5.printMat()
print(newMat5.sparse)




    
    
