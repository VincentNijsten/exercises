def remove(dictionary, key):
    dictionary.pop(key)
    return dictionary

dictionary = {"een": 1, "twee":2}
print(remove(dictionary, "een"))