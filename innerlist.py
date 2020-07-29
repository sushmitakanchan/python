# To make the elements in the inner list and tuple to the outer list:
list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
list2=[i for each in list1 for i in each]
print (" required output:",list2)
