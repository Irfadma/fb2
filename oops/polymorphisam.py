# method overloading
# from multipledispatch import 

# @dispatch(int,int)
# def findsum(x,y):
#     print(x+y)
# @dispatch(int,int,int)
# def findsum(x,y,z):
#     print(x+y+z)
# @dispatch(str,str,str)
# def findsum(x,y,z):
#     print(x+y+z)
# findsum(1,2)
# findsum(1,2,3)
# findsum("a","b","c")

# method overriding-same method name,no of arguments same

# class A:
#     def printdata(self):
#         print("inside class A")
# class B(A):
#     def printdata(self):
#         print("inside class B")
# a1=A()
# b1=B()
# b1.printdata()



# class person:
#    def __init__ (self,name,age):
#       self.name=name
#       self.age=age
#    # def print_person(self):
#    #     print(self.name,self.age,self.place)
# class student(person):
#    def __init__(self,rollno,dept,name,age):
#       self.rollno=rollno
#       self.dept=dept
#    def print_person(self):
#        print("name:",self.name,"\nage:",self.age,"\nrollno:"self.rollno,"dept:,self.dept")
# p1.people("1,"cs","abc",12)
# p1.printdata()

# bank account
# class bank:
#     bank_name="SBI"
#     def account(self,name,account_no):
#         self.name=name
#         self.account_no=account_no
#         self.main=1000
#         self.balance=self.main
#     def deposit(self,d_amount):
#         self.d_amount=d_amount
#         self.balance=self.balance+self.d_amount
#         print("your",bank.bank_name,"account has been credited",self.d_amount)
#         print("your tottal amount is:",self.balance)
#     def withdraw(self,w_amount):
#         self.w_amount=w_amount
#         if w_amount>self.balance:
#             print("insufficient balance")
#         else:
#             self.balance=self.balance-self.w_amount
#             print("your",bank.bank_name,"account has been debited",self.w_amount)
#             print("your balance amount is:",self.balance)
    
# b1=bank()
# b1.account("anu",12345567)
# b1.deposit(1000)
# b1.withdraw(500)

# class person:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#     def print_data(self):
#         print(self.name,self.age,self.place)
# f=open("text1.txt","r")
# for i in f:
#     l=i.rstrip("\n").split(",")
#     name=l[0]
#     age=l[1]
#     place=l[2]
#     a=person(name,age,place)
#     a.print_data()


#encapsulation

# class A:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#     def printdata(self):
#         print(self.name,self.age,self.place)

# a1=A("abc",12,"calicut")
# a1.printdata()
# print(a1.age)

# class employee:
#     def __init__(self):
#         self.name="abc"
#         self.age=23
#         self.__empid=100
#     def setvalue(self,name,age,__empid):
#         self.namename=name
#         self.age=age
#         self.empid=__empid
#     def getvalue(self):
#         print(self.name,self.age,self.__empid)
#         self.__readempid()
#     def __readempid(self):
#         print(self.__empid)
# class manger(employee):
#     def manager(self,__name,__age,__empid):
#        self.name=__name
#     self.age=__age
#     self.empid=__empid
# e1=employee()
# e1.getvalue()
# e1.manager()


# class person:
#     eye=2
#     def persondetails(self):
#         print("persondetails")
#     @classmethod
#     def persondetails2(cls):
#         print(cls.eye)
#         print(person.eye)
#     @staticmethod
#     def info():
#         print("static method")
# p1=person()
# p1.persondetails()
# person.info()


# abstartion

from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def area(self):
        pass
class triangle(polygon):
    def area(self):
        print("area...")
class rectangle(polygon):
    def area(self):
        print("area...")

t1=triangle()
# t1.sides()
t1.area()
r=rectangle()
r.area()
# r.rectangle()
# r1.sides()




    