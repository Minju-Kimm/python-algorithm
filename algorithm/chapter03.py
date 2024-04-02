#Q-1
#"shirt"

#Q-2
result = 0
i = 1
while i <= 1000:
    if(i % 3 == 0):
        result += i
    i += 1
print(result)

#Q-3
i = 0
while True:
    i += 1
    if i > 5: break
    print("*" * i)

#Q-4
for i in range(1,101):
    print(i)

#Q-5
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

#Q-6
numbers = [1,2,3,4,5]
result = [num*2 for num in numbers if num % 2 == 1]

marks= [90, 25, 67, 45, 80]
for num in range(len(marks)):
    if marks[num] < 60:
        continue
    print("%d번 학생은 합격 목걸이를 드립니다." %(num+1))

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print("")

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

result = [num * 3 for num in a]
