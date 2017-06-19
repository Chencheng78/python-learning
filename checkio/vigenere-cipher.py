def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
	key = ''
	for i in range(len(old_encrypted)):
		if ord(old_encrypted[i]) - ord(old_decrypted[i]) < 0:
			n = ord(old_encrypted[i]) - ord(old_decrypted[i]) + 26 + 65
		else:
			n = ord(old_encrypted[i]) - ord(old_decrypted[i]) + 65
		n = chr(n)
		key += n
	print(key)
	keyphrase2 = ''
	for i in range(1,len(key)):
		if key[0:i] == key[i:i*2]:
			keyphrase2 = key[0:i]
			break
	print(keyphrase2)
	l1 = []	
	for i in range(1,len(key)):
		if key[0] == key[i]:
			#print(key[0:i])
			l1.append(key[0:i])
	print(l1)
	if l1 != [] and keyphrase2 == '':
		keyphrase = max(l1,key = len)
	elif l1 != [] and (keyphrase2 in l1) and (key in keyphrase2 * (len(key) // len(keyphrase2) +1)):
		keyphrase = keyphrase2
	else:
		keyphrase = key
	print(keyphrase)

	a,b = len(new_encrypted) // len(keyphrase) , len(new_encrypted) % len(keyphrase)
	new_key = keyphrase * a + keyphrase[0:b+1]
	print(new_key)

	new_decrypted=''		
	for i in range(len(new_encrypted)):
		if ord(new_encrypted[i]) - ord(new_key[i]) < 0:
			m = ord(new_encrypted[i]) - ord(new_key[i]) + 26 + 65
		else:
			m = ord(new_encrypted[i]) - ord(new_key[i]) + 65
		m = chr(m)
		new_decrypted += m


	return new_decrypted

# print(decode_vigenere('NOBODYEXPECTSTHESPANISHINQUISITION',
#                            'PVFQNGSZWIEDAHJLWRKVWUOMPACWUPXKYV',
#                            'QBVGHXSTAWFOAQTPFGIWICZEPKXDCSPKXOZAKYNVNSNSSYEVWOHKKXIHKCIVSUWFSEEUQBIPRKXQHKHXKFMGRPRGVMGULEUSTMFVQKXIHGKRQCMBULSHRCAQBVVOLWQBWEYUDCUCCXLWTYIRBMGUPFNILFCIEPNIKHBPCXLKJLVGKAWPTSUDXFQMIUCQCPZXJOASYVYNNJSEVRUSLSTHFNOLFCDFCMSGKUGJKZHGYIFKKQQBRVKVQAALGIIFGHTQCQHKCIDYWB'))
# print(decode_vigenere('HELLO', 'OIWWC', 'ICP'))
# print(decode_vigenere('LOREMIPSUM',
#                            'OCCSDQJEXA',
#                            'OCCSDQJEXA'))
print(decode_vigenere('AAAAAAAAA', 'ABABABABC', 'ABABABABC'))
