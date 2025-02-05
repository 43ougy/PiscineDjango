def my_var():
    nameInt = 42
    nameStr = "42"
    nameLongStr = "quarante-deux"
    nameFloat = 42.0
    nameBool = True
    nameList = [42]
    nameDict = {42: 42}
    nameTuple = (42,)
    nameSet = set()
    print(nameInt, " est de type ", type(nameInt))
    print(nameStr, " est de type ", type(nameStr))
    print(nameLongStr, " est de type ", type(nameLongStr))
    print(nameFloat, " est de type ", type(nameFloat))
    print(nameBool, " est de type ", type(nameBool))
    print(nameList, " est de type ", type(nameList))
    print(nameDict, " est de type ", type(nameDict))
    print(nameTuple, " est de type ", type(nameTuple))
    print(nameSet, " est de type ", type(nameSet))

if __name__ == '__main__':
    my_var()