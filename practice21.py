
def sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum(1, 12))
print(sum(1,2,3,4,5,6,1111))