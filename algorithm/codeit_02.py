# 택이의 우승 상금
i = 1988
year = 2016
reward = 50000000
RATE = 0.12

dongil_result = reward
while i < year:
    dongil_result = dongil_result * (1 + RATE)
    i += 1

if dongil_result > 1100000000:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(dongil_result - 1100000000)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(1100000000 - dongil_result)))

# 피보나치 수열
first = 1
second = 1
third = 0
i = 3

print(first)
print(second)

while i <= 50:
    third = first + second
    print(third)
    first = second
    second = third
    i += 1

# 구구단 만들기
i = 1
j = 1

while i <= 9:
    while j <= 9:
        print("{} * {} = {}".format(i, j, i * j))
        j += 1
    i += 1
    j = 1