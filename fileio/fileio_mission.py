import pickle

def emp_process():
    emp_list = {}

    while True:
        prompt = '''
*** 직원 정보 관리 서비스 ***
1. 새 직원정보 추가
2. 직원정보 삭제
3. 전체 출력
4. 파일에 저장
5. 파일로부터 읽기
9. 종료
'''
        print(prompt)
        choice = input("번호 선택: ")

        if choice == '1':
            empid = input("사번: ")
            empname = input("이름: ")
            empno = input("주민번호: ")
            email = input("이메일: ")
            phone = input("전화번호: ")
            salary = int(input("급여: "))
            job = input("직급: ")
            dept = input("부서: ")

            emp_list[empid] = [empid, empname, empno, email, phone, salary, job, dept]

        elif choice == '2':
            empid = input("삭제할 사번: ")
            if empid in emp_list:
                del emp_list[empid]
                print(f"{empid} 번 사번의 직원 정보가 삭제되었습니다.")
            else:
                print("없는 사번입니다.")

        elif choice == '3':
            for k, v in emp_list.items():
                print(k, ":", v)

        elif choice == '4':
            filename = input("파일명: ")
            with open(filename, 'wb') as f:
                pickle.dump(emp_list, f)
            print(f"{filename} 파일에 저장되었습니다.")

        elif choice == '5':
            filename = input("파일명: ")
            with open(filename, 'rb') as f:
                emp_list = pickle.load(f)
            print("파일에서 불러오기 완료")

        elif choice == '9':
            print("프로그램 종료")
            break