# # pop()
# #popitem
# #del

# # set-mutabale,duplicates not allowed
# s={1,2,3,4,5,1,2,3,4,5,"a","b",{"python":"a","java":"b"}}
# s2=set()
# #print(s)
# # add()
# s2.add("python") #single data immutable arguments
# s2.add(123)
# # s2.add([1,2,3])
# # s2.update([10,20,30]) mutable data,oyerable arguments
# #s2.update()
# # print(s2)


# s={1,2,3,4,5,6,"a","b"}
#  s.remove("z")
#  s.discard('z')
#  print(s)



l=["a","b","a","c","c","b","d"]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
