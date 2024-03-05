def double_dict_values(dictionary):
    dict = {}
    for k, v in dictionary:
        nv = v * 2
        dict[k] = nv
    return dict

dictionary = {'a': 1, 'b': 2, 'c': 3}
print(double_dict_values(dictionary))