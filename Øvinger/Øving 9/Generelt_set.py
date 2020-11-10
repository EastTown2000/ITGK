#a)
my_set = set(range(1, 20, 2))

#b)
my_set2 = set(range(1, 10, 2))

#c)
my_set3 = my_set - my_set2

#d)
#Snittet fra sett b) og c) er tomt, og fra a) og c) er c)

#e)
def allUnique(lst):
    return len(lst) == len(set(lst))

#f)
def removeDuplicates(lst):
    modlst = []
    for item in set(lst): modlst.append(item)
    return modlst
    
print(removeDuplicates([1,3,5,2,3,7]))
