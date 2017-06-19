
def checkio(ip):
	ip_bin = []
	subnet = 0
	for i in range(0,len(ip)):
		addr = ip[i].split(".")
		addr0 = bin(int(addr[0]))
		addr1 = bin(int(addr[1]))
		addr2 = bin(int(addr[2]))
		addr3 = bin(int(addr[3]))


		ip_bin.append(('0'*(10-len(addr0)) + addr0[2:]) + ('0'*(10-len(addr1))+ addr1[2:]) + ('0'*(10-len(addr2))+ addr2[2:]) + ('0'*(10-len(addr3))+ addr3[2:]))

	#print(ip_bin)
	for i in range(0,len(ip_bin[0])):
		check = []
		for j in range(0,len(ip_bin)):
			check.append(ip_bin[j][i])
			#a = ip_bin[j][i]
			#b = ip_bin[j][0]
			#if ip_bin[j][i] == ip_bin[j][0]:
		if len(set(check)) == 1:
			subnet+=1
		else:
			break
	ip_bin1 = ip_bin[0][0:subnet] + '0' * (32-subnet)
	#print subnet

	ip_str = str(int(ip_bin1[0:8],2)) + '.' + str(int(ip_bin1[8:16],2)) + '.' + str(int(ip_bin1[16:24],2)) + '.' + str(int(ip_bin1[24:32],2))
	# list_ip = list(ip_bin1)
	# for i in range(8,32,8):
	# 	list_ip.insert(i,'.')
	# ip_bin2 = ''.join(list_ip).split('.')
	# ip_str = 
		#print(check)	
	return (ip_str + '/' + str(subnet))
	#return ip_bin1
print(checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]))
print(checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]))
print(checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]))


