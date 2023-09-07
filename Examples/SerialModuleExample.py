from cvzone.SerialModule import SerialObject

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