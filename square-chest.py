def checkio(lines):
	count = 0
	lines = list(sorted(i) for i in lines)
	print(lines)
	for i in lines:
		if i[1] - i[0] == 1:
			a = [[i[0],i[0] + 4] , [i[1],i[1] + 4] , [i[0] + 4, i[1]+4]]
			b = [[i[0],i[0] + 4] , [i[1],i[1]+1] , [i[0] + 4, i[0]+8] , [i[1]+1,i[1]+1+4] , [i[1]+1+4,i[1]+1+8], [i[0]+8,i[0]+8+1] , [i[1]+8,i[1]+8+1]]
			c = [[i[0],i[0] + 4] , [i[0] + 4, i[0]+8] , [i[0] + 8, i[0]+12] , [i[1],i[1]+1] , [i[1]+1,i[1]+2] , [i[0]+12,i[0]+12+1] , [i[0]+12+1,i[0]+12+2] , [i[0]+12+2,i[0]+12+3] , [i[0]+3,i[0] +3+ 4] , [i[0]+3 +4,i[0] +3+ 4 +4] , [i[0]+3 +8,i[0] +3+ 8 +4]]
			fa = 0
			fb = 0
			fc = 0
			for i in a:
				if i in lines:
					fa +=1
			for i in b:
				if i in lines:
					fb +=1
			for i in c:
				if i in lines:
					fc +=1
			if fa == len(a):
				count+=1
			if fb == len(b):
				count+=1
			if fc == len(c):
				count+=1

	return count


print(checkio([[16,15],[16,12],[15,11],[11,12],[11,10],[10,14],[9,10],[14,13],[13,9],[15,14]]))