def merge_dict(dict1, dict2):
    for k, v in dict2.items():
        dict1[k] = v
    return dict1

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dict(dict1, dict2))