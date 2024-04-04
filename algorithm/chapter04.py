def add(a, b):
    print("%d와 %d를 더하면 %d입니다."%(a, b, a+b))
a = 3
b = 10
add(a, b)

print(add(3, 4))

def say():
    print("wow")

say()

def add_many(*args):
    result = 0
    for i in args:
        result += i
    print(result)

add_many(3, 4, 5, 6, 10, 11, 12, 13)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, name='Minju', age=20)

add = lambda a, b: a+b
result = add(3, 4)
print(result)

a = input()
print(a)

b = input("숫자 입력하셔요: ")
print(b)
