# 시퀀스 자료형

# 리스트와 튜플, 문자열, range -> 공통점 : 값이 연속적으로(sequence) 이어져 있다.
# 값이 연속적으로 이어진 자료형을 시퀀스 자료형(sequence type)이라고 한다.

print("파이썬","파","이","썬") # 단어들이 합쳐진 것 -> 문자열

# 시퀀스 자료형의 공통 기능, 특징

## 특정한 값이 (안에) 있는 지 확인
## -> 요소(element) -> 묶음 안에 존재하는지를 확인
## 값 시퀀스 객체
## 객체 : 특정한 자료형 타입에 속하는 것들

shoes = ["아디다스","나이키","컨버스"]
print("shoes :",shoes)
print("'아디다스' in shoes?? :",'아디다스' in shoes) # in도 일종의 연산자 ex) for i in ~~
print("'반스' in shoes?? :",'반스' in shoes)
print("'닥터마틴' not in shoes?? :",'닥터마틴' not in shoes, not '닥터마틴' in shoes) # in이 먼저 연산 처리됨
# 따라서 not '닥터마틴' in shoes 의 경우, '닥터마틴' in shoes의 결과값이 False가 나오고 not False가 되면서 최종적으로 True값을 반환한다.

# 시퀀스 자료형의 객체들의 공통적인 기능.
# 시퀀스 타입 <= (문자열, 리스트, 튜플, range)

tup = ("마제소바", "토리동", "부타동", "점보부타동", "반숙계란")
print("Tup :",tup) # 튜플
print("'쌀국수' in Tup?? :", '쌀국수' in tup)
r = range(500, 100, -25)
print("r :", list(r))
print("200 not in r :", 200 not in r)
# 문자열 검색
phone_number = "010-9999-9999"
print("'0' in phone_number?? :",'0' in phone_number)
print("'010' in phone_number?? :",'010' in phone_number)
print("'011' in phone_number?? :",'011' in phone_number)
### 문자열은 연속된 부분집합들의 형태로 단어들을 검색 가능
### But, 다른 시퀀스는 안된다. 문자열만 가능!
print()

## 연결(concatenate)
# 시퀀스 객체는 +연산자를 이용하여 객체를 서로 연결-새 객체 생성 가능하다.
# 시퀀스 객체 1 +시퀀스 객체 2 (웬만하면 동일 타입)

# 리스트 예시
a = [0,1,2,3]
a = list(range(4)) # 위의 a와 같은 결과값
aa = list('1234')
print(aa)
# print(a)
# b= [4,5,6,7]
b = list(range(40,98,8))
# print(b)
c = a+b
print("a + b =",c,"\n") # 리스트끼리의 +연산자를 통해 연결

# 튜플 예시
# a = ("a", "b", "c", "d")
a = tuple("abcd") # list("abcd")
# b = ("e", "f", "g", "h")
b = tuple("efgh") # list("efgh")
print("a + b :", a + b)

# 시퀀스 자료형 중에 연결 안되는 것 : range가 연결이 안됨!
# 잘 연결되는지 검사할 바에야 아예 막자
# print(range(10) + range(10, 20)) : unsupported operand type(s) for +: 'range' and 'range'
# range(7, 10) + range(100, 20, -1)
print(list(range(10)) + list(range(10, 20)))


# 문자열도 시퀀스 -> 연결(+)연산자 가능
# greeting = "Hello"
# my_name = input("Your name : ")
# print(greeting+my_name)

# 문자열과 숫자 연결
# money = input("받고 싶은 돈 : ")
# print(type(money))
# money = int(money)
# # print("당신의 계좌에 "+money+"만원이 입금되었습니다.") # TypeError: can only concatenate str (not "int") to str
# print("당신의 계좌에 "+str(money)+"만원이 입금되었습니다.")

## 반복

# * 연산자는 시퀀스 객체를 특정 횟수만큼 반복하여 시퀀스 객체를 만든다.(0 or 음수를 넣으면 빈 것이 나온다.)
'''
- 시퀀스객체 * 정수
- 정수 * 시퀀스 객체
'''
k = [0,10,20,30]
print("k 리스트를 3번 반복한다 :",k+k+k)
print("k 리스트를 3번 반복한다 :",k*3) # k+k+k == k*3
print("k 리스트를 0번 반복한다 :",k*0) # 빈 리스트
print("k 리스트를 -3번 반복한다 :",k*-3) # 빈 리스트
## 튜플도 유사...
k *=6
print(k) # 산술할당연산자도 연결 똑같이 함
# range는 안됨!
# print((range(10)*3)) #TypeError: unsupported operand type(s) for *: 'range' and 'int'
print(tuple(range(10))*10)
hi = "HI"
print(hi*10,"\n")

## 시퀀스 객체의 길이 구하기
## == 시퀀스 객체의 요소, element, 개수 구하기
## len -> length의 약자. 파이썬의 len은 함수! len(...)
## len(시퀀스 객체)

a = [1,1,2,3,5,8,13,21,34,55] # 피보나치 수열
print(len(a)) # a 리스트안에 10개의 element가 있다.
b = ['dwd',2,33213,'qwe',True]
print(len(b))


# range : range에 len 함수를 사용하면 숫자가 생성되는 개수를 구한다.
print(len(range(98561,515144684,1000)))
print(len(range(75,55,-4)))

# 문자열 : len -> 포함된 '문자' 개개의 개수
s = "오늘은 \'마제소바\'를 먹을 것입니다."
print(len(s)) # 20개, 문자와 공백, 온점(.) 과 같은 특수 기호도 개수에 포함된다.
              # \(역슬래시)는 포함되지 않는다.
print(s)
# 파이썬은 숫자, 영어, 한글의 길이 구분 X -> 똑같이 길이 1씩 센다.

# 인덱스
# 시퀀스 객체 -> 여러 개의 데이터들이 묶여있는 형태 -> 요소들간의 순서가 정해져있음
# -> 시퀀스 객체 내에 요소들의 위치 == 인덱스 (Index)
# 시퀀스_객체[인덱스번호] -> 시퀀스 객체에 []를 붙이고 []안에 각 요소의 인덱스(번호)를 지정하면 해당 요소에 접근(호출)
a = [100,200,300,400,500]
print(a[1])
# 프로그래밍에서는 모든 숫자 세기를 0부터 시작한다.
print("a 리스트의 첫번째 요소 :",a[0]) # 리스트[0] == 리스트의 첫번째 요소
                                    # 리스트[1] == 리스트의 두번째 요소 지칭!
# 인덱스를 통해서 내가 원하는 값(특정한 순서에 있는 값)을 불러오는 것 : 인덱싱(Indexing)
print("len(a) :",len(a))
# print(a[5]) # IndexError: list index out of range -> index를 생각할 때, len보다 1 작은 것까지.


# range
r = range(2,5) # 2 3 4
print("r[2] :",r[2])

# 문자열 (string)
s = "오늘의 날씨를 알려드리겠습니다."
print("s[7] :",s[7]) # 인덱스 7 -> 8번째 -> 스페이스 공백
print("s[8] :",s[8]) # 인덱스 8 -> 9번째
print(s) # 인덱스 없이 호출 -> 그 자체 (전체 값)
# 해당 객체 전체

## 음수 인덱스
a = [32,11,56,187,102]
print("a[-1] :",a[-1]) # 102 출력
print("a[-4] :",a[-4]) # 11
print("a[-5] :",a[-5]) # 32
# print("a[-6] :",a[-6]) # IndexError: list index out of range
print(a[len(a)-1]) # len보다 음수 인덱스가 커지면 에러

# 튜플, range,...
s = "마제소바"
print(s[-1])
sn = "991111-1154334"
print(sn[-7])
print()

# 인덱스를 통해 요소에 값 할당(대입) == 수정
print(a)
print(a[0],"\n") # 시퀀스객체[인덱스] <- 그 값을 불러오는 기능 / 그 값의 위치를 확인

b= [0] * 5
print("b 리스트 수정 전 :",b)
b[0] = 137
b[1] = 52
b[2] = 66
b[3] = 984
b[4] = 1021
print("b 리스트 수정 후 :",b)
# b[5] = 778 # IndexError: list assignment index out of range
print()

# 인덱스를 통해서 요소의 값을 재할당 -> 리스트!
# 튜플, range, 문자열은 재할당 X -> read-only
t = (1,2,3)
# t[0] = 4 # TypeError: 'tuple' object does not support item assignment
r = range(10)
# r[7] = 555 # TypeError: 'range' object does not support item assignment
st = "하하"
# st[0] = "호" # TypeError: 'str' object does not support item assignment


## 요소 삭제 (요소 수정과 삭제 모두 리스트 전용 기능)
aa = ["바나나", "키위", "콩"] # 0, 1, 2
print(aa)
del aa[2]
print("del aa[2] :",aa)
# 튜플, range, 문자열 > del 안먹힘!
## 요소 수정과 삭제 모두 리스트 전용 기능