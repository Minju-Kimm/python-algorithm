def power(a, b):
    result = 1
    print("{}^{} = {}".format(a, 0, result))
    for i in range(b):
        result *= a
        print("{}^{} = {}".format(a, i + 1, result))
    return result

power(2, 10)

# for문으로 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i * j))
    j = 0