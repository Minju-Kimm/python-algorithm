def power(a):
    return a*a


def solution():
    for i in range(1, 400):
        for j in range(i + 1, 400):
            k = 400 - i - j
            if power(k) == power(i) + power(j):
                print(i * j * k)


solution()