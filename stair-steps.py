
def max_steps(numbers, method_values = None):
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 0:
        return 0
    return numbers[-1] + max(max_steps(numbers[:-1]), max_steps(numbers[:-2]))


def checkio(numbers):
    return max_steps(numbers + [0])

print(checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]))
#print(checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]))
print(checkio([]))

