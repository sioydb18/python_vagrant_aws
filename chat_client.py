import socket
import threading

# 서버로부터 메시지를 받아 출력하는 함수
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(message)
            else:
                break  # 서버로부터 정상적인 메시지 수신이 안 될 경우 연결 종료
        except Exception as e:
            print("오류 발생:", e)
            break

# 클라이언트 시작 함수
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(("localhost", 12345))  # 서버에 연결 시도
    except ConnectionRefusedError:
        print("서버에 연결할 수 없습니다.")
        return

    print("[채팅 시작] 채팅을 시작합니다.")

    # 서버로부터 메시지를 받기 위한 스레드 시작
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    try:
        while True:
            message = input("")
            if message.lower() == 'quit':  # 'quit' 입력 시 클라이언트 종료
                break
            client.send(message.encode())  # 메시지를 서버로 전송
    except KeyboardInterrupt:
        pass  # Ctrl+C 누를 시 예외 처리
    finally:
        print("연결을 종료합니다.")
        client.close()

start_client()