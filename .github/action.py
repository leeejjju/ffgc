import socket
import struct
import sys


def send_commit_msg(server_ip, server_port, commit_msg):
    # 소켓 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 서버에 접속
        client_socket.connect((server_ip, server_port))

        # MESSAGE에 따라 다른 동작 수행
        if commit_msg.startswith("SUBMIT:"):
            # 숫자 추출
            number_str = commit_msg.split(":")[1]
            number = int(number_str)

            # 숫자를 4바이트로 패킹하여 전송
            packed_number = struct.pack("i", number)
            client_socket.sendall(packed_number)

            # 파일 이름과 파일 내용 전송
            file_name = "../submission.cpp"
            send_file(client_socket, file_name)

        elif commit_msg == "REGISTER":
            # 0을 4바이트로 패킹하여 전송
            packed_number = struct.pack("i", 0)
            client_socket.sendall(packed_number)

            # 파일 이름과 파일 내용 전송
            file_name = "../test_driver.cpp"
            send_file(client_socket, file_name)
            file_name = "../solution.cpp"
            send_file(client_socket, file_name)

        elif commit_msg == "FINISH":
            # -1을 4바이트로 패킹하여 전송
            packed_number = struct.pack("i", -1)
            client_socket.sendall(packed_number)

        else:
            print("not a valid commit msg. abort.")

    finally:
        # 소켓 종료
        client_socket.close()



def send_file(socket, file_name):
    # 파일 크기 계산

    with open(file_name, "rb") as file:
        file_data = file.read()

    # 파일 이름과 파일 크기를 4바이트로 패킹하여 전송
    packed_filename_size = struct.pack("i", len(file_name)) 
    packed_file_size = struct.pack("i", len(file_data))

    socket.sendall(packed_filename_size)
    socket.sendall(file_name.encode())
    socket.sendall(packed_file_size)
    socket.sendall(file_data)

    print("sended " + file_name)


def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py <IP> <PORT> <MESSAGE>")
        return

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    commit_msg = sys.argv[3]

    send_commit_msg(server_ip, server_port, commit_msg)


if __name__ == "__main__":
    main()

