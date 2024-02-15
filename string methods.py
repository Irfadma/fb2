# # string methods
# s="python programming"
# # upper()
# print(s.upper())
# print(s)
# # lower
# print(s.lower())
# print(s.title())
# print(s.capitalize())


# # print(s.startwith("pthon"))
# # print(s.endswith("gn"))
# s="python programming"
# # print(s.split())
# # print(s.split("t"))
# # print(s.split("thon"))
# print(s)
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
  
# s="python programming"
# print(s.replace("p","j",1))

# s2="luminar technolab"
# first=s2[0]
# second=s2[1:]
# print(first+second.replace(first,"$"))
# s="python123"
# print(s.isalpha())
# print(s.isnumeric())


s1="python @123"
alphabets=0
numbers=0
space=0
speical=0
for i in s1:
    if i.isalpha():
        alphabets+=1
    elif i.isnumeric():
        numbers+=1
    elif i.isspace():
        space+=1
    else:
        special=+1


