name="abc"
age=12
place="calicut"
print("my name is",name,"and my age is",age)
# default formatting
print("my name is {} and my age is {}".format(name,age))  #placeholder
# positional formatting
print("my age is{1} and my nameis{0}".format(name,age))
#  keyword formatting
print("my name is {x}and my age is {y}".format(x=name,y=age))

print(f"my name is {name} and my age is {age}")