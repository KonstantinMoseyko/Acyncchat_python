from socket import *


def server_main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('localhost', 10000))
    s.listen(5)

    client, addr = s.accept()
    print('Получаем запрос на соединение: ', addr)

    while True:
        data = client.recv(10000)
        decoded_data = data.decode('utf-8')
        print('Было получено сообщение: ', decoded_data)
        if decoded_data == 'close':
            client.close()
            return

        msg = 'Сообщение получено'
        client.send(msg.encode('utf-8'))


if __name__ == '__main__':
    server_main()
    try:
        server_main()
    except Exception as e:
        print(e)    
