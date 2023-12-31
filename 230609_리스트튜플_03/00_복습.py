"""
# 숫자 계산
* 파이썬에서는 숫자의 자료형에 따라 결과가 달라질 수 있음
* 파이썬에서는 숫자를 정수(int), 실수(float), 복소수(complex)로 구분
* 보통 프로그래밍에서는 정수와 실수를 주로 사용
## 정수 계산
### 사칙연산
"""


# 덧셈
print(1+1)
print('덧셈',2033+20311)
# 뺄셈
print('뺄셈 302-123=',302-123)

# 곱셈
print('곱셈 89*54=',89*54)

# 나눗셈
print('나눗셈 72/8=',72/8)

# 실수인 것을 어떻게 알까? -> type 함수 사용
print(type(72/8)) # <class 'flaot'>
print("type(4 / 2)", type(4 / 2))  # <class 'float'>

"""
### 몫 (`//`) 연산자
* 정수끼리 나눗셈 결과가 정수로 나오도록 해야할 때 //로 나눗셈을 하면 됨
* `//`은 버림 나눗셈(floor division)이라고 부르며 나눗셈의 결과에서 소수점 이하는 버림
"""
print("5 / 2 =", 5 / 2, "5 // 2 =", 5 // 2) # 나머지 1이 사라진다


"""* 참고로 실수에 // 연산자를 사용하면 결과는 실수가 나오며 소수점 이하는 버림.
* 따라서 (연산자 앞뒤 숫자 중 하나라도 실수라면) 결과는 항상 `.0`으로 끝남
"""



"""### 나머지 (`%`) 연산자"""
print("5 // 2 =", 5 // 2, "5 % 2 =", 5 % 2)
# 모듈로(modulo) 연산자

"""### 거듭제곱 (`**`) 연산자"""
print("5 * 2 =", 5 * 2, "5 ** 2 =", 5 ** 2)
print("5 ** 0.5 =", 5 ** 0.5)

"""### 값을 정수로 만들기
* 계산 결과가 실수로 나왔을 때 강제로 정수로 만들어야 할 때는 int에 괄호를 붙이고 숫자 또는 계산식을 넣으면 됨
* 특히 int에 문자열을 넣어도 정수로 만들 수 있음. 단, 정수로 된 문자열이라야 함

```
int(숫자)
int(계산식)
int('문자열')
```
"""

# int는 정수(integer)를 뜻하며 값을 정수로 만들어 줌 (소수점 이하는 버림)
# cf) int, long, float, double, ... (수와 관련된 자료형은 많음)
# int, float <- 파이썬에서는...
print(int(3.3), int(5 / 3), int('10'), int("100"))
# print(int("100.100")) -> int에 float(실수)형태의 문자열 넣으면 오류
# print(int("5 / 3")) -> int에 계산식을 담은 문자열을 넣으면 오류
"""### 몫과 나머지 함께 구하기"""
print("5 // 3 =", 5 // 3, ",", "5 % 3 =", 5 % 3)
print("divmod(5, 3) =", divmod(5, 3))

"""## 실수 계산

### 실수끼리의 계산
"""

# 실수끼리의 덧셈
print("3.5 + 2.1 =", 3.5 + 2.1)
# 실수끼리의 뺄셈
print("4.3 - 2.7 =", 4.3 - 2.7)  # 부동소수점 오차
print("2.7 - 1.5 =", 2.7 - 1.5)  # 이런 식으로 소수점 미만의 작은 오차가 생기면 -> 부동소수점 오차
# 실수끼리의 곱셈
print("1.5 * 3.1 =", 1.5 * 3.1)
# 실수끼리의 나눗셈
print("1.5 / 3.1 =", 1.5 / 3.1)
# 몫 연산자, 나머지 연산자, 거듭제곱 연산자...

"""### 실수와 정수 간의 계산
* 실수와 정수를 함께 계산하면 표현 범위가 넓은 실수로 계산됨 (실수가 정수보다 표현 범위가 넓음)
"""



"""### 값을 실수로 만들기
* `float`에 괄호를 붙이고 숫자 또는 계산식을 넣으면 됨
* 특히 `float`에 문자열을 넣어도 실수로 만들 수 있음
* 단, 실수 또는 정수로 된 문자열이라야 함
```
float(숫자)
float(계산식)
float('문자열')
```
"""
print("float(5) =", float(5), "(정수를 넣었을 때)")
print("float(1 + 2) =", float(1 + 2), "(계산식을 넣었을 때)")
print("float('5.3') =", float('5.3'), "소수점을 포함한 숫자가 들어간 문자열")
print("float('5') =", float('5'), "소수점을 포함하지 않은 숫자가 들어간 문자열")
# float에 문자열로 표현된 계산식 넣으면 오류
"""* `float`는 부동소수점(**float**ing point)에서 따왔으며 값을 실수로 만들어줌
* 즉, 실수는 `float` 자료형
"""
print("type(3.5) =", type(3.5))


"""## 괄호 사용하기"""
print("5 + 2 * 3 =", 5 + 2 * 3, ",", "(5 + 2) * 3 = ", (5 + 2) * 3)


"""* 만약 곱셈보다 덧셈을 먼저 계산하고 싶다면 덧셈 부분을 괄호로 묶어주면 됨"""


# 변수와 입력

## 변수 만들기
x = 10
print("x =", x)


"""* `x = 10`이라고 입력하면 10이 들어있는 변수 x가 만들어짐
* 즉, 변수이름 = 값 형식. 이렇게 하면 변수가 생성되는 동시에 값이 할당(저장)

* 변수 이름은 원하는 대로 지으면 되지만 다음과 같은 규칙을 지켜야 함
# https://www.microsoft.com/ko-kr/language
# https://www.deepl.com/translator
> 영문 문자와 숫자를 사용할 수 있음<br>
> 대소문자를 구분함<br>
> 문자부터 시작해야 하며 숫자부터 시작하면 안 됨<br>
> _(밑줄 문자)로 시작할 수 있음 (중간에 들어가도 됨)<br>
> 특수 문자(+, -, *, /, $, @, &, % 등)는 사용할 수 없음<br>
> 파이썬의 키워드(if, for, while, and, or 등)는 사용할 수 없음
"""



"""* 변수에는 숫자뿐만 아니라 문자열도 넣을 수 있음"""
text = 'hello hello'
print("text :", text)

"""### 변수의 자료형 알아내기
* type(변수)
"""



"""* x에는 정수 10이 들어있으므로 int, y에는 문자열 Hello, world!가 들어있으므로 str이라고 나옴
* int는 정수(**int**eger), str은 문자열(**str**ing)에서 따옴
* 즉, 변수의 자료형은 변수에 들어가는 값에 따라 달라짐

### 할당 연산자 `=`
* 수학에서는 =(등호) 기호는 양 변이 같다는 뜻
* 하지만 프로그래밍 언어에서 =는 변수에 값을 할당(assignment)한다는 의미
* 수학의 등호와 같은 역할을 하는 연산자는 `==`(동등연산자)

### 변수 여러 개를 한 번에 만들기
"""
x = 10; y = 20; z = 30; # 할 수는 있는데 파이썬스럽지 X
print(x, y, z)
x, y, z = 10, 20, 30 # 파이썬 스러움 (언팩킹)
print(x, y, z)
"""* 변수이름1, 변수이름2, 변수이름3 = 값1, 값2, 값3 형식으로 변수를 ,(콤마)로 구분한 뒤 각 변수에 할당될 값을 지정해주면 됨
* 변수와 값의 개수는 동일하게 맞춰주어야 하며 나열된 순서대로 값이 할당
* 만약 변수와 값의 개수가 맞지 않으면 에러가 발생
"""



# 변수 여러 개를 만들 때 값이 모두 같아도 된다면?
x = y = z = 10
print(x, y, z)
# 두 변수의 값을 바꾸려면?
x, y = 10, 20
x, y = y, x
print(x, y)
# 빈 변수 만들기
x = None
print(x)
"""* 파이썬에서 None은 아무것도 없는 상태를 나타내는 자료형
* 보통 다른 언어에서는 널(null)이라고 표현

## 변수로 계산하기
"""
a, b = 10, 20
print("a + b =", a + b)
c = a + b
print("a + b = c", c)
"""* 변수 a, b에 숫자를 할당한 뒤에 a와 b의 값을 더해서 변수 c에 할당
* 변수는 변수끼리 계산할 수 있고, 계산 결과를 다른 변수에 할당할 수 있음

### 산술 연산 후 할당 연산자 사용
"""



"""* 변수 한 개에서 값의 변화를 계속 유지하려면 계산 결과를 다시 변수에 저장해야 함"""



"""* 파이썬에서는 변수를 두 번 입력하지 않도록 산술 연산 후 할당 연산자를 제공"""



"""* a에는 10이 들어있고 a += 20을 수행하면 a에는 10과 20을 더한 결과인 30이 들어감
* +=처럼 산술 연산자 앞에 =(할당 연산자)를 붙이면 연산 결과를 변수에 저장(+ =처럼 두 연산자를 공백으로 띄우면 안 됩니다)
* 즉, a += 20은 a = a + 20을 축약한 형태
---
* 덧셈(+=) 외에도 뺄셈(-=), 곱셈(\*=), 나눗셈(/=, //=), 나머지(%=)도 같은 방식
* 똑같이 연산(-, *, /, //) 후 할당(=) 한다는 뜻입
---
* 만들지 않은 변수 d에 10을 더한 후 다시 할당하면 에러가 발생
"""



"""### 부호 붙이기
* 값이나 변수 앞에 양수, 음수 부호를 붙이면 됨
"""



"""## 입력 값을 변수에 저장하기

### input 함수 사용하기
"""
a = input()
print("a에 input한 값 :", a)

"""* 입력한 문자열이 그대로 출력
* 즉, `input` 함수는 사용자가 입력한 값을 가져오는 함수

### input 함수의 결과를 변수에 할당
* `변수 = input()`
"""





"""* 실행을 해보면 '문자열을 입력하세요: '처럼 안내 문구가 먼저 나옴
* 여기에 문자열을 입력한 뒤 엔터 키를 누르면 입력한 그대로 출력
* 즉, 이 문자열은 사용자에게 입력받는 값의 용도를 미리 알려줄 때 사용
* 다른 말로는 프롬프트(prompt)라고도 부름

### 두 숫자의 합 구하기
"""







"""## 입력 값을 변수 두 개에 저장하기
* input 한 번에 값을 여러 개 입력받으려면 input에서 split을 사용한 변수 여러 개에 저장(각 변수는 콤마로 구분)
```
변수1, 변수2 = input().split()
변수1, 변수2 = input().split('기준문자열')
변수1, 변수2 = input('문자열').split()
변수1, 변수2 = input('문자열').split('기준문자열')
```
"""



"""* input에 split을 사용하면 입력받은 값을 공백을 기준으로 분리하여 변수에 차례대로 저장(split은 분리하다, 나누다라는 뜻)
* 문자열 'Hello Python'을 공백을 기준으로 분리하여 'Hello'는 첫 번째 변수 a에 'Python'은 두 번째 변수 b에 저장

### 두 숫자의 합 구하기
"""





"""### map을 사용하여 정수로 변환
* map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환(실수로 변환할 때는 int 대신 float를 넣음)
```
변수1, 변수2 = map(int, input().split())
변수1, 변수2 = map(int, input().split('기준문자열'))
변수1, 변수2 = map(int, input('문자열').split())
변수1, 변수2 = map(int, input('문자열').split('기준문자열'))
```
"""



"""### 입력받은 값을 콤마를 기준으로 분리"""



"""* split(',')과 같이 분리할 기준 문자열을 콤마로 지정하였으므로 '10,20'에서 10은 a, 20은 b에 저장

# 출력

## 값을 여러 개 출력하기
* `print`에는 변수나 값 여러 개를 ,(콤마)로 구분하여 넣을 수 있음
```
print(값1, 값2, 값3)
print(변수1, 변수2, 변수3)
```
"""



"""* print에 변수나 값을 콤마로 구분해서 넣으면 각 값이 공백으로 띄워져서 한 줄로 출력 (값을 여러 개 출력할 때 print 함수를 여러 번 쓰지 않아도 됨)

### sep로 값 사이에 문자 넣기

* 값 사이에 공백이 아닌 다른 문자를 넣고 싶을  때는 print의 sep에 문자 또는 문자열을 지정(sep는 구분자라는 뜻의 **sep**arator에서 따옴)
```
print(값1, 값2, sep='문자 또는 문자열')
print(변수1, 변수2, sep='문자 또는 문자열')
```
"""



"""* sep=', '처럼 콤마와 공백을 넣어주면 1, 2, 3과 같은 형태로 출력 (공백 없이 콤마만 지정해도 됨)
* 또한, sep=''처럼 빈 문자열을 지정하면 각각의 값은 서로 붙어서 출력됨
* 특히 sep에는 'x'와 같은 일반적인 문자도 넣을 수 있음

## 줄바꿈 활용하기
"""

# print에 값을 여러 개 지정하면 한 줄에 모든 값이 출력

# print의 sep에 개행 문자(\n)라는 특별한 문자를 지정하면 값을 한 줄에 하나씩 출력



"""### end 사용하기
* print는 기본적으로 출력하는 값 끝에 \n을 붙임. 그래서 print를 여러 번 사용하면 값이 여러 줄에 출력
"""



"""* print를 여러 번 사용해서 print(1, 2, 3)처럼 한 줄에 여러 개의 값을 출력하려면 print의 end에 빈 문자열을 지정해주면 됨

```
print(값, end='문자 또는 문자열')
print(변수, end='문자 또는 문자열')
```
"""


"""* end는 현재 print가 끝난 뒤 그 다음에 오는 print 함수에 영향을 줌"""


"""## 숫자를 콤마로 구분해서 표현하기"""