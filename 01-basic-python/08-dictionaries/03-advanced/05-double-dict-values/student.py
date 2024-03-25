def double_dict_values(dictionary):
    newdict = {}
    for k, v in dictionary.items():
        nv = v * 2
        newdict[k] = nv
    return newdict

dictionary = {'a': 1, 'b': 2, 'c': 3}
print(double_dict_values(dictionary))