# class mobile:
#     color="red"
#     def call(self):
#         print("calling...")
#     def game(self):
#         print("gaming...")
# mobile1=mobile()
# mobile1.call()
# mobile1.game()
# mobile2.mobile()
# mobile2.call()
# mobile3.mobile()
# mobile4.mobile()
# print(mobile1.color)


# class mobile:
#     color="red"
#     def call(self):
#         print("calling...")
#     def game(self):
# class laptop(mobile):
#     pass
# l1=call()

# multilevel

# class gparent:
#     def gparent_features(self):
#         print("grand parent features")

# class parent(gparent):
#     def parent_features(self):
#         print("parent features")
# class child(parent):
#     def child_features(self):
#         print("child features")
# c1=child()
# c1.chitures()
# c1.parent_features()
# c1.gparent_features()


# multiple

# class father:
#     def father_features(self):
#         print("grand parent features")

# class mother:
#     def mother_features(self):
#         print("parent features")
# class child(father,mother):
#     def child_features(self):
#         print("child features")
# c1=child()
# c1.child_features()
# c1.father_features()
# c1.mother_features()

#heirarchical
# class parent:
#     def parent_features(self):
#         print("mother features")

# class child1:
#     def child1_features(self):
#         print("mother features")
# class child2(parent):
#     def child2_features(self):
#         print("child features")
# c1=child1()
# c1.parent_features()
# c1.child2()
# c2.parent_features()

# #hybrid
# class college:
#     pass
# class branch(college):
#     pass
# class year(college):
#     pass
# class student(year,branch):
#     pass

# class printdata:
#     def findsum(self,num1,num1,num2):
#         # print(num1+num2)
#         self.num1=num1
#         self.num2=num2
#     def printsum(self):
#         print(self.num1+self.num2)
# p1=printdata()
# p1.findsum(2,4)
# p1.printsum():


# class student:
# def student_details(self.name,age,dept,college):
#    self.name=name
#    self.age=age
#    self.dept=dept
#    self.college=college
# def print_student(self):
#     print("name:",self.name,"age:",self.age,"deept:",self.dept,"college:",self.college)


# s1=student()
# s1.stud_dedtails("abc",12,"cs")
# s1.print_stud()
# s2=student()
# s2.stud_details("asd",23,"ec")
# s2.print_stud()


#static\class variable


# class student:
#    college="xyz"
#    def student_details(self,name,age,dept):
#      self.name=name
#      self.age=age
#      self.dept=dept
#    def print_student(self):
#       print("name:",self.name,"age:",self.age,"dept:",self.dept,"college:",student.college)


# s1=student()
# s1.student_details("abc",12,"cs")
# s1.print_student()
# s2=student()
# s2.stud_details("asd",23,"ec")
# s2.print_stud()



# class student:
#    institution_name="nasif"
#    fee=60000
#    def student_details(self,name,age,rollno):
#        self.name=name
#        self.age=age
#        self.rollno=rollno
#    def print_student(self):
#       print("name:",self.name,"age:",self.age,"rollno:",self.rollno,"institution:",self.institution_name,"fee:",self.fee)


# s1=student()
# s1.student_details("abc",12,1)
# s1.print_student()
# s2=student()
# s2.student_details("asd",23,2)
# s2.print_student()

# constructor
# class student:
#    def __init__(self,name,age):
#       self.name=name
#       self.age=age
#    def printdetail(self):
#       print(self.name,self.age)
# s1=student("abc",12)
# s1.printdetail()
# s2=student()

# class person:
#    def people(self,name,age,place):
#       self.name=name
#       self.age=age
#       self.place=place
#    # def print_person(self):
#    #     print(self.name,self.age,self.place)
# class student(person):
#    def stud(self,rollno,dept):
#       self.rollno=rollno
#       self.dept=dept
#    def print_person(self):
#        print(self.name,self.age,self.place,self.rollno,self.dept)
# p1=student()
# p1.people("koduvally",21,"irfad")
# p1.stud(23,"cs")
# p1.print_person()


