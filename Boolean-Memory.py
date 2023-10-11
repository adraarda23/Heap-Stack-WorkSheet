import sys
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
print(sys.getsizeof("\0"))
