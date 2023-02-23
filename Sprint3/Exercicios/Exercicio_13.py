def my_map(list,f):
    list2 = []
    for i in list:
        list2.append(f(i))
    
    return list2

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_map(a, lambda x: x**2))