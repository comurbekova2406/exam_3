#keys = [int, float, str, None]#

list1 = [True, 2.3, None, "brook", 5]

list_type = {}

for i in list1:
    print(type(i))
    if type(i) in [int]:
        list_type["int"] = i

    elif type(i) == float:
        list_type["float"] = i

    elif type(i) == str:
        list_type["str"] = i

    elif type(i) == bool:
        list_type["bool"] = i

    elif type(i) is not None:
        list_type["none"] = i

print(list_type)
