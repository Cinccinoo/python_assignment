from loop.while_mission import sungjuk_process
from fileio.fileio_mission import emp_process

def menu():
    while True:
        prompt = '''
*** 파이썬 과제 1 ***
1. while 실습문제
2. fileio 실습문제
9. 과제 실행 테스트 끝내기
'''
        print(prompt)
        choice = input("번호 선택: ")

        if choice == '1':
            sungjuk_process()
        elif choice == '2':
            emp_process()
        elif choice == '9':
            print("프로그램 종료")
            break
        else:
            print("잘못 입력함")

if __name__ == "__main__":
    menu()