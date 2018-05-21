

money = int(input("금액을 입력하세요: "))
arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

count = 0
for i in arr:
    count = money // i
    money = money % i
    print(i, "원:", count,"개")
