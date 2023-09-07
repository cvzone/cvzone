"""
Serial Module
Uses "pySerial" Package
By: Computer Vision Zone
Website: https://www.computervision.zone/
"""

import serial
import logging
import serial.tools.list_ports

class SerialObject:
    """
    Allow to transmit data to a Serial Device like Arduino.
    Example send $255255000
    """

    def __init__(self, portNo=None, baudRate=9600, digits=1, max_retries=5):
        """
        Initialize the serial object.

        :param portNo: Port Number
        :param baudRate: Baud Rate
        :param digits: Number of digits per value to send
        :param max_retries: Maximum number of retries to connect
        """
        self.portNo = portNo
        self.baudRate = baudRate
        self.digits = digits
        self.max_retries = max_retries

        if self.portNo is None:
            for retry_count in range(1, self.max_retries + 1):
                print(f"Attempt {retry_count} of {self.max_retries} to connect...")
                connected = False
                ports = list(serial.tools.list_ports.comports())
                for p in ports:
                    if "Arduino" in p.description:
                        print(f'{p.description} Connected')
                        self.ser = serial.Serial(p.device)
                        self.ser.baudrate = baudRate
                        connected = True
                        break
                if connected:
                    break
                else:
                    print(f"Attempt {retry_count} failed. Retrying...")

            if not connected:
                logging.warning("Arduino Not Found. Max retries reached. Please enter COM Port Number instead.")
        else:
            for retry_count in range(1, self.max_retries + 1):
                print(f"Attempt {retry_count} of {self.max_retries} to connect...")
                try:
                    self.ser = serial.Serial(self.portNo, self.baudRate)
                    print("Serial Device Connected")
                    break
                except:
                    print(f"Attempt {retry_count} failed. Retrying...")
                    if retry_count >= self.max_retries:
                        logging.warning("Serial Device Not Connected. Max retries reached.")

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
        Retrieve data from the serial device.

        :return: list of data received, or None if an error occurred
        """
        try:
            data = self.ser.readline()
            data = data.decode("utf-8")
            data = data.split('#')
            dataList = []
            [dataList.append(d) for d in data]
            return dataList[:-1]
        except serial.SerialException as se:
            logging.error(f"SerialException: {se}")
        except UnicodeDecodeError as ude:
            logging.error(f"UnicodeDecodeError: {ude}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Initialize the Arduino SerialObject with optional parameters
    # baudRate = 9600, digits = 1, max_retries = 5
    arduino = SerialObject(portNo=None, baudRate=9600, digits=1, max_retries=5)

    # Initialize a counter to keep track of iterations
    count = 0

    # Start an infinite loop
    while True:
        # Increment the counter on each iteration
        count += 1

        # Print data received from the Arduino
        # getData method returns the list of data received from the Arduino
        print(arduino.getData())

        # If the count is less than 100
        if count < 100:
            # Send a list containing [1] to the Arduino
            arduino.sendData([1])
        else:
            # If the count is 100 or greater, send a list containing [0] to the Arduino
            arduino.sendData([0])

        # Reset the count back to 0 once it reaches 200
        # This will make the cycle repeat
        if count == 200:
            count = 0

######### ARDUINO CODE ##############

# #include <cvzone.h>
#
# SerialData serialData(1,1); //(numOfValsRec,digitsPerValRec)
# /*0 or 1 - 1 digit
# 0 to 99 -  2 digits
# 0 to 999 - 3 digits
#  */
# //SerialData serialData;   // if not receving only sending
#
#
# int sendVals[2]; // min val of 2 even when sending 1
# int valsRec[1];
#
# int x = 0;
#
# void setup() {
#
# serialData.begin(9600);
# pinMode(13,OUTPUT);
# }
#
# void loop() {
#
#   // ------- To SEND --------
#   x +=1;
#   if (x==100){x=0;}
#   sendVals[0] = x;
#   serialData.Send(sendVals);
#
#   // ------- To Recieve --------
#   serialData.Get(valsRec);
#   digitalWrite(13,valsRec[0]);
#
# }