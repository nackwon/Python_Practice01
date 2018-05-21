
arr = [str(count) for count in range(1, 100)]
count = 0
for i in arr:
    count = (i.count("3") + i.count("6") + i.count("9"))
    if count != 0:
       print(i, "짝"*count)