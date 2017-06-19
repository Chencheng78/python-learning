def namelist(names):
	out = ''
	for i in range(len(names)-2):
		out = out + names[i]['name'] + ', '
	if len(names) - 2 >= 0:
			out = out + names[len(names)-2]['name'] + ' & '
	if len(names) - 1 >= 0:
		out = out + names[len(names)-1]['name']
	return out

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
print(namelist([ {'name': 'Bart'} ]))
print(namelist([]))