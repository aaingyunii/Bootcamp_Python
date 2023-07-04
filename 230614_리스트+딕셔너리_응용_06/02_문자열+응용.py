# 문자열

## 문자열 조작하기

### 문자열 바꾸기

'''
문자열.replace("바꿀 문자열","새 문자열") -> 기존 문자열 안의 바꿀 문자열을 새 문자열로 '교체'
-> 매번 사본이 나온다. / 원본이 바뀌지 않는다.
'''

greeting = "안녕하세요! 김파이썬씨"
print(greeting)
print("수정된 greeting :",greeting.replace("파이썬","코딩"))
print(greeting, "원본이 바뀌지 않았다.")
greeting = greeting.replace("파이썬","코딩") # 재할당하여 원본을 바꿀 수 있다.
print("재할당후 greeting :" ,greeting)


### 문자열 분리하기
### 문자열.split(구분자) -> 구분자를 기준으로 문자열을 리스트화 (구분자를 입력안하면 -> " "(공백))
a = "태조 정종 태종 세종 문종 단종 세조"
print(a.split(),a.split(" "),a.split("종"))
print(list(a))  # 문자열을 리스트화 하면 한 글자씩 쪼개져서 표현
# map(int, input().split()) # -> 요소마다 int를 적용 -> split()을 통해 공백으로 나눠줘서...

a="태조,정종,태종,세종,문종,단종,세조"
print(a.split(),a.split(","))



### 문자열 리스트 연결하기 (특정한  구분자를 입력)
b = ["태조","정종","태종","세종","문종","단종","세조"]
# b.join(...) -> 이런 메서드가 없음
print("".join(b))   # 합칠 경우, 요소들 사이에 들어갈 '구분자'에다가 join(시퀀스)
print(",".join(b))   # 합칠 경우, 요소들 사이에 들어갈 '구분자'에다가 join(시퀀스)
print(";".join(b))   # 합칠 경우, 요소들 사이에 들어갈 '구분자'에다가 join(시퀀스)
print(" ".join(b))   # 합칠 경우, 요소들 사이에 들어갈 '구분자'에다가 join(시퀀스)
print(type(" ".join(b)),type(b))


# 일괄 대문자화, 소문자화 Upper, Lower
t = "Hello PythoN!"
print(t.upper())    # 대문자화
print(t.lower())    # 소문자화
u = "HELLO PYTHON!"
print(u.isupper())  # 모든 문자가 대문자인지 확인하는지거
ll = "HellOpythoN"
print(ll.islower())  # 모든 문자가 소문자인지 확인하는지거
print(ll.isalpha())  # 전부 알파벳인가?



# 채우기 및 삭제
text = "            앞 뒤로 스페이스가 있는 경우       "
print("text :",text)
print(text.replace(" ",""))
print("text.strip() :",text.strip())
print("text.lstrip() :",text.lstrip(),"Hi")  # left
print("text.rstrip() :",text.rstrip())  # right

d= "614"    # 4자리를 맞춰야한다면 -> 맨 앞에 0을 채우자.
print("0"+d)
d2 = "64"   # 4자리를 맞춰야한다면
print("00"+d2)

# 문자열.rjust(N, S) : N은 정렬의 기준이 되는 길이. S:채우는데 쓰이는 문자.
print(d2.rjust(4, "0")) # justify -> right
print(d2.rjust(4, "I")) # justify -> right
print(d2.rjust(4, " ")) # justify -> right
# 문자열.ljust(N, S)
print(d2.ljust(4, "0")) # justify
# 문자열 왼쪽에 길이를 만족시킬 때까지 0을 넣는...
print('d2.zfill(4)', d2.zfill(4)) # rjust(N, "0") # zero - fill
print('d2.zfill(6)', d2.zfill(6)) # rjust(N, "0") # zero - fill

### 메소드 체이닝
# -> 문자열을 변형시키는 메소드 -> 결과물 문자열 -> 자기 자신에게 계속 변화를 시킬 수 있음.
# 메소드를 줄줄이 연결한다고 해서 메소드 체이닝(method chaining)
t = "      hello world         "
print(t.strip())
print(t.strip().upper())
print(t.strip().upper().replace("WORLD", "EARTH"))
print(t.strip().upper().replace("WORLD", "EARTH").split()) # split() -> 리스트니까 안됨...
print(";".join(t.strip().upper().replace("WORLD", "EARTH").split()))
print(";".join(t.strip().upper().replace("WORLD", "EARTH").split()).lower())

# 문자열 위치 찾기 & 갯수 세기
# -> 리스트.index(...) => value의 인덱스를 찾음.
# -> 문자열.find(...) -> 텍스트 in 문자열 -> 한 글자가 아니더라도 부분문자열을 찾을 수 있게
t = "아메리카노"
print(t.find("메")) # 인덱스 개념
print(list(t).index("메"))
print(t.find("리카")) # -> find를 사용해줘야 한다
# print(list(t).index("리카"))  # ValueError: '리카' is not in list
t2 = "리카리카리카"
print(t2.find("리카"))  # 맨 앞쪽.

## 문자열 개수 세기
print(t2.count("카"))
print("찐찐찐찐찐이야 완전 찐이야".count("찐"))
