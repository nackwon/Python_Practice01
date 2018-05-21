input_number = input("숫자 5개를 , 로 구분하여 입력하세요")

number = input_number.split(",")
sum = 0
for i in range(0,5):
    sum += int(number[i])
aver = float(sum / len(number))
print(aver)