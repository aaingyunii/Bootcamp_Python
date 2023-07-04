# 불(Bool)과 비교, 논리 연산자
## 불과 비교연산자 사용하기
'''
* 프로그램 -> 참, 거짓 판단 -> 참(True): 어떠한 조건이나 수식을 만족시키는가? / 거짓(False): 만족시키지 못한다.
* Bool or Boolean : 참과 거짓 으로 구성된 자료형. <- 조건이나 수식들이 존재하게 함.
# 두 값의 관계를 판단하는 비교 / 두 값의 논리적 관계를 판단하는 논리 연산자
if, while,...구문 작성..
'''
print(True,False) # 다른 언어들은 대개 true, false
print("True의 정수형:",int(True),"/ False의 정수형:",int(False))

# 비교 연산자 - 판단-결과
## 등호(같다, 다르다)와 부등호(크다, 작다) -> 비교하는 식이 맞으면 True, 틀리면 False
print('10 > 5','10이 5보다 크다, 초과한다:',10>5)
print('10 < 5','10이 5보다 작다, 미만이다:',10<5)

## 숫자가 같은지 다른지 비교
'''
* 일반적으로 수학에서는 =를 쓰는데, 파이썬 등 프로그래밍에서는 ==으로 쓴다.
* = -> 대입연산자, 변수에 값을 할당해주는 역할
* 다를 때는, !=(not equal) 
'''
print('1 == 1:',1==1)
print('2 == 1:',2==1)
print('1 != 1:',1!=1)

## 문자열 동등 여부 비교 (only)
print("'python' == 'python':","python" == "python") # java에서는 X equals -> 주소값을 비교하기때문
print("'Python' == 'python':","Python" == "python") # 대소문자가 다르면 다른문자!
print("'Python' != 'python':","Python" != "python") # 대소문자가 다르면 다른문자!

# 숫자 비교 : 부등호
print("10 > 20:",10>20) # 초과    왼쪽 값을 기준으로 생각
print("10 < 20:",10<20) # 미만
print("10 >= 20:",10>=20) # 이상
print("10 <= 20:",10<=20) # 이하

# 객체가 같은 지, 다른 지 비교
'''
* is, is not -> 연산자
* ==, != : 값 자체를 비교
* is, is not : 객체를 비교한다. 객체 주소를 비교한다(타입).
'''
# 정수 1과 실수 1.0은 까다롭게 생각하면 다르다.
print("1 == 1.0 :", 1 == 1.0) # 1 이라는 값은 같다. 상호 변환이 가능 - 같은 숫자형일 경우에 같다고 한다.
print("'1' == 1.0 :", '1' == 1.0) # 문자열과 숫자의 비교이므로 성립 X

a = (1 is 1.0)
print("1 is 1.0 :",a)
b = (1 is not 1.0)
print("1 is not 1.0 :",b)

# 논리 연산자
## 논리 연산자 -> and, or, not
'''
* java -> &,&& / |,|| / !
'''
# and 연산자
have_car = True
have_money = True
can_drive = have_car and have_money # and : 하나라도 틀리면 다 False.
print("I have car : ",have_car)
print("I have money : ",have_money)
print("I can drive : ",can_drive)

print("have_car & have_money :",have_car & have_money) # &는 사용 가능하나 / && -> 문법 오류

# or 연산자 : 하나라도 True -> True 반환
hungry = True
study = True
eat_lunch = hungry or study # True / 둘다 False -> False 반환
print("hungry or study :",hungry or study)
print("hungry | study :",hungry | study) # &와 마찬가지로, | 사용 가능 / || 문법 오류, 사용 불가!

# not 연산자 : 논리값을 뒤집는다. / True -> False , False -> True
sleepy= True
print("Are you sleepy? :",sleepy)
print("Not sleepy :", not sleepy) # 졸리지 않다.
boring = False
print("Are you boring :",boring)
print("Not boring :",not boring) # ! 연산자 역할 X

# not and or -> 1,2,3 연산 순위 그대로 not and or

print("not True and False or not False :",not True and False or not False)
print("(not True) and (False) or (not False) ->","False and False or True :",False and False or True)
print("((not True) and (False)) or (not False) ->","False or True :",False or True)
# 위에서 처럼 not and or 의 순서가 헷갈리면 ()를 사용하면서 하나씩 처리를 하면서 연산한다.
# not 부분부터 () 묶어 연산,...
# 1. 괄호 사용하기 2. 변수로 끊어서 연산하기
# 논리 연산도 ()를 통해 강제로 우선순위를 정해줄 수 있다.

# 논리 연산자 + 비교 연산자 (무조건 비교 연산자가 먼저다!!!!!)
# 비교 연산자를 통해서 값을 비교하고 이것을 통해 True or False 결과값(Bool값)이 도출된다.
# 이후 논리 연산자가 이를 받아서 처리함.
# 산술(1) -> 비교(2) -> 논리(3) 연산자 순서 BUT, 괄호와 변수로 표현된 것이 먼저 처리한 상황임.
print("10 == 10 and 10 != 5 :",True and True) # True
print("10 > 5 or 10 < 3 :",True or False) # True
print("5+5 > 8 and 3-2 < 6 ->","10 > 8 and 1 < 6 :",True and True) # True 산술 연산부터 하고, 그 다음 비교, 논리 연산자 순으로 처리.
print("not 10 > 5 :",not 10 > 5)
print("not 7+3 > 5 :",not 7+3 > 5)

# 정수, 실수, 문자열을 Bool값으로 만들기 / 판별하기
'''
정수, 실수, 문자열 -> Bool => bool(1)
'''
# 정수, 실수 (숫자)
print("bool(1) :",bool(1))
print("bool(0) :",bool(0))
print("bool(-1) :",bool(-1)) # 정수, 실수 등 => 숫자에서 True/False의 기준은 0이면 False, 0이 아니면 True
print("bool(0.1) :",bool(0.1))
print("bool(23150) :",bool(23150))
# number -> bool ??? >> number !=0
# 0만 아니면 True / 0이면 False

#문자열
print("bool('아무말이나') :",bool('아무말이나')) # True
print("bool(' ') :",bool(' ')) # True, 비어있어보이나 스페이스(띄어쓰기) 값이 있기때문에 True
print("bool('') :",bool('')) # False =>"", '' 와같이 감싸진 것만 있을 때, 이때만 문자열의 bool값이 False를 반환한다.
# 문자열의 길이가 0보다 큰지를 통해 bool 판단, 0일 경우에만 False, 그 외 True
# string -> bool ???? len(string) > 0 # length(길이)

