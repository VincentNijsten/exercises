def remove_duplicates(xs):
    x = set()
    list = []
    for i in xs:
        x.add(i)
    for i in x:
        list.append(i)
    return list
print(remove_duplicates([1,2,3,3,4,1]))