# functions

# print()
# len()
# type()

# user defined functionc
# block of codes which executes only when it is called
# code reusability

# l=[1,2,3,4,5]
# print(max(l))
# print(min(l))
# print(sum(l))

# def findsum():
#     num1=2
#     num2=3
#     s=num1+num2
#     print(s)
# findsum()
# findsum()
# findsum()
# print("bye")
# findsum()

# def findsum(num1,num2):
#     s=num1+num2
#     print(s)
# findsum(4,2)
# findsum(4)
# findsum()

# key word

# arbitary arguments(args)

# def func(*args):
#     print(args)
# func(1,2,3)

#arbitrary keyword arguments(**kwargs)
# def func(**kwargs):
#     print(kwargs)
# func(name="abc",age=12,place="calicut")

# s=0
# def findsum(num1,num2):
#     global s
#     s=num1+num2         #scope of variable
#     print(S)            #pass by value,pass by refrence
# findsum(1,2)
# print(s)


# s=0
# def findsum(0):
#     # global s
#     s=5
#     print("inside fun:",s)

def function1():
    name=input("enter the name:")
    print(name)
    return name

x=10
def function2():
    return "hello"