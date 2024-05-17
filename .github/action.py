import sys

def main():
    # 명령줄 인자로 받은 커밋 메시지 출력
    commit_message = sys.argv[1]
    print("Commit message:", commit_message)

if __name__ == "__main__":
    main()

