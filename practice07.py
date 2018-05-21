number = input("숫자를 입력하세요. : ")

sum = 0
def check_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return print("숫자가 아닙니다.")

def start(n):
    if n % 2 == 0:
        return 2
    elif n % 2 == 1:
        return 1

if check_number(number):
    n = int(number)
    for i in range(start(n), n+1, 2):
        sum += i
print(sum)



