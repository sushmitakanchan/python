#MAKE A NEW LIST WHICH CONTAINS THE SUM OF TUPLE
list1=[(1,2),(3,4),(5,6),(4,5)]
list2=[]
for each in range(0,len(list1)):
    a,b=list1[each]
    list2.append(a+b)
print("sum of tuple:",list2)
