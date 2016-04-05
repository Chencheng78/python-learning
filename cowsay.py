def cowsay(text):
	COW = r'''
		\   ^__^
		 \  (oo)\_______
			(__)\       )\/\
				||----w |
				||     ||
'''
	text = text.split(' ')
	while '' in text:
		text.remove('')
	text = ' '.join(text)
	if len(text) <= 39:
		top = ' ' + '_' * (len(text)+2)
		bot = ' ' + '-'* (len(text)+2)
		content2 = '< ' + text + ' >'
	else:
		text = text.split(' ')
		i = 0
		content = []
		while i < len(text):
			line = ''
			while len(line) + len(text[i]) <= 39:
				line = line + text[i]+' '
				i += 1
				if i > len(text) - 1:
					break
			content.append(line)
		m = max(len(i) for i in content)
		top = ' ' + '_' * (m+1)
		bot = ' ' + '-'* (m+1)
		content2 = []
		for i in range(len(content)) :
			if i == 0:
				#line = '/ '
				content2.append('/ ' + content[i] + ' ' * (m-len(content[i])) + '\\' )
			elif i == len(content)-1:
				content2.append('\\ ' + content[i] + ' ' * (m-len(content[i])) + '/' )
			else:
				content2.append('| ' + content[i] + ' ' * (m-len(content[i])) + '|' )
		content2 = '\n'.join(content2)
	return '\n%s\n%s\n%s%s' %(top,content2,bot,COW)
	#return '%s'%COW


if __name__ == '__main__':
#These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
		\   ^__^
		 \  (oo)\_______
			(__)\       )\/\
				||----w |
				||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
		\   ^__^
		 \  (oo)\_______
			(__)\       )\/\
				||----w |
				||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
		\   ^__^
		 \  (oo)\_______
			(__)\       )\/\
				||----w |
				||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line


	#assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n.%s.\nRight answer:\n.%s.\n' % (cowsay_one_line, expected_cowsay_one_line)

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
	#assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n.%s.\nRight answer:\n.%s.\n' % (cowsay_two_lines, expected_cowsay_two_lines)

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do ''eiusmod tempor incididunt ut labore et dolore magna aliqua.')
	#assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n.%s.\nRight answer:\n.%s.\n' % (cowsay_many_lines, expected_cowsay_many_lines)

print(cowsay('                    h e     l l o w o r l d'))