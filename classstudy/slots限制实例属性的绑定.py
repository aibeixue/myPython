class Student:
    __slots__ = ('name','age')

class GraduateStudent(Student):
    pass



s=Student()
s.name='小明'
s.age=18
print(s.name,s.age)
#继承的子类
g=GraduateStudent()
g.name='guorui'
g.age='18'
print(g.name,g.age)
g.score=100
print(g.score)

# __slots__ 可以限制实例属性的绑定，使用__slots需注意：__slots__顶一顶额属性仅对当前类实例起作用，
#对继承的子类是不起作用的，除非子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots_
#加上父类的__slots__

