from mojPrzyklad import nameAdder as nAd, namePrinter as nPr, nameMultiplier
from mojPrzyklad import name_multi as list3

list1 = []
nAd(list1, 'Ada')
list2 = ['Dfg', 'des', 'Tgh', 'Jho', 'DaB', 'name1', 'Name2']
nAd(list1, list2)
print('Etap pierwszy:', list1)
nAd(list1, list3)
nPr(list2[1])

nameMultiplier(list1)

