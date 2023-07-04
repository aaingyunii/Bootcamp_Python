# 콘솔로부터 입력 받아서 입력값을 변수에 저장
# input 함수 사용
# input()
a=input() # input -> 실행창을 통해 입력 받으면 -> a 변수에 저장
print(a) # a를 출력

# input의 결과를 변수에 할당
# 가이드 메시지를 입력
x = input("오늘은 무엇을 드셨습니까?: ")
print(x)

# 입력은 input, 출력은 print. (표준입출력)
# input("...문자열...") <- 프롬프트(prompt)
# -> 사용자에게 입력받는 값의 용도를 알려줄 때 사용

# 두 숫자의 합 구하기 with input
a = input("첫 번째 숫자 입력: ")
b = input("두 번째 숫자 입력: ")
print(a+b) # a=17, b=39 a+b=1739 <- input으로 받은 값들은 문자열로 인식하기 때문이다.
print(type(a),type(b))
###
a = int(input("첫 번째 숫자 입력: "))
b = int(input("두 번째 숫자 입력: "))
print(a+b) # a=55, b=553 a+b=608 <- input으로 받은 값을 int로 캐스팅!하여 +연산이 가능해졌다.
print(type(a),type(b))

# 입력값을 변수 두 개에 저장.
'''
* input 한번에 값을 여러 개 입력 받으려면,
input에 split을 사용하여 변수 여러 개에 저장 가능.
(각 변수는 콤마로 구분)
* 변수1, 변수2 = input().split()
* 변수1, 변수2 = input().split('기준문자열')
* 변수1, 변수2 = input('문자열').split()
* 변수1, 변수2 = input('문자열').split('기준문자열')
'''

a,b=input('문자열 두개를 입력하세요: ').split()
# split() -> 입력받은 값을 공백(스페이스) 기준으로 구분
print("a값은",a," b값은",b)

a,b=input('문자열 두개를 입력하세요: ').split(',')
# split(',') -> 입력받은 값을 ,(콤마) 기준으로 구분
print("a값은",a," b값은",b)

#두 숫자를 한번에 입력 받아서 합 구하기
a,b=input("숫자 두 개를 입력하세요(스페이스로 구분): ").split()
print("정수형 캐스팅X: ",a+b)
print("정수형 캐스팅O: ",int(a)+int(b))

# map을 사용하여 정수로 변환
# map -> 지도. / 사상. -> 2개 이상의 쌍을 짝짓는다.
'''
map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환(실수로 변환할 때는 int 대신 float를 넣음)
* 변수1, 변수2 = map(int, input().split()) # 스페이스로 구분되오 있다면 각각 쪼개준다.
* 변수1, 변수2 = map(int, input().split('기준문자열'))
* 변수1, 변수2 = map(int, input('문자열').split())
* 변수1, 변수2 = map(int, input('문자열').split('기준문자열'))
'''
a,b=map(int,input("숫자 두 개를 입력하세요(스페이스로 구분): ").split())
print("a+b =",a+b)
a, b = map(int, input("숫자 두 개를 입력하세요 (콤마(,) 구분): ").split(','))
print("a+b =",a+b)