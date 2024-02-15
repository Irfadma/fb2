result=0
n=121
temp=n
while n>0:
  rem=n%10
  result=(result*10)+rem
  n=n//10
print(n)
print(result)
if temp==result:
    print("palindrome")
else:print("not palindrome")
result=0
n=153
temp=n
while n>0:
  rem=n%10
  result=(result**10)+rem
  n=n//10
 print(n)
 print(result)
 if  temp==result:
     print("palindrome")
 else:
     print("not palindrome")    