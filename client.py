import socket
import _thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((input('server\'s local ip: '), int(input('startup server\'s port: '))))
print('\033[32m'+'connected!'+'\033[0m')

def send(connection: socket):
    while True:
        connection.sendall(input().encode('utf-8'))


_thread.start_new_thread(send, tuple([s]))
while True:
    data = s.recv(1024)
    if len(data.decode('utf-8')) > 0:
        print('\033[36m\033[7m' + data.decode('utf-8') + '\033[0m')
