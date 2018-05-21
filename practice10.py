deposit = 0
while True:
    print("="*35)
    print("  1.예금 | 2.출금 | 3.잔고 | 4.종료")
    print("="*35)
    select_number = input("선택>")

    if select_number == "1":
        number = int(input("예금액>"))
        deposit += number
    elif select_number == "2":
        number = int(input("출금액>"))
        deposit -= number
    elif select_number == "3":
        print("잔고액>",deposit)
    elif select_number == "4":
        print("프로그램 종료")
        break
    else:
        print("다시 입력해 주세요")
