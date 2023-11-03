# testList = [1,2,False,5,"test1",6,"test7","test8",True]
# testList2=["test3","test1",1,3]
# print(id(testList[0]),id(testList2[2]), "Value:1 Different Arrays variables but same value and same address")
# print(id(testList),"testList1 id ")
# print(id(testList2),"testList2 id ")
# for i in testList:
#     print(id(i))
# testList.extend(testList2)


# print(id(testList),"testList1 extended id")

#Note1 testList1's id didnt changed after extend operation that
#means it didnt returned new list (??malloc and realloc applied on the
# background ?? ) 
# testList3 =[]
# testList4=[]

# for i in range(300):
#     testList3.append(i)
# for j in range(300):
#     testList4.append(j)
# print(id(testList4[290]),id(testList3[290])) different address



#same address
# for i in range(300):
#     testList3.append(i)
#     testList4.append(i)
# print(id(testList4[290]),id(testList3[290]))

# twoHundredNinety=290
# counter=0
# for i in range(300):
#     if(i==290):
#         print(id(i),id(counter),id(twoHundredNinety),"290-----------")
#     print(id(i),id(counter))
#     counter+=1



#Note2:-----WRONG---------Compiler doesn't reserve numbers in loop it creates addresses in a loop time ---WRONG-----
#Note2 Test Phase
a=5
b=5
c=260
print(id(a),id(b),id(c))

for i in range(280):
    if(i==5):
        print(id(i),"55555555555")
    elif(i==260):
        print(id(i),"260260260260")
    elif(i==270):
        print(id(i),"270270270270") #270 and 260 have same addresses
#Python has optimized variable address algorithm
#So is that mean python can run infinitely ??


#"5 address is same so its not new allocation"
# 4332958416
# c=5
# print(id(c))

d=260
print(id(d))
print(d is c)

#Allocates first 256 value for special area


