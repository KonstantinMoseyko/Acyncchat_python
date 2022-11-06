from socket import *


def client_main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 10000))

    while True:
        msg = str(input('Введите сообщение серверу: '))
        msg_encoded = msg.encode('utf-8')
        s.send(msg_encoded)
        data = s.recv(1024)
        print('Сервер: ', data.decode('utf-8'))


if __name__ == '__main__':
    client_main()
    try:
        client_main()
    except Exception as e:
        print(e) 