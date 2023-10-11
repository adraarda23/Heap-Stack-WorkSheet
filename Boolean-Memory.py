import ctypes
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

#Hypothesis1 : Variable declaration time doesnt matter

#Experiment1 
x=3
y=2
z=1

print("x=3-->",id(x),"y=2-->",id(y),"z=1-->",id(z))
#Experiment2
x=2
y=1
z=3
print("x=2-->",id(x),"y=1-->",id(y),"z=3-->",id(z))
#Observation-Based Interpretation:
"""
Currently, Python (and perhaps other compiled programming 
languages as well) compiles integers in a hierarchical order.
This means that the largest numbers always have the largest 
addresses, and this property can be useful in certain algorithms.
"""

#Example usages of memory address similarity
List = [1,2,3,4,5,6,10,2,3,7,8,1,8,3,13,24,1,23,1,2,1,3,1] 
startAddress=0
"""
This for loop finds the largest number in the array without setting
any variables and can be useful in a memory-constrained environment.
"""
for i in range(len(List)):
    if(startAddress<id(List[i])):
        startAddress=id(List[i])
value_at_address = ctypes.cast(startAddress, ctypes.py_object).value
print(value_at_address)







    

    

