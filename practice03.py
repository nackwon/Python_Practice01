def gugudan():
    for i in range(1, 10):
        for j in range(2, 10):
            print("%d * %d = %d" % (j, i, i * j), end="\t")
        print(end='\n')

gugudan()