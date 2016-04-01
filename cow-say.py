COW = r'''
    \   ^__^
     \  (oo)\_______
        (__)\       )\/\
            ||----w |
            ||     ||
'''

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
    			line = line + text[i] + ' '
    			i += 1
    			if i > len(text) - 1:
    				break
    		content.append(line)
    	#print(content)
    	m = max(len(i) for i in content)
    	#print(m)
    	top = ' ' + '_' * (m+2)
    	bot = ' ' + '-'* (m+2)
    	content2 = []
    	for i in range(len(content)) :
        	if i == 0:
                #line = '/ '
        		content2.append('/ ' + content[i] + ' ' * (m-len(content[i])) + ' \\' )
        	elif i == len(content)-1:
        		content2.append('\\ ' + content[i] + ' ' * (m-len(content[i])) + ' /' )
        	else:
        		content2.append('| ' + content[i] + ' ' * (m-len(content[i])) + ' |' )
    #print(text)
    #print(content)
    	content2 = '\r\n'.join(content2)
    #print(content2)
    return '%s\r\n%s\r\n%s%s' %(top,content2,bot,COW)
    
    #return content
print(cowsay('A longtextwithonlyonespacetofittwolines.'))
print(cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do ''eiusmod tempor incididunt ut labore et dolore magna aliqua.'))
print(COW)
print(cowsay("spaces                                                                     inside"))
