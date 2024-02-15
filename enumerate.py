# enumerate(iterable,start=0)
l1=[10,111,12,13,14,15]
ret=enumerate(l1,start=1)
print(list(ret))


l1=[10,11,12,13,14,15]
ret=enumerate(l1,start=1)
# for in in ret:
#   print(i)

for i, j in ret:
    print(i)
    #print(j)
for i,j in ret:
    print(i)
    print(j)