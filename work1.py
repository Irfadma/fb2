#1
# count=0
# for row in range(5):
#   for col in range(row+1):
#     count+=1
#     print(count,end=" ")
#   print()

# #2
# n=5768
# count=0
# while(n>0):
#   rem=n%10
#   n=n//10
#   count+=1
# print("count:",count)

# #3
# l=[1,2,3,4,5]
# l1=[]
# for i in l:
#   l1.insert(0,i)
# print(l1)

#4
# s="irfad@2002gmail.com"
# alpha=0
# digits=0
# space=0
# special=0
# for i in s:
#   if i.isalpha():
#    alpha+=1
#   elif i.isnumeric():
#     digits+=1
#   elif i.isspace():
#     space+=1
#   else:
#     special+=1
# print(alpha)
# print(digits)
# print(space)
# print(special)
#6
# l=[5,10,15,10,20,15,30]
# s=set(l)
# l2=list(s)
# print(l2)
#8
# l1=["ten","twenty","thirty"]
# l2=[10,20,30]
# d={}
# for i in l1:
#   for j in l2:
#     d[i]=j
#     l2.remove(j)
#     break
# print(d)
#10
Employee=[
{"name":"A", "designation": "manager", "salary": 50000},
{"name":"B", "designation": "accountant","salary": 30000}, 
{"name":"C","designation":"bda","salary": 15000},
{"name": "D", "designation": "hr" ,"salary":40000}
]
for i in Employee:
  # print(i["name"])
  if i["salary"]>20000:
    print(i["name"])


