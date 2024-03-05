def cakes(eggs, butter, flour):
    return min(eggs // 5, butter // 250, flour // 250)
print(cakes(10, 250, 250))