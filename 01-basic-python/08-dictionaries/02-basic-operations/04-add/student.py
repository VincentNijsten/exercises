def add(dictionary, key, value):
    dictionary[key] = value
    return dictionary

dictionary = {"een": 1, "twee":2}
print(add(dictionary, "drie", 3))