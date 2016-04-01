
def longest_palindromic(text): 
	candidate = []
	for i in range(0,len(text)):
		for j in range(i,len(text)):
			if text[i]==text[j]:
				candidate.append(text[i:j+1])

	candidate2 = []
	for i in candidate:
		for j in range(0,len(i)):
			if i[j] != i[len(i) - 1 - j]:
				break
			else:
				if j == (len(i) - 1 - j):
					candidate2.append(i)
	candidate2.sort(key= lambda x : len(x),reverse=True)
	return candidate2[0]

print(longest_palindromic('asdafadsaqaw'))