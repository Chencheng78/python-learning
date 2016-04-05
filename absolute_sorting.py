def checkio(numbers_array):
    numbers = list(numbers_array)
    numbers.sort(key = lambda x : abs(x))
    return numbers

    print(checkio((-20, -5, 10, 15)))