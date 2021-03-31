
# class People:
#     name=''
#     age=0
#     __weight=0
#     def __init__(self,name,age,weight):
#         self.name=name
#         self.age=age
#         self.__weight=weight
#     def speak(self):
#         print(f'{self.name}说：我{self.age}岁,体重：{self.__weight}')
#
# class Student(People):
#     grade=''
#     def __init__(self,name,age,weight,grade):
#         People.__init__(self,name,age,weight)
#         self.grade=grade
#     def speak(self):
#         print(f'{self.name}说：我{self.age}岁了，我在读{self.grade}年级')
#
# class Speaker():
#     topic=''
#     name=''
#     def __init__(self,name,topic):
#         self.name=name
#         self.topic=topic
#     def speak(self):
#         print(f'我叫{self.name}，我是一个演说家，我演讲的主题是{self.topic}。')
#
# class Sample(Speaker,Student):
#     a=''
#     def __init__(self,name,age,weight,grade,topic):
#         Student.__init__(self,name,age,weight,grade)
#         Speaker.__init__(self,name,topic)
#
# test=Sample(name='guorui',age='18',weight='80斤',grade=2,topic='sample主题')
# test.speak()
# stu=Student(name='xiaoguo',age='20',weight='50公斤',grade=3)
# stu.speak()
# super(Student,stu).speak()

from types import MethodType


class Site:
    __site='www.baidu.com'
    def __init__(self,name):
        self.name=name
        siteList=[]

def set_age(self,age):
    self.age=age



site=Site('医脉相诚')
print(site._Site__site)
site.ip='192.168.10.205'
print(site.name,site.ip)
site.set_age=MethodType(set_age,site)
site.set_age(25)
print(site.age)

site2=Site('淘宝')