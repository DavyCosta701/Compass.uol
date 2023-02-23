def splitter(arg):
    list1 = arg[:len(arg)//3]
    list2 = arg[len(arg)//3:(len(arg)//3)*2]
    list3 = arg[(len(arg)//3*2):(len(arg)//3)*3]
    print(list1,list2,list3)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
splitter(lista)