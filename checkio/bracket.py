import re
def checkio(expression):
	list1 = re.findall(r'[(,),{,},\[,\]]',expression)
	i = 0
	while len(list1) > 1:
		if list1[i] == '{' and list1[i+1] == '}':
        	list1.remove(list1[i])
        	list1.remove(list1[i])
        	i = 0
    	elif list1[i] == '[' and list1[i+1] == ']':
        	list1.remove(list1[i])
        	list1.remove(list1[i])
        	i = 0
    	elif list1[i] == '(' and list1[i+1] == ')':
        	list1.remove(list1[i])
        	list1.remove(list1[i])
        	i = 0
    	elif list1[i] == '}' or list1[i] == ']' or list1[i] == ')':
        	break
    	else:
        	i += 1
    if len(list1) == 0:
    	return True
    else:
    	return False
	
	# if (list1st1.count('(') == list1.count(')') and list1.count('{') == list1.count('}') and list1.count('[') == list1.count(']')) == True:
	# 	return True
	# else:
	# 	return False
