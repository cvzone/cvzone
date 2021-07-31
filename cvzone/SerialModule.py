"""
Serial Module
Uses "pySerial" Package
By: Computer Vision Zone
Website: https://www.computervision.zone/
"""

import serial
import time
import logging
import serial.tools.list_ports

class SerialObject:
    """
    Allow to transmit data to a Serial Device like Arduino.
    Example send $255255000
    """
    def __init__(self, portNo=None, baudRate=9600, digits=1):
        """
        Initialize the serial object.
        :param portNo: Port Number.
        :param baudRate: Baud Rate.
        :param digits: Number of digits per value to send
        """
        self.portNo = portNo
        self.baudRate = baudRate
        self.digits = digits
        connected = False
        if self.portNo is None:
            ports = list(serial.tools.list_ports.comports())
            for p in ports:
                if "Arduino" in p.description:
                    print(f'{p.description} Connected')
                    self.ser = serial.Serial(p.device)
                    self.ser.baudrate = baudRate
                    connected = True
            if not connected:
                logging.warning("Arduino Not Found. Please enter COM Port Number instead.")

        else:
            try:
                self.ser = serial.Serial(self.portNo, self.baudRate)
                print("Serial Device Connected")
            except:
                logging.warning("Serial Device Not Connected")


    def sendData(self, data):
        """
        Send data to the Serial device
        :param data: list of values to send
        """
        myString = "$"
        for d in data:
            myString += str(int(d)).zfill(self.digits)
        try:
            self.ser.write(myString.encode())
            return True
        except:
            return False

    def getData(self):
        """
        :param numOfVals: number of vals to retrieve
        :return: list of data received
        """
        data = self.ser.readline()
        data = data.decode("utf-8")
        data = data.split('#')
        dataList = []
        [dataList.append(d) for d in data]
        return dataList[:-1]

def main():
    arduino = SerialObject()
    while True:
        arduino.sendData([1, 1, 1, 1, 1])
        time.sleep(2)
        arduino.sendData([0, 0, 0, 0, 0])
        time.sleep(2)


if __name__ == "__main__":
    main()
