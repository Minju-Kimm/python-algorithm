num = [80,75,55]
sum = 0
for i in num:
    sum += i
print(int(sum/len(num)))

pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd) #연월일 부분 출력
print(num) #숫자 부분 출력

print(pin[7])

a = "a:b:c:d"
a.replace(":", "#")
print(a)

a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result) #Life is too short

a = (1,2,3)
a = a + (4,)
print(a)

#3번 -> 딕셔너리의 키에 리스트를 쓸 수 없다

a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

a = b = [1,2,3]
a[1] = 4
print(b)