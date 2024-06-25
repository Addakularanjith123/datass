# class Emp:
#     def __init__(self):
#         self.name=name
# class Soft(Emp):
#     pass
# se1=Soft(name="ranjith")
class Soft:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self._sal=sal ##_is the protected variable
        self.__sal=sal## (__) is the private variable so we can't acces

se1=Soft(name="ranjith",age=33,sal=20000)

print(se1.name,se1.age,se1._sal)
print(se1.name,se1.age,se1.__sal)## (__) is local it is within the constractor it gives error



