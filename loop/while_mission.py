def sungjuk_process():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

    while True:
        prompt = '''
*** 원하는 메뉴 번호를 선택하세요. ***
1. 추가
2. 삭제
3. 출력
4. 끝내기
'''
        print(prompt)
        choice = input("번호 선택: ")

        if choice == '1':
            sno = int(input("번호: "))
            sname = input("이름: ")
            score = int(input("점수: "))
            sungjuk_list.append([sno, sname, score])
            print("새로운 학생정보가 추가되었습니다.")

        elif choice == '2':
            print(f"현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.")
            idx = int(input("제거할 아이템 순번: "))

            if 0 <= idx < len(sungjuk_list):
                sungjuk_list.pop(idx)
                print(f"{idx}번 위치의 아이템이 제거되었습니다.")
                print(f"현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.")
            else:
                print("순번이 잘못 입력되었습니다.")

        elif choice == '3':
            for i, item in enumerate(sungjuk_list):
                print(i, ":", item)

        elif choice == '4':
            print("성적관리 프로그램이 종료되었습니다.")
            break