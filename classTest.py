ls1=["software","ranjith",23,"30000"]
ls2=["software","rajesh",22,"20000"]


class SoftwareEng:
    #class attribute
    sits_on="always sits on the chair"

    def __init__(self,name,age,sal):
        self.name=name#instance attribute belong to only for this method
        self.age=age
        self.sal=sal

ob1=SoftwareEng(name="ranjith",age=23,sal=20003)
ob2=SoftwareEng(name="Bhasker",age=28,sal=320000)

print(ob1.name,ob1.age,ob1.sal)
print(f"Hi I am {ob1.name} with {ob1.age} and my salary is {ob1.sal}")
print(ob2.name)