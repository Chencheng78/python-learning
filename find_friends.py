
'''
def check_connection(network,f1,f2):
	connection = ()
	count = 0
	for i in network:
		if connection == ():
			connection.append(i.split('-'))
		else:
			for j in (0,count):
				if i.split('-')[0] in connection[j] or i.split('-')[1] in connection[j] :
					connection[j].append(i.split('-')[0])
					connection[j].append(i.split('-')[1])
				else:
					connection.append(i.split('-'))
					count+=1
	return connection
'''
def check_connection(network,f1,f2):
	connection = []
	visited = set()
	future = []
	for i in network:
		connection.append(i.split('-'))
	for i in range(0,len(connection)):
		visited.add(f1)
		if f1 in connection[i]:
			link = connection[i]
			link.remove(f1)
			future.append(link[0])
	while future != set():
		for i in range(0,len(future)):
			visited.add(future[i])
			for j in range(0,len(connection)):
				if future[i] in connection[j]:
					link = connection[j]
					link.remove(future[i])
					if link != []:
						future.append(link[0])

	return visited
print(check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
	"scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
"scout2", "scout3"))


