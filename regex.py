# regular expression
# search pattern
# validation
# s="hello123"
# pattern="123"
# re-regular expression
# search(),findall(),sub(),split()

# import re
# s=input("enter the user name")
# patter="123"
# x=re.search(patter,s)
# if x:
#     print("validation")
# else:
#     print("invalid username")


# findall

# import re
# s="the car in car"
# pattern="car"
# x=re.findall(pattern,s)
# print(x)

#sub

# import re
# s="the rain in spain"
# pattern="in"
# replace="#"
# x=re.sub(pattern,replace,s)
# print(x)


# #split

# import re
# s="the rain in spain"
# pattern=" "
# x=re.split(pattern,s)
# print(x)

#quamtifires
#meta charectors

# import re
# s="ala3bc"
# pattern="1.3"
# x=re.search(pattern,s)
# if x:
#     print("valid user name")
# else:
#     print("invalid user name")

# [abc]-any of the string a,b,c

# import re
# s="ala3bc"
# pattern="[abc]"
# x=re.search(pattern,s)
# if x:
#     print("valid user name")
# else:
#     print("invalid user name")

#[a-z]-any charector from a to z
# [A-Z]
# [0-9]

# import re
# s="[a-z]"
# pattern="[abc]"
# x=re.search(pattern,s)
# if x:
#     print("valid user name")
# else:
#     print("invalid user name")

# ^(up arrow)

# import re
# s=input("ente rthe phone number")
# pattern=r"^[6-9]"
# x=re.search(pattern,s)
# if x:
#     print("valid phone number")
# else:print("invalid phone number")

#[^abc]
# import re
# s=input("ente rthe phone number")
# pattern=r"[^abc]"
# x=re.search(pattern,s)
# if x:
#     print("valid phone number")
# else:print("invalid phone number")

# import re
# s=input("ente rthe phone number")
# pattern=r"^t$"
# x=re.search(pattern,s)
# if x:
#     print("valid phone number")
# else:print("invalid phone number")


# import reo
# s=input("ente rthe phone number")
# pattern="^[6-9][0-9]{9}$"
# x=re.search(pattern,s)
# if x:
#     print("valid phone number")
# else:print("invalid phone number")

# - zero or more occurences

# import re
# s="the rain in spain is good innn"
# pattern="i*n"
# print(re.findall(pattern,s))

# + one or more occurences

# import re
# s="the rain in spain is good innn"
# pattern="in+"
# print(re.findall(pattern,s))

# ? atmos one

# import re
# s="the rain in spain is good innn"
# pattern="in?"
# print(re.findall(pattern,s)


# import re
# s=input("enter the phone number")
# pattern=r"^(\+91)?(\-)?(\s)?([6-9][0-90]{9}$)"
# x=re.search(pattern,s)
# if x:
#    print("valid phone number")
# else:
#    print("invalid phonr number")

# email
# import re
# s=input("enter the email")
# pattern=r"^([a-z]?[@](\s)?([0-9]{0-}$)"
# x=re.search(pattern,s)
# if x:
#     print("valid email")
# else:
#     print("invalid email")



