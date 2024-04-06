numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 여기에 코드를 작성하세요
for i in range((round)(len(numbers) / 2)):
    num = numbers[i]
    numbers[i] = numbers[len(numbers) - 1 - i]
    numbers[len(numbers) - 1 - i] = num
print("뒤집어진 리스트: " + str(numbers))