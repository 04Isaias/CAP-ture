# This program sends a flag to a bluetooth module so that it starts
# recoding a video
# important pins: p4 (TX) p5(RX)

import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))

# val = input("select Port: COM")  # select port to connect to
val = 4  # Andrew's COM is 4.

# for x in range(0, len(portList)):
#     if portList[x].startswith("COM" + str(val)):
#         portVar = "COM" + str(val)
#         print(portList[x])

portVar = "COM" + str(val)

serialInst.baudrate = 115200
serialInst.port = portVar
serialInst.open()


def record():
    count = 0
    flag = input("send flag to openMV: ")
    # serialInst.write(flag.encode('utf-8'))
    if flag == 'exit':
        exit()
    if flag == '1':
        serialInst.write(flag.encode('utf-8'))
        flag = 0
    while 1:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            packet = packet.decode('utf')
            count += 1
            if count == 2:
                break
            print(packet)

    print("Recording Finished.")
