#Get x and y from the user
#x - nr of eggs an alien hatches
#y - nr of days it takes for an egg to hatch
while True:
    try:
        x=int(input("How many eggs does an alien lay: "))
        y=int(input("How many days for an egg to hatch: "))
        if x>0 and y>0:
            break
        else:
            print("You must enter positive numbers! Try again!")
            continue
    except ValueError:
        print("You must input integer values! Try Again!")
        continue
#--------------------------------------------------


#Here,we initialize the list aliens.
#aliens[i]=y
#i - the day
#y - how many aliens are in that day
aliens=[1]+[0 for i in range(29+y)]
#--------------------------------------------------


#Two rules apply for each day.
#1. The number of aliens we have in day i transfers over to day i+1
#2. the number of aliens we have in day i+y increases by x*number of aliens in
#   day i
#We loop over the 30 days and apply those two rules for each day
for i in range(30):
    aliens[i+y]+=x*aliens[i]
    aliens[i+1]+=aliens[i]
#---------------------------------------------------
    
#print the result
print("Day 30: we have %d aliens"%aliens[29])



    
    
