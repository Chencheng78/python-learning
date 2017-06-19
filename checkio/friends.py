class Friends:
	def __init__(self, connections):
		self.connections = list(connections)

	def add(self, connection):
		con = list(connection)
		count = 0
		for i in self.connections:
			if con[0] in i and con[1] in i:
				count += 1
		if count != 0:
			return False
		else:
			self.connections += (connection, )
			return True

	def remove(self, connection):
		con = list(connection)
		count = 0
		for i in self.connections:
			if con[0] in i and con[1] in i:
				count += 1
		if count != 0:
			self.connections.remove(connection)
			return True
		else:
			return False

	def names(self):
		name = self.connections[0]
		for i in self.connections:
			name = name | i
		return name

	def connected(self, name):
		friends = set()
		for i in self.connections:
			if name in i:
				friends = friends | i
		try:
			friends.remove(name)
		except: pass
		return friends

	def __repr__(self):
		return 'Friends(%s)' %self.connections

f = Friends([{"And", "Or"}, {"For", "And"}])
print(f)
print(f.add({"Or", "And"}))
print(f)
