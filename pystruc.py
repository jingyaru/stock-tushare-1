##用来熟悉Python的基础数据结构

##tuple
#nested_tuple=(1,2,3),(1,2,3)
#print(nested_tuple)

##dic
from collections import Iterable
onedic={'key1':1,'key2':(1,2,3),'key3':[1,2,3]}

print(onedic)
print(isinstance(onedic.keys(),Iterable))
print(onedic.values())