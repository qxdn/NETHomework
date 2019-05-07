#!/usr/bin/env python
# coding=UTF-8
'''
@Author: QianXu
@LastEditors: QianXu
@Description: NONE
@Date: 2019-05-04 00:40:33
@LastEditTime: 2019-05-07 12:59:30
'''
import socket
from tkinter import *
from tkinter import ttk
import sys
from threading import Thread
import tkinter.messagebox
import sys

class tcpclient: #tcp客户端
    hostname=None
    IP='127.0.0.1'
    port=8080
    is_close=True
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hostname=socket.gethostname()
        IP=socket.gethostbyname_ex(self.hostname)
        IP=(str)(IP[2][0])
        self.IP=IP
    def tcpclient(self,IP,port):
        self.IP=IP
        self.port=port
    def connect(self):
        try:
            self.s.connect((self.IP, self.port))  #连接
        except Exception:
            #print('server not found or not connect')
            tkinter.messagebox.showerror('ERROR','server not found or not connect')
            sys.exit(0)  # 退出
        self.is_close=False
    def send(self,text):
        self.s.sendall(text.encode())  #发送
    def receive(self,size=1024):
        data = self.s.recv(size)  #默认最多1024字节
        data = data.decode()
        return data
    def close(self):
        self.s.close()
        self.is_close=True

class tcpserver:  #tcp服务器
    hostname=None
    host='127.0.0.1'
    port=8080
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr=None         #客户 IP port
    conn=None        
    is_close=True
    def __init__(self):
        self.hostname=socket.gethostname()
        host=socket.gethostbyname_ex(self.hostname)
        host=(str)(host[2][0])
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host=host
    def tcpserver(self,IP,port):
        self.IP=IP
        self.port=port
    def connect(self):
        self.s.bind((self.host , self.port))  # 监听
        self.s.listen(1)  # 最大一个连接
        self.conn, self.addr = self.s.accept()  # 等待连接 获取客户端IP和端口
        self.is_close=False
        #print('connected with', self.addr)
    def send(self,text):
        self.conn.sendall(text.encode())
    def receive(self,size=1024):
        data = self.conn.recv(size)  # 最多1024字节
        data = data.decode()
        return data
    def close(self):
        self.conn.close()
        self.s.close()
        self.is_close=True
class UDP:   #UDP 自发自收
    hostname=None
    host='127.0.0.1'
    port=8080
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #UDP
    addr=('127.0.0.1',port)         #客户IP port
    is_close=True
    def __init__(self):
        self.hostname=socket.gethostname()
        host=socket.gethostbyname_ex(self.hostname)
        host=(str)(host[2][0])
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host=host
    def udp(self,IP,port):
        self.host=IP
        self.port=port
        self.addr=(IP,port)
    def connect(self):
        self.s.bind((self.host,self.port))
        self.is_close=False
    def send(self,data):
        self.s.sendto(data.encode(),self.addr)
    def receive(self,size=1024):
        data,self.addr=self.s.recvfrom(size)
        data=data.decode()
        return data
    def close(self):
        self.s.close()
        self.is_close=True
        


hostname=socket.gethostname()   #主机名
IP=socket.gethostbyname_ex(hostname) #IP
IP=(str)(IP[2][0])

'''
以下基本为图形界面
'''


root=Tk()
root.title('计算机网络通信 钱旭') #题头
'''
框架
'''
frame1=Frame(root)
frame1.pack(side=LEFT)
frame2=Frame(root)
frame2.pack(side=BOTTOM)
frame3=Frame(root)
frame3.pack(side=TOP)

'''
frame1
'''

'''
选择协议
'''   
def go(*args):   #处理事件，*args表示可变参数  
    pass
    #print(comboxlist.get()) #打印选中的值  
    #print(comboxlist.current())  
comvalue=StringVar()#窗体自带的文本，新建一个值  
comboxlist=ttk.Combobox(frame1,textvariable=comvalue) #初始化  
comboxlist["values"]=("tcp client","tcp server","UDP")  
comboxlist.current(0)  #选择第一个  
comboxlist.bind("<<ComboboxSelected>>",go)  #绑定事件,(下拉列表框被选中时，绑定go()函数)  
comboxlist.pack(expand=YES,fill=X) 

'''
IP
'''
label1=Label(frame1,text='IP')
label1.pack()
entry1=Entry(frame1)
entry1.insert(0,IP)
entry1.pack(expand=YES,fill=X)


'''
端口
'''
label2=Label(frame1,text='端口')
label2.pack()
entry2=Entry(frame1)
entry2.insert(0,'8080')
entry2.pack(expand=YES,fill=X)

'''
连接按键
'''
s=tcpclient()
button1_flag=True


'''
另一个线程
'''
def listen(name):
    '''
    name 无关紧要，因为必需要两个参数
    '''
    global button1_flag
    global s
    global text1
    while True:
        if button1_flag==False:  #需要连接
            if True==s.is_close: #为连接
                IP=entry1.get()
                port=entry2.get()
                port=(int)(port)
                tcp=comboxlist.current()
                if tcp==0:
                    s=tcpclient()
                    s.tcpclient(IP,port)
                    s.connect()
                elif tcp==1:
                    s=tcpserver()
                    s.tcpserver(IP,port)
                    s.connect()
                    data='connect with IP:{0},port:{1}\n'.format(s.addr[0],s.addr[1])
                    text1.insert(INSERT,data)
                elif tcp==2:
                    s=UDP()
                    s.udp(IP,port)
                    s.connect()

            else :
                data=s.receive()
                text1.insert(INSERT,data)
        else:
            if False==s.is_close:
                s.close()
            else:
                pass

    '''
    IP=entry1.get()
    port=entry2.get()
    port=(int)(port)
    tcp=comboxlist.current()
    if tcp==0:
        s=tcpclient()
        s.tcpclient(IP,port)
    else:
        s=tcpserver()
        s.tcpserver(IP,port)
    s.connect()
    while True:
        if button1_flag==False:
            data=s.receive()
            text1.insert(INSERT,data)
        else:
            if False==s.is_close:
                s.close()
            else:
                pass
    '''       
t=Thread(target=listen,args=(666,))
t.start()


def button1_callback():
    global button1_flag
    global s
    if button1_flag==True:
        button1_flag=False
        button1['text']='关闭'
    else:
        button1_flag=True
        button1['text']='连接'
    pass
button1=Button(frame1,text='连接',command=button1_callback)
button1.pack(expand=YES,fill=X)

'''
frame2
'''
'''
发送
'''
label3=Label(frame2,text='发送区')
label3.pack(side=LEFT)

'''
文本输入
'''
text2=Text(frame2)
text2.pack(expand=YES,fill=X)

'''
发送按键
'''
def button2_callback():
    data=text2.get('1.0',END)
    #if not data:
    #    pass
    s.send(data)
button2=Button(frame2,text='发送',command=button2_callback)
button2.pack(side=RIGHT,expand=YES,fill=BOTH)


'''
frame3
'''

'''
接收标签
'''
label4=Label(frame3,text='接收区')
label4.pack(side=LEFT)

'''
接收框
'''
text1=Text(frame3)
text1.pack(expand=YES,fill=X)

mainloop() 
