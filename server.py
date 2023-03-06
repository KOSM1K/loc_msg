import socket
import _thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print('Server local Ip addres is:', ipaddr)

s.bind((ipaddr, 3030))
s.listen(1)
conn, addr = s.accept()


def send(connection: socket):
    while True:
        connection.sendall(input().encode('utf-8'))


_thread.start_new_thread(send, tuple([conn]))
while True:
    data = conn.recv(1024)
    if len(data.decode('utf-8')) > 0:
        print('\033[36m\033[7m' + data.decode('utf-8') + '\033[0m')
