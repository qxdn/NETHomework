#!/usr/bin/env python
# coding=UTF-8
'''
@Author: QianXu
@LastEditors: QianXu
@Description: NONE
@Date: 2019-05-06 21:54:30
@LastEditTime: 2019-05-06 22:04:56
'''
import socket
 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket.SOCK_DGRAM UDP
# 绑定 客户端口和地址:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
    # 接收数据 自动阻塞 等待客户端请求:
    data, addr = s.recvfrom(1024) #recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端
    print(data.decode())
    data=input('send:')
    s.sendto(data.encode(), addr) 