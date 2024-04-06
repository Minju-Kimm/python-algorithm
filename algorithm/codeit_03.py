# 리스트 함수
numbers = [1, 2, 3, 4, 5]

numbers.append(3)
print(numbers)
# [1, 2, 3, 4, 5, 3]

del numbers[0]
print(numbers)
# [2, 3, 4, 5, 3]

numbers.insert(0, 1)
print(numbers)
# [1, 2, 3, 4, 5, 3]

# 리스트 정렬
sort_list = [3, 10, 28, 1, 86]
new_list = sorted(sort_list, reverse=True)
print(new_list)
sort_list.sort()
print(sort_list)

# 리스트 인덱싱 연습
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1

