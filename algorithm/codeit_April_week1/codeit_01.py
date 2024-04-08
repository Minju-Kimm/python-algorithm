# floor division(버림 나눗셈)
print(8 // 3) ##2

# round 함수 -> 반올림
print(round(3.14132324, 2))

print("'응답하라 1988'은 많은 시청자들에게 사랑을 받은 드라마예요.")
print("데카르트는 \"나는 생각한다. 고로 존재한다.\"라고 말했다.")

print("영화 '신세계'에서 \"드루와~\"라는 대사가 유행했다.")

# 형변환
print(int(1.4))
print(float(3))
print(int("30"))
print(str(3) + str(5)) # 35

#string_formatting
year = 2024
month = 4
day = 3

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day)) # 오늘은 2024년 4월 3일입니다.

# 문자열 포매팅 실습
wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5, wage * 5, "달러"))  # 여기에 코드를 작성하세요

# "1시간에 5710.8원 벌었습니다." 출력
print("{}시간에 {:.1f}{} 벌었습니다.".format(1, wage * 1 * exchange_rate, "원"))  # 여기에 코드를 작성하세요

# "5시간에 28554.0원 벌었습니다." 출력
print("{}시간에 {:.1f}{} 벌었습니다.".format(5, wage * 5 * exchange_rate, "원"))  # 여기에 코드를 작성하세요

# 불린형
print(True and True) # True
print(False or False) # False
print(not True) # False
print(2 > 1) # True
print(3 == 3) # True

# type 함수
print(type(3)) # <class 'int'>
print(type(3.0)) # <class 'float'>
print(type("wow")) # <class 'str'>

def hello():
    print("hello")

print(type(hello)) # <class 'function'>
print(type(print)) # 파이썬 내장 함수 -> <class 'builtin_function_or_method'>

# return과 print 차이 실습
def first():
    message = "코드잇"
    return message


def second():
    message = "codeit"
    print(message)


def third():
    message = None
    print(message)
    return message


# 테스트 코드
print(first())
second()
print(third())

# while 반복문 사용하여 1 이상 100 이하의 짝수 모두 출력하기
i = 1
while i <= 100:
    if i % 2 == 0: print(i)
    i += 1

# while 문을 사용 하여, 100 이상의 자연수 중 가장 작은 23의 배수를 출력해 보세요.
i = 100
while i % 23 != 0:
    i += 1
print(i)

# 학점 계산기
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90: print("A")
    elif total >= 80: print("B")
    elif total >= 70: print("C")
    elif total >= 60: print("D")
    else: print("F")


# while문과 if문을 활용하여, 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.
i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)


# while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 코드를 작성해 보세요.
i = 1
result = 0
while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        result += i
    i += 1
print(result)

# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 코드를 작성해 보세요.
i = 1
count = 0
while i <= 120:
    if 120 % i == 0:
        count += 1
        print(i)
    i += 1
print("120의 약수는 총 {}개입니다.".format(count))

