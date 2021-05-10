import cvzone
import time

mySerial = cvzone.SerialObject("COM3", 9600, 1)
while True:
    mySerial.sendData([1, 1, 1, 1, 1])
    time.sleep(2)
    mySerial.sendData([0, 0, 0, 0, 0])
    time.sleep(2)