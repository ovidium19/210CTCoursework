'''s1=input("String 1: ")   #(1)
s2=input("String 2: ")   #(1)
s3=s1+s2                 #(1)
print(s3)                #(1)'''

#O(4) - not dependent on input
#------------------------------------------------
s1=input("String 1: ")   #(1)
s2=input("String 2: ")   #(1)
s3=""                     #(1)
for i in s1:            #(n)
    if i not in s3:     #(n)
        s3+=i           #(n)
for i in s2:            #(m)
    if i not in s3:     #(m)
        s3+=i           #(m)
print(s3)               #(1)'''

#O(3m+3n+4) = O(m+n)
#-------------------------------------------------------------
'''s1=input("String 1: ")   #(1)
s2=input("String 2: ")   #(1)
for i in s1:             #(n)
    if i in s2:          #(n)
        s1=s1.replace(i,"")    #(n)
if s1!="":
    print(s1)
else:
    print("Empty String")#(1)'''

#O(3n+3) = O(n)
#----------------------------------------------------
