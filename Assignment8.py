class Kom:
    def __init__(self,name,role):
         self.name=name
         self.role=role

    def myfun(self):
         print(self.name,self.role)
         


obj1=Kom("komal","casher")
print(obj1.name,obj1.role)
obj2=Kom("rene","banker")
# print(obj2.name,obj2.role)
obj2.myfun()
obj3=Kom("pallavi","teacher")
print(obj3.name,obj3.role)
obj4=Kom("puja","web devloper")
# print(obj4.name,obj4.role)
obj4.myfun()

# Unlike class attributes, instance attributes are not shared by objects. Every object has its own copy of the instance attribute
#  (In case of class attributes all object refer to single copy).
# so thats why instance attributes have more preferrence


# super is use to refer the parent class instance
#class is define to inharit all the properties of another class 