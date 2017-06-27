# -*- coding:utf-8 -*-
import serial
import time


class Myserial:

    def __init__(self, port, baudrate, timeout=0):
        self.timeout = timeout
        self.port = port
        self.baudrate = baudrate

    def connect(self):
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        except Exception as e:
            print e
            return 0
        else:
            if self.connection.isOpen():
                print '%s is connected successfully!' % self.port
                return 1

    def disconnect(self):
        if self.connection.isOpen():
            self.connection.close()
            print '%s is closed!' % self.port
            return 1
        else:
            print 'Error: Port: %s is not connected!' %self.port
            return 0

    def send_command(self, cmd):
        self.connection.write('\r')
        self.connection.flush()
        self.connection.write(cmd + '\r')
        return 1

    def read_output(self):
        out = ''
        time.sleep(0.5)
        while self.connection.inWaiting() > 0:
            #time.sleep(0.2)
            out += self.connection.read(1)
        return out
        #return self.connection.read(1000)

    def K3C_serial_login(self, username, password):
        self.send_command(username)
        time.sleep(0.5)
        self.send_command(password)

if __name__ == '__main__':
    ser = Myserial('com3', 115200, timeout=1)
    s = ser.connect()
    while 1:
        enter = raw_input('K3C#')
        if enter == 'exit':
            break
        else:
            ser.send_command(enter)
            receive = ser.read_output()
            print receive
    ser.disconnect()


