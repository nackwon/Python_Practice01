number = input("수를 입력하세요 : ")

def check_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return print("숫자가 아닙니다.")

if check_number(number):
    if int(number) % 2 == 0:
        print("짝수")
    elif int(number) % 2 == 1:
        print("홀수")
    else:
        print("0입니다.")