# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = name

#         print("hi",self.name
#     def get_avg(self):
#         sum = 0 
#         for val in self.marks:
#             sum += val,"your avg score is:",sum/3)
# s1 = student("sushant mohan", [94, 95, 98])
# s1.get_avg()


#del method

# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("sushant")
# print(s1.name)
# del s1.name
# print(s1.name)


#Private(like)

# class Account:
#     def __init__(self, acc_no , acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.acc_pass)


# acc1 = Account("12345","ABCD")
# print(acc1.acc_no)
# print(acc1.reset_pass())


# class Person:
#     __name = "anonymous"
#     def __hello(self):
#         print("hello person")
#     def welcome(self):
#         self.__hello()
# p1 = Person()

# print(p1.welcome())


#Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped.")
# class Toyotacar(Car):
#     def __init__(self,name):
#         self.name = name
# car1 = Toyotacar("fourtuner")
# car2 = Toyotacar("prius")
# print(car1.start())
