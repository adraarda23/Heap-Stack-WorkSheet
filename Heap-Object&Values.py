class Arda():
    def __init__(self,a1,a2,a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3

    def yazdir(self):
        print(self.a1,self.a2,self.a3)
    def adres_yazdir(self):
        return id(self)

arda = Arda(1,2,3)
arda.yazdir()

arda2=Arda(3,4,5)
arda2.yazdir()

arda_value_copy = Arda(1,2,3)

print("-----Address----------")
print(arda.adres_yazdir(),"arda")
print(arda2.adres_yazdir(),"arda2")
print(arda_value_copy.adres_yazdir(),"arda_value-copy")


print("--------arda----------")
print(id(arda.a1),"a1")
print(id(arda.a2),"a2")
print(id(arda.a3),"a3")       # Memory adress of arda.a3 is has same value with arda2.a1

print("--------arda2----------")
print(id(arda2.a1),"a1")      # *** arda2.a1 and arda.a3 shares same memory address ***
print(id(arda2.a2),"a2")
print(id(arda2.a3),"a3")

arda3=Arda("arda","ardak","arda")

print("-----arda3--------------")
print(id(arda3.a1),"a1")
print(id(arda3.a2),"a2")
print(id(arda3.a3),"a3")      #Also arda3.a1 and arda3.a3 has same value and memory address
print("------------------------")

#Hypothesis1 : Do we change memory adresss when we change value of arda3.a1 ??


#Hypothesis1 --Experiment1:
print("---Hypothesis1 --Experiment1--")
arda3.a1="ardak"
print("-----arda3--------------")
print(id(arda3.a1),"a1")
print(id(arda3.a2),"a2")
print(id(arda3.a3),"a3")   
print("------------------------")

#Hypothesis1 --Experiment2:
print("---Hypothesis1 --Experiment2--")
arda3.a1="ard"
print("-----arda3--------------")
print(id(arda3.a1),"a1")
print(id(arda3.a2),"a2")
print(id(arda3.a3),"a3")   
print("------------------------")

#Hypothesis1 --Experiment3:
print("---Hypothesis1 --Experiment3--")
arda3.a1="ardak"
print("-----arda3--------------")
print(id(arda3.a1),"a1")
print(id(arda3.a2),"a2")
print(id(arda3.a3),"a3")   
print("--After arda3.a1 Value Change--")
arda3.a1="arda"
print("-----arda3--------------")
print(id(arda3.a1),"a1")
print(id(arda3.a2),"a2")
print(id(arda3.a3),"a3")   
print("------------------------")

#Observation-Based Interpretation:
"""
Even objects created with same value their addresses are not same.
However self values of objects can share the same memory address.
Also change of any values which has same address only effects changed
values address so when we are changing objects values it doesnt change its
value it changes its address not the value
"""



