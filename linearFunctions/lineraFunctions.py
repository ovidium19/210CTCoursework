def calcFunction(eq,x):
    #simply calculate the value of the linear function for a given value x
    return eq[0]*x+eq[1]

def binarySearch(big,low,start,end):
    ######################################################
    #   on the principle of binary search
    #   2 base cases: 1. if start>end, then start is our critical point
    #       - it means the functions are not equal on an integer value
    #                 2. if eq1==eq2, then mid is our critical point
    #       - it means the functions are equal on an integer value
    #   
    #   if low > big, then we passed our critical point and have to search
    #           in range (start,mid-1)
    #   if low < big, then we havent reached the critical point yet so
    #           we look in (mid+1,end)
    #####################################################
    
    if start>end:
        return start
    else:
        mid=int((start+end)/2)
        eq1 = calcFunction(big,mid)
        eq2 = calcFunction(low,mid)
        if eq2 == eq1 :
            return mid
        elif eq2 > eq1:
            return binarySearch(big,low,start,mid-1)
        else:
            return binarySearch(big,low,mid+1,end)
    
    
def findCriticalPoint(big,low):
    incr = big[1]-low[1] #max value the critical point can have
    return binarySearch(big,low,1,incr)
    
    
print("A linear function can be written as : a*x + b = 0")

while True:
    try:    
        a,b=map(int,input("\nFirst function, enter a,b(tuple separated by comma): ").strip().split(","))
        break
    except ValueError:
        print("must be integers, separated by comma")
        continue
while True:
    try:    
        c,d=map(int,input("\nFirst function, enter a,b(tuple separated by comma): ").strip().split(","))
        break
    except ValueError:
        print("must be integers, separated by comma")
        continue
if (b>d and a>c) or (b<d and a<c):
    #the functions cant have a critical point if they never meet!
    print("no critical point!")
    critical=False
elif b>d:
    bigger=(a,b)
    lower=(c,d)
    critical=True
elif b<d:
    bigger=(c,d)
    lower=(a,b)
    critical=True
if critical:
    x=findCriticalPoint(bigger,lower)
    print("%d * %d + %d = %d"%(bigger[0],x,bigger[1],calcFunction(bigger,x)))
    print("%d * %d + %d = %d"%(lower[0],x,lower[1],calcFunction(lower,x)))
    print("Critical point is therefore x=%d"%x)
