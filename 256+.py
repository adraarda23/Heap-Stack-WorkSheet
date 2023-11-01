addressCounter_i= set()
addressCounter_counter=set()
counter =0
for i in range(500):
    #before 257
    if(id(i)== id(counter)):
        print("+",end="")
    #after 257    
    else:
        print(i , id(i), id(counter))
        addressCounter_i.add(id(i))
        addressCounter_counter.add(id(counter))
    counter+=1
print(addressCounter_i.difference(addressCounter_counter))
print(addressCounter_counter.difference(addressCounter_i))
print(len(addressCounter_i),len(addressCounter_counter))








