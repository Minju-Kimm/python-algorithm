def is_palindrome(word):
    # 여기에 코드를 작성하세요
    for i in range(0, round(len(word)/2)):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True

# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))