스탠다드 라이브러리에 있는 random 모듈은 랜덤으로 숫자를 생성하는 다양한 함수들을 제공합니다.


```python
import random
```

# randint() 함수

- `randint()` 함수는 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수. 
- `randint(a, b)`를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴한다


```python
import random

print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
```
```text
8
3
6
6
2
```

1 이상 20 이하의 정수 다섯 개를 출력함.

# uniform() 함수
- 두 수 사이의 랜덤한 소수를 리턴하는 함수
- `randint()` 함수와 다른 것은 리턴하는 값이 정수가 아니라 **소수라는 점**
- `uniform(a, b)`를 하면, a ≤ N ≤ b를 만족하는 어떤 **랜덤한 소수 N**을 리턴

```python
import random

print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
```
```text
0.08811632754196952
0.599056286966887
0.03005761564442677
0.45302183459579204
0.5120418463594933
```
0 이상, 1 이하의 수 다섯 개를 출력했는데요. 보시다시피 매번 다른 랜덤한 수가 출력되었습니다. 여러분이 실행하면 아마 또다른 결과가 나오겠죠?