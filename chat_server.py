import socket
import threading

clients = set()  # 연결된 클라이언트를 관리하기 위한 세트

# 클라이언트 처리 함수
def handle_client(conn, addr):
    print(f"[새 연결] {addr}가 연결되었습니다.")
    
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break  # 클라이언트로부터 메시지 수신이 안 될 경우 연결 종료

            print(f"[{addr}] {message}")
            broadcast_message = f"[{addr}] {message}".encode()

            # 연결된 모든 클라이언트에게 메시지 전송
            for client in clients:
                if client != conn:  # 메시지를 보낸 클라이언트 제외
                    client.sendall(broadcast_message)
        except Exception as e:
            print(f"{addr}와의 연결에서 오류 발생: {e}")
            break
    
    conn.close()
    clients.remove(conn)

# 서버 시작 함수
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen()
    print("[서버 시작] 연결을 기다립니다...")

    while True:
        try:
            conn, addr = server.accept()
            clients.add(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[현재 연결 수] {len(clients)}")
        except KeyboardInterrupt:
            print("\n서버를 종료합니다.")
            for client in clients:
                client.close()
            server.close()
            break

start_server()