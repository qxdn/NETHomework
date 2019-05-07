#!/usr/bin/env python
# coding=UTF-8
'''
@Author: QianXu
@LastEditors: QianXu
@Description: NONE
@Date: 2019-04-22 08:18:48
@LastEditTime: 2019-05-06 22:16:19
'''

import socket
import sys
'''
客户端的代码
'''
#IP = '127.0.0.1'  # IP地址 调试
#IP='192.168.3.26'
#port = 40005  # 端口
hostname=socket.gethostname()
IP=socket.gethostbyname_ex(hostname)
IP=(str)(IP[2][0])
print('本机名{0},本机IP"{1}"'.format(hostname,IP))
IP=input('IP:')
port=(int)(input('端口:'))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((IP, port))  #连接
except Exception:
    print('server not found or not connect')
    sys.exit(0)  # 退出

while True:
    send = input('send:')
    s.sendall(send.encode())
    data = s.recv(1024)  #最多1024字节
    data = data.decode()
    print('recieved:', data)
    if send.lower() == '1':  # 发送1结束连接
        break
s.close()  # 关闭
