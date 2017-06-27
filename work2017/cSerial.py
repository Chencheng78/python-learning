import myserial
import time
import sys
import datetime

def get_current_time():
    current_time = datetime.datetime.now()
    return  current_time.strftime("%H:%M:%S.%f")

class cSerial:

    def __init__(self):
        self.isDebug =  True
        self.timeOut = 0
        pass

    def connect(self, serial_port_number, baud_rate):
        try:
            self.connection = myserial.Serial(serial_port_number, baud_rate, timeout = self.timeOut)
        except:
            info = sys.exc_info()
            if self.isDebug: print "connecting exceptionally" + str(info[0]) + ": " + str(info[1])
            ##self.connection.isOpen()
            return [0, "connecting exceptionally" + str(info[0]) + ": " + str(info[1])]
        else:
            if self.connection.isOpen():
                if self.isDebug: print "connected to " + str(serial_port_number) + " succefully"
                return [0, "connected to " + str(serial_port_number) + " succefully"]
            else:
                return[-1, "connected to " + str(serial_port_number) + " failed"]

    def disconnect(self):
        if self.connection.isOpen():
            self.connection.close()
            if self.isDebug: print "Close serial port successfully"
            return [0, "serial port closed"]
        else:
            if self.isDebug: print "No connection to close"
            return [-1, "No connection to close"]

    def write(self, CMD):
        if not CMD.strip():
            if self.isDebug: print "the CMD: " +CMD
            return [-1, "the input cmd is null"]    
        
        if self.connection.isOpen():
            self.connection.write("\r\n")
            time.sleep(0.2)
            try:
                if self.isDebug: print "[" + get_current_time() + "]-->:" + CMD.strip()
                self.connection.write(CMD.strip() + "\n")
                #self.connection.write("\n")
            except:
                info = sys.exc_info()
                if self.isDebug: print "write to Ser failed: ", info[0],":",info[1]
                return [-1, "write to Serial port exceptionally"]
            return [0, "write to Serial port succefully"]
        else:
             return [-1, "serial handle is Null"]

    def read(self, waiting_interval = 0.2):
        self.rece_data = ""
        self.return_date = ""
        if self.connection.isOpen():
            try:
                while 1:
                    time.sleep(waiting_interval)
                    num_rece_buffer = self.connection.inWaiting()
                    self.rece_data = self.connection.read(num_rece_buffer)
                    #if self.isDebug: print "[rece from Ser] <--:" + self.rece_data
                    if 0 == len(self.rece_data):
                        break
                    else:
                        self.return_date += self.rece_data
            except:
                info = sys.exc_info()
                if self.isDebug: print "read from Ser failed: ", info[0], ":", info[1]
                return [-1, "read from Ser failed"]
            return [0, self.return_date]
        else:
            return [-1, "serial handle is Null"]

    ## return until find the required string or timeout
    def read_until(self, str, timeout = 5, waiting_interval = 0.2):
        '''
        :param str: expected string
        :param waiting_interval: read interval(s),default 0.2
        :param timeout: default 5s
        :return: 0, successfully; 1,timeout; -1,exception
        '''
        self.rece_data = ""
        self.return_data = ""
        self.time_beginnng = time.time()
        if self.connection.isOpen():
            try:
                while 1:
                    time.sleep(waiting_interval)
                    num_rece_buffer = self.connection.inWaiting()
                    self.rece_data = self.connection.read(num_rece_buffer)
                    self.return_data += self.rece_data
                    #if self.isDebug: print "[rece from Ser] <--:" + self.rece_data
                    if -1 != self.rece_data.find(str):
                        return [0, self.return_data]
                    if (time.time() - self.time_beginnng) > timeout:
                        return [1, self.return_data]
            except:
                info = sys.exc_info()
                if self.isDebug: print "read from Ser failed: ", info[0], ":", info[1]
                return [-1, "read from Ser failed", self.return_data]
        else:
            return [-1, "serial handle is Null"]

def main():
    serial_port = "COM3"
    baud_rate = 115200
    cSer_port = cSerial()
    try:
        res = cSer_port.connect(serial_port, baud_rate)
        if res[0]: print "connect to %s with BaudRate %s failed" %(serial_port, baud_rate)
        while True:
            str_cmd = raw_input("root@K3C:")
            cSer_port.write(str_cmd)
            res = cSer_port.read_until("ls")
            if True:
                print "The received data is "  + str(res)
    finally:
        info = sys.exc_info()
        print info[0], ": ", info[1]
        cSer_port.disconnect()


if "__main__" == __name__:
    main()



