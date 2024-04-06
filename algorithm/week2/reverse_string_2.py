# https://school.programmers.co.kr/learn/courses/30/lessons/181905

def solution(my_string, s, e):
    answer = ''
    substring = my_string[s:e + 1]
    reversed_string = substring[::-1]

    my_string = my_string[:s] + reversed_string + my_string[e + 1:]
    answer = my_string
    return answer