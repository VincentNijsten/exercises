def repeat(function,n):
    for x in range(n):
        function()

def say_hello():
    print("Hello!")

print(repeat(say_hello, 5))