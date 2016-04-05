'''
rules:
1. first letter equals : 10%
2. last letter equals : 10%
3. len(word1) / len(word2) * 30%
4. len(set(word1)) / len(set(word2)) * 50%
'''
import string

def find_word(message):
    message = message.lower().split(' ')
    print(message)
    likeness = []
    for i in range(len(message)):
    	count = 0
    	s = message.pop(i).strip(string.punctuation)
    	for j in message:
    		j = j.strip(string.punctuation)
    		if s[0] == j[0]:
    			count += 10
    		if s[::-1][0] == j[::-1][0]:
    			count += 10
    		count += min(len(s),len(j)) / max(len(s),len(j)) *30
    		count += len(set(s).intersection(set(j))) / len(set(s + j)) *50
    		#count += min(set(len(s)),set(len(j))) / max(set(len(s)),set(len(j))) *50
    	#print(count)	
    	likeness.append(round((count / len(message)),3))
    	#print(likeness)
    	message.insert(i,s)
    #return message[likeness.index(max(likeness),-1)]
    print (max(likeness))
    print(likeness.index(max(likeness)))
    print (likeness)
    return message[(len(likeness) - 1) - likeness[::-1].index(max(likeness))]


print(find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University."))


'''

if) __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
'''