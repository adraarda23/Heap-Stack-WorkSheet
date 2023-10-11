boolean1 = True
boolean2 =True
boolean3 = False

print(id(True),id(False))

print(id(boolean1),id(boolean2),id(boolean3))

"""
Result : When compiler starts to compile it defines default address
for True and False and whenever user set variables which is boolean
variables points to this address
"""




#Example usages of memory address similarity
List = [1,2,3,4,5,6,10,2,3,7,8,1,8,3,13,2,1,23,1,2,1,3,1] 
biggestNumber =0
startAddress=0
#This for loop finds biggest number in the array
for i in range(len(List)):
    if(startAddress<id(List[i])):
        startAddress=id(List[i])
        biggestNumber=List[i]
print(biggestNumber)







    

    

