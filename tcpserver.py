#!/usr/bin/env python
# coding=UTF-8
'''
@Author: QianXu
@LastEditors: QianXu
@Description: NONE
@Date: 2019-04-22 08:21:33
@LastEditTime: 2019-04-26 19:00:09
'''
import socket

#host = "127.0.0.1"  # 本机IP
hostname=socket.gethostname()
host=socket.gethostbyname_ex(hostname)
host=(str)(host[2][0])
print('本机名{0},本机IP"{1}"'.format(hostname,host))
host=input('HOST:')
port=(int)(input('端口:'))
#host='192.168.3.26'
#port = 40005  # 端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  # 监听
s.listen(1)  # 最大一个连接
conn, addr = s.accept()  # 等待连接 获取客户端IP和端口
print('connected with', addr)

while True:
    data = conn.recv(1024)  # 最多1024字节
    data = data.decode()
    if not data:
        break
    print('receive:', data)
    send = input('send:')
    conn.sendall(send.encode())

conn.close()
s.close()
