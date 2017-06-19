import math


def checkio(radius):
	n = math.ceil(radius)
	total = math.ceil(radius) ** 2
	solid = 0
	empty = 0

	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if math.sqrt(i**2 + j ** 2) <= radius:
				solid += 1
			if math.sqrt((i - 1) ** 2 + (j - 1) ** 2) >= radius:
				empty += 1

	return [4 * solid, 4*(total - solid - empty)]

print(checkio(0.9))
print(checkio(3))
print(checkio(2.1))
print(checkio(2.5))
