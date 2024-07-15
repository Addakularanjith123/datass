# class Employee:
#     #pass
#     def __init__(self):
#         self.name=name
#         self.age=age
#         self.sal=sal
#
#
# class SoftwareEng(Employee):
#     pass
#
# class Designer(Employee):
#     pass
# se1=SoftwareEng()
# de1=Designer()


class Employee:
    #pass
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sal=sal


class SoftwareEng(Employee):
    pass

class Designer(Employee):
    pass
se1=SoftwareEng(name="ranjith",age="22",sal="50000")
print(se1)
#mmmmmde1=Designer()