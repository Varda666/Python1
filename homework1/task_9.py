#Дополните приведенный код, используя списочный метод append(), чтобы список list1 имел вид list_final:

#list_f = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]


list1[2][2].insert(2, 7000) # почему нельзя поставить в индексе -1 ?
print(list1)