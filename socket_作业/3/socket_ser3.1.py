# 书写一个socket服务器和客户端代码,要求客户端读取一个jpg或者png的媒体文件,
# 然后发送给服务器,服务器接受并保存在磁盘上面(位置随意)

# 服务端代码

import socket
import os

dir_name = os.path.dirname(__file__)

jpg_name = os.path.join(dir_name, '1_copy.png')

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('127.0.0.1', 60000)
ss.bind(addr)

ss.listen(5)
conn, addr = ss.accept()

b_file = b""

while 1:
    msg = conn.recv(65535)
    if not msg:
        break
    b_file += msg

with open(jpg_name, 'wb') as f:
    f.write(b_file)

conn.close()
ss.close()

