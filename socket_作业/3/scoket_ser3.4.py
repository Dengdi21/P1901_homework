import socket
from threading import Thread


def pel_chat_server():
    people_list = []
    sev = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('127.0.0.1', 60024)
    sev.bind(addr)
    sev.listen(5)
    
    while 1:
        conn, conn_addr = sev.accept()
        people_list.append(conn)
        
        net = Thread(target=wechat, args=(conn, conn_addr, people_list))
        net.start()

# for i in people_list:
#     i.start()


def wechat(conn, connaddr, people_list):
    while 1:
        msg = conn.recv(65535)
        print('{}发来消息：{}'.format(connaddr, msg))
        re_msg = "\n{}发来消息：{}".format(connaddr, msg)
        # conn.send(re_msg.encode())
        
        for j in people_list:
            j.send(re_msg.encode())


def main():
    pel_chat_server()


if __name__ == '__main__':
    main()
