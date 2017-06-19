def checkio(path):
	path = path.split('-')
	steps = [path[0]]
	dest = path[1]
	moves = 0
	while dest not in steps:
		a = [i for i in steps if i[0] in ['a','b','c','d','e','f','g','h'] and i[1] in ['1','2','3','4','5','6','7','8']]
		steps = []
		for chess in a:
			steps.extend([(chr(ord(chess[0])-1) + chr(ord(chess[1])-2)),(chr(ord(chess[0])+1) + chr(ord(chess[1])-2)),
			   (chr(ord(chess[0])-2) + chr(ord(chess[1])-1)),(chr(ord(chess[0])+2) + chr(ord(chess[1])-1)),
			   (chr(ord(chess[0])-2) + chr(ord(chess[1])+1)),(chr(ord(chess[0])+2) + chr(ord(chess[1])+1)),
			   (chr(ord(chess[0])-1) + chr(ord(chess[1])+2)),(chr(ord(chess[0])+1) + chr(ord(chess[1])+2))])
		moves +=1
		a = []
	return moves

# print(checkio("b1-d5"))
# print(checkio("a6-b8"))
# print(checkio("a1-h8"))
print(checkio("h1-g2"))