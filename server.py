import socket
import _thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print('Server local Ip address is:', ipaddr)

if input('continue with this ip address? [Y/n]: ').lower() != 'y':
    ipaddr = input('type in target address: ')

port = int(input('type in target port: '))

s.bind((ipaddr, 3030))
print('\033[31m'+'Ready!')
print('Waiting for a connection...'+'\033[0m')

s.listen(1)
conn, addr = s.accept()

print('\033[32m'+'connected!'+'\033[0m')

def send(connection: socket):
    while True:
        connection.sendall(input().encode('utf-8'))


_thread.start_new_thread(send, tuple([conn]))
while True:
    data = conn.recv(1024)
    if len(data.decode('utf-8')) > 0:
        print('\033[36m\033[7m' + data.decode('utf-8') + '\033[0m')
