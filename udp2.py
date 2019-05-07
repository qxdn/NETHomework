#!/usr/bin/env python
# coding=UTF-8
'''
@Author: QianXu
@LastEditors: QianXu
@Description: NONE
@Date: 2019-05-06 21:59:07
@LastEditTime: 2019-05-06 22:02:34
'''
import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
while True:
    data=input('send:')
    # 发送数据:
    s.sendto(data.encode(), ('127.0.0.1', 9999))
    # 接收数据:
    print (s.recv(1024).decode())
s.close()