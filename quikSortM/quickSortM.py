#find the mth smallest elem
def quickSortM(seq,m):
    #same as quicksort, we from 2 lists, low and high
    #low will have elements lower or equal than pivot
    #high will have elements higher than pivot
    pivot=int(len(seq)/2)
    low=[]
    high=[]
    for i in range(len(seq)):
        
        if i!=pivot:
            if seq[i]<=seq[pivot]:
                low+=[seq[i]]
            else:
                high+=[seq[i]]
    #---------------------------------------------------
    #if the length of list low equals m-1, then our pivot is the mth smallest elem of the list
    if len(low)+1==m:
        return seq[pivot]

    #if the length of the list low >= m, then our mth smallest element is inside the list low
    elif len(low)>=m:
        return quickSortM(low,m)

    #else, our mth smallest element is inside the list high, however, because we are discarding low and
    #pivot from the list, we are now looking for the m-len(low)-1 smallest element in the list
    else:
        return quickSortM(high,m-len(low)-1)
    #-----------------------------------------------------
while True:
    try:
        seq=list(map(int,input("Enter a list of numbers separated by space: ").strip().split(" ")))
        m=int(input("which element to find: "))
        break
    except ValueError:
        print("all items must be integers")
        continue
print(seq)
print(quickSortM(seq,m))
