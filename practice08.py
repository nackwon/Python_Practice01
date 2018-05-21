import random

print("="*20)
print("  [숫자 맞추기 게임]")
print("="*20)

random_number = random.randint(1, 100)

def shutdown(y):
    if y == "y" :
        print("=" * 20)
        print("[숫자 맞추기 게임 종료]")
        print("=" * 20)
        exit()

while True:
    my_number = int(input("숫자 : "))
    if my_number == random_number:
        print("정답 입니다.")
        shutdown(input("종료하시겠습니까?(y/n)"))
    elif my_number > random_number:
        print("더 낮게")
    elif my_number < random_number:
        print("더 높게")