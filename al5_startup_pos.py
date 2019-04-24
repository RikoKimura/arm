# coding: UTF-8

# 2017-05-26 by scharette
# very basic example of AL5 + Python

# obtain required libraries
import serial

# create and open a serial port
sp = serial.Serial('/dev/ttyUSB0', 9600)
#sp = serial.Serial('COM3', 9600)


# set the arm to default centered position
#sp.write("#0 P1500\r".encode()) # 丸いとこの回転
#sp.write("#1 P1500\r".encode()) # 一番下の肩
#sp.write("#2 P1500\r".encode()) # ひじ
#sp.write("#3 P1500\r".encode()) # 手首の上下
#sp.write("#4 P1800\r".encode()) #　指
#sp.write("#5 P1500\r".encode())

#sp.write("#5 P1800\r".encode()) # 手首の回転
#sp.write("#3 P1000\r".encode())

joint = 4
val = 800+1000

cmd = "#{0} P{1}\r".format(str(joint), str(val))

sp.write(cmd.encode())

print(cmd.encode())
