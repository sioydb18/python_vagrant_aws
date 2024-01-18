import socket
import threading

# 클라이언트 처리 함수
def handle_client(conn, addr):
    print(f"[새 연결] {addr}가 연결되었습니다.")
    
    while True:
        message = conn.recv(1024).decode()
        if not message:
            break

        print(f"[{addr}] {message}")
        broadcast_message = f"[{addr}] {message}".encode()

        # 연결된 모든 클라이언트에게 메시지 전송
        for client in clients:
            client.sendall(broadcast_message)
    
    conn.close()

# 채팅 서버 시작 함수
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen()
    print("[서버 시작] 연결을 기다리는 중...")

    while True:
        conn, addr = server.accept()
        clients.add(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

clients = set()
start_server()
