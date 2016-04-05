'''
 A pawn is safe if another pawn can capture a unit on that square.
'''

def safe_pawns(pawns):
	pawns = list(pawns)
	safe = 0
	for p in range(0,len(pawns)):
		chess = pawns[p]
		n_chess1 = chr(ord(chess[0])-1) + chr(ord(chess[1])-1)
		#n_chess2 = chr(ord(chess[0])+1) + chr(ord(chess[1])-1)
		n_chess3 = chr(ord(chess[0])+1) + chr(ord(chess[1])-1)
		#n_chess4 = chr(ord(chess[0])-1) + chr(ord(chess[1])-1)
		if (n_chess3 in pawns) or (n_chess1 in pawns) :
			safe +=1

	return safe

print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))