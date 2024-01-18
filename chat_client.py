import socket
import threading

# 서버로부터 오는 메시지 수신 함수
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("오류가 발생했습니다!")
            client.close()
            break

# 채팅 클라이언트 시작 함수
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))
    print("[채팅 시작] 채팅을 시작합니다.")

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input("")
        client.send(message.encode())

start_client()
