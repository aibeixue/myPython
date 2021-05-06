class Student():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f'Student object {self.name}'
    __repr__=__str__

stu=Student('GUORUI')
print(stu)
print(Student('xiaoguo'))

# class Fib:
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>10:
#             raise StopIteration()
#         return self.a
# for n in Fib():
#     print(n)

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f=Fib()
print(f[:10])



