print("숫자를 입력하세요")
temp = 0

for i in range(1, 6):
    number = int(input("숫자 : ").strip())
    if temp < number:
        temp = number

print("최대값은 %d 입니다." % temp)