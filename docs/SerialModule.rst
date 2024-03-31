Serial Module
=============

Overview
--------
The Serial Module facilitates communication between Python scripts and serial devices such as Arduino boards. It leverages the "pySerial" package to transmit data to and from serial devices, enabling a wide range of applications in robotics, home automation, and interactive projects.

Dependencies
------------
- serial
- logging

Features
--------
- Automatic detection and connection to Arduino devices.
- Customizable connection settings including baud rate, data precision, and connection retries.
- Data transmission to serial devices with specified digit formatting.
- Data reception from serial devices with error handling.

Class: SerialObject
-------------------

Initialization
~~~~~~~~~~~~~~
.. code-block:: python

    def __init__(self, portNo=None, baudRate=9600, digits=1, max_retries=5):
        """
        Initializes the SerialObject with connection parameters.

        :param portNo: String, specifies the port number. If None, attempts to auto-detect Arduino devices.
        :param baudRate: Integer, sets the baud rate for serial communication.
        :param digits: Integer, defines the number of digits per value to send.
        :param max_retries: Integer, specifies the maximum number of connection attempts.
        """

Methods
-------

**sendData**
.. code-block:: python

    def sendData(self, data):
        """
        Transmits data to the connected serial device.

        :param data: List of integers, the data to send to the device.
        :return: Boolean, True if data was successfully sent, False otherwise.
        """

**getData**
.. code-block:: python

    def getData(self):
        """
        Retrieves data from the serial device.

        :return: List of strings representing the data received, or None if an error occurred.
        """

Example Usage
-------------
The following example demonstrates initializing a `SerialObject` for communication with an Arduino, sending data based on a counter value, and receiving data from the Arduino:

.. code-block:: python

    if __name__ == "__main__":
        arduino = SerialObject(baudRate=9600, digits=1, max_retries=5)
        count = 0

        while True:
            count += 1
            print(arduino.getData())

            if count < 100:
                arduino.sendData([1])
            else:
                arduino.sendData([0])

            if count == 200:
                count = 0

This script attempts to automatically connect to an Arduino device, sends a continuous stream of data based on the count, and prints any data received from the Arduino.

Arduino Code
------------
To complement the Python script, the following Arduino sketch demonstrates a simple serial communication setup:

.. code-block:: cpp

    #include <Arduino.h>
    
    void setup() {
        Serial.begin(9600);
        pinMode(13, OUTPUT);
    }
    
    void loop() {
        if (Serial.available() > 0) {
            int receivedValue = Serial.read();
            digitalWrite(13, receivedValue == '1' ? HIGH : LOW);
        }
    }

This Arduino sketch reads data from the serial port and turns on or off an LED (connected to pin 13) based on the received value.
