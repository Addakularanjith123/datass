# crreate a class
se1=["soft eng","ranjith",24,"junior","20000"]
se1=["soft eng","ravi",23,"senior","40000"]
class SofrEng:
    #pass  simple class
    def __init__(self, name,age,level,salary):
        #instace attributesṇ
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
s1=SofrEng(name="ranjith",age=55,level="senior",salary=80000)

#se1=SofrEng()
print(s1.name,s1.age,s1.level,s1.salary)