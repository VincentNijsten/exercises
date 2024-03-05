def last_digit(x):
    last = str(x)[-1]
    return last

def remove_last_digit(x):
    return x // 10

def digit_sum(n):
    result = 0
    while n > 0:
        result += last_digit(n)
        n = remove_last_digit(n)
    return result