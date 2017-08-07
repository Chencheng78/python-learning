from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpsersock = socket(AF_INET, SOCK_DGRAM)
udpsersock.bind(ADDR)

while True:
    print 'waiting for message'
    data, addr = udpsersock.recvfrom(BUFSIZ)
    udpsersock.sendto('[%s] %s' %(ctime(), data), addr)
    print '...received from and returned to:', addr

udpsersock.close()
