# https://school.programmers.co.kr/learn/courses/30/lessons/181913

def solution(my_string, queries):
    answer = ''
    for query in queries:
        start = query[0]
        end = query[1]
        # 시작 인덱스부터 종료 인덱스까지의 부분 문자열을 뒤집기
        substring = my_string[start:end+1]
        reversed_substring = substring[::-1]
        # 뒤집은 부분 문자열을 원래 문자열에 대체
        my_string = my_string[:start] + reversed_substring + my_string[end+1:]
    answer = my_string
    return answer