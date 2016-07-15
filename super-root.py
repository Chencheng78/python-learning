def super_root(number):
    x = 0
    base = 1.0
    while not number - 0.001 < x ** x < number + 0.001:
        if x ** x <= number - 0.001:
            x += base
        else:
            base /= 2
            x -= base
    return x

print(super_root(81))