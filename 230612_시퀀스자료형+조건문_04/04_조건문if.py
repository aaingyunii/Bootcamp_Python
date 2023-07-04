# 조건문
## 특정 조건을 만족시켰을 때 실행시키는 문법
## -> True가 나오면 (계산, 실행 => 그 결과가 True 다. <=> 만족시켰다.)
## -> bool, 비교연산자, 논리연산자,...
a=0

'''
# if 조건문 
if 조건식 :
    조건을 만족시켰을 때 실행할 코드
'''
my_age = int(input("당신의 나이는? : "))
if my_age >= 20: # 비교연산자
    # 조건식을 만족하면 들여쓰기 된 내부의 코드 실행
    print("술 담배가 가능합니다.")

# if my_age >= 20: # 비교연산자
# # 조건식을 만족하면 들여쓰기 된 내부의 코드 실행
# print("술 담배가 가능합니다.") # IndentationError: expected an indented block after 'if' statement


# 중첩 if문
if my_age < 20:
    print("학생 입니다.")
    if my_age >= 17: # 새로운 if문을 열면 -> 새로운 들여쓰기
        print("고등학생 입니다.")
    if my_age < 17 and my_age >=14:
        print("중학생 입니다.")


# else
'''
if A: # A를 만족시킬 떄 실행 (A - 나이가 20세 이상인가?)
    ...
    print 성인입니다.
else:
    ...?(나이가 성인이 아니다.)
    print 성인이 아닙니다.
'''
'''
if <조건식>:
    코드1
else: # 단독으로 올 수 없음. if의 조건이 아닌 경우에 실행되는 것을 의미.
    코드2
'''

if my_age > 20:
    print("복권을 구입할 수 있습니다.")
else:
    print("복권을 구입할 수 없습니다.")


# 조건문에 다양한 자료형 넣어보기

# bool -> 숫자는 0이 아니면 -> True (0만 False)
# 글자는 ""가 아니면 -> True
# len(시퀀스) == 0 -> False, len(시퀀스) != 0 -> True
print("bool(1) :",bool(1))
print("bool(0) :",bool(0))
print("bool(-1) :",bool(-1))
print("bool('False') :",bool('False')) # 'False' => 문자열 / len(string) != 0 -> True
print("bool('') :",bool('')) # '' => 문자열 / len(string) == 0 -> False
print("bool([]) :", bool([]))
print("bool([100]) :", bool([100]))

if 1 : # 알아서 bool로 바꿔줌 : if bool(1) 와 같음
# if True
    print("참이다참이다.")
if 0:
    print("00000") # if 0 이 False
if '':
    print("공백 문자열") # 공백 문자열은 False len(str) == 0 -> False
if [False]:
    print("리스트 in False, 길이가 있는 문자열")


# elif
'''
if : 단순히 조건을 만족시키는 지 여부
if ... else : 만족할 때 / 만족하지 않을 때를 구분해서 배치

만약 조건이 여러 가지라면??
'''
menu = input("마시고 싶은 음료 : (아메리카노, 제로콕, 물) : ")
# if menu =="아메리카노":
#     print("아메리카노가 나왔습니다.")
# # ---------- 조건문이 각각 나뉘어서 3개가 된 것...
# if menu =="제로콕":
#     print("제로콕이 나왔습니다.")
# # ----------
# if menu =="물":
#     print("물 나왔습니다.")
# else:
#     print("주문할 수 없는 음료입니다.")
# ----------
if menu =="아메리카노":
    print("아메리카노가 나왔습니다.")
elif menu =="제로콕":
    print("제로콕이 나왔습니다.")
elif menu =="물":
    print("물 나왔습니다.")
else:
    print("주문할 수 없는 음료입니다.")
# ----------
# elif는 단독으로 사용 불가! => 맨 처음 if문이 있어야 elif가 붙을 수 있기 때문
# elif는 추가적으로 들여쓰기할 필요 없다. 기본적인 코드블록의 들여쓰기만 하면 된다.