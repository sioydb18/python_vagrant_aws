import psutil
import time
import argparse

def monitor_process(pid, interval=10):
    """
    프로세스의 메모리 사용량을 모니터링합니다.
    
    :param pid: 모니터링할 프로세스 ID.
    :param interval: 체크 간격(초 단위).
    :cmd -> netstat -ano로 PID 확인
    :실행 예:python monitor_process.py <PID> --interval 10
    """
    try:
        process = psutil.Process(pid)  # PID로 프로세스 객체 생성
        while True:
            mem_info = process.memory_info()  # 메모리 정보 가져오기
            # 메모리 사용량을 MB 단위로 출력
            print(f"[PID: {pid}] 메모리 사용량: {mem_info.rss / 1024 ** 2:.2f} MB")
            time.sleep(interval)  # 지정된 간격으로 대기
    except psutil.NoSuchProcess:
        print(f"PID {pid}에 해당하는 프로세스가 존재하지 않습니다.")
    except KeyboardInterrupt:
        print("모니터링 중지.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='프로세스의 메모리 사용량을 모니터링합니다.')
    parser.add_argument('pid', type=int, help='모니터링할 프로세스 ID(PID).')
    parser.add_argument('--interval', type=int, default=10, help='메모리 체크 간격(초 단위).')

    args = parser.parse_args()
    monitor_process(args.pid, args.interval)