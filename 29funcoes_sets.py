set1 = {1, 5, 2, 9}
set2 = {3, 2, 6, 9}



set3 = set1.union(set2)
print(set3)


set4 = set1.intersection(set2)
print(set4)

"""
set1.intersection_update(set2)
print(set1)"""

set5 = set1.symmetric_difference(set2)#verifica os elementos q nao se repetem nos sets
print(set5)