# class Dog():
#     def __init__(self,name):
#         self.name=name
#     def biting(self):
#         print(f'{self.name}在咬人')
#     def biting_ex(self):
#         print('咬人')
#
# def too_simple():
#     print('惊喜吧')
#
# dog1=Dog('小黑')
# print(dog1.__dict__)
# print(Dog.__dict__)
#
# print(id(dog1.biting))
# print(id(Dog.biting.__get__(dog1,Dog)))
# dog1.__dict__['biting']=too_simple
# dog1.biting()

# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=None
#         self.setAge(age)
#     def setAge(self,age):
#         if age<7 or age>20:
#             raise Exception('年龄不符合需求')
#         self.__age=age
#     def getAge(self):
#         return self.__age
#
# stu=Student('小明',14)
# print(stu.name)
# print(stu.getAge())
# stu.setAge(10)
# print(stu.getAge())
# stu.name='xiaoguo'
# print(stu.name)


class Studnt():
    def __init__(self,name,yw_score,sx_score):
        self.name=name
        self.yw_score=yw_score
        self.sx_score=sx_score
        self.teacher=None
class Teacher():
    def __init__(self,name):
        self.name=name
        self.students=[]

stu=Studnt('小明','98','80')
teacher=Teacher('张老师')

stu.teacher=teacher
teacher.students.append(stu)
print(stu.name,stu.yw_score,stu.sx_score,stu.teacher.name)
print(teacher.students[0].name)


