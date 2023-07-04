# 리스트 응용
a = 0
## 리스트 조작하기

### 리스트에 요소 추가하기

'''
* append : 요소 하나를 맨뒤에 추가
* extend : 리스트를 연결하여 확장
* insert : 특정한 인덱승에 요소를 추가
'''

### 기존 리스트에 요소 하나 추가하기

a = [10,20,30]
print("원본 a 리스트 :",a)

# a = [10,20,30,500] 이렇게 다시 a 값을 재할당
a.append(500) # append -> 리스트 맨 뒤 인덱스에 새로운 원소(요소)를 추가
# ? : 없던 인덱스에 값을 할당할 수 없었으나 -> append를 통해 신규 인덱스 생성 및 값 할당이 가능하다.
# '리스트'라는 자료형, 타입, 클래스에 딸린 내장 기능 = 메서드.
print("추가된, 수정된 a 리스트 :",a)

b=list()    # == b=[]
print("원본 b 리스트 :",b)
b.append(10)
print("추가된 b 리스트 :",b)

b=[]
for i in range(10):
    b.append(i)
    print("반복문을 통해 추가된 b 리스트 :",b)



### 리스트 안에 리스트 추가하기
l = [[0]*5]*5   # 행 -> 열
print(l)
l.append([1])
print(l,"b 리스트 길이 :",len(l))    # append 시에 길이는 무조건 1씩 증가
print()



### 리스트 확장하기
a = ['사과'] * 3
b = ['배']
print(a+b)
print(a+b)
print(a+b)
print(a)    # a는 변하지 않는다.
print(b)
# inplace -> 대체 -> 메서드를 실행하는 순간 굳이 재대입/재할당 X -> 원래 변수에 영향을 미친다. 원본에 영향 O
a.extend(b) # append, extend -> 다시 할당/대입 과정 X
# append, extend => 원본 영향을 미친다.
# extend -> + 가 아닌 += 역할을 한다.
# extend는 전달받은 리스트의 원소를 하나씩 반복하면서 append라고 보시면 됨.
print("a.extend(b)한 순간 a 리스트 :",a)


####### 예시
l = [1, 2 ,3]
l2 = [4, 5, 6]

#1.
l3 = l + l2
print("#1 :", l3)

#2.
l3 = []
l3.extend(l)
l3.extend(l2)
print("#2 :", l3)

#3.
l3 = []
for v1 in l:
    l3.append(v1)
for v2 in l2:
    l3.append(v2)
print("#3 :", l3)

#3-1.
l3 = []
for v1 in l:
    l3.append(v1*2)
for v2 in l2:
    l3.append(v2*2)
print("#3-1 :", l3)


### 리스트의 특정 인덱스에 요소 추가하기
# 리스트객체.insert(인덱스, 요소)는 리스트의 특정 인덱스에 요소 하나를 추가합니다.
a = list(range(10,40,10))
print(a)
a.insert(3,40) # 기존에 없던 자리인 인덱스 3에 40이 추가될 수 있다.
a.insert(2,15) # 인덱스 2 자리에 15를 넣는다. 기존의 인덱스 2자리에 있던 요소의 인덱스는 +1 되어 뒤로간다.
a.insert(10000000,100) # 인덱스의 값이 기존 리스트의 길이보다 커지면 설정한 인덱스에 추가되는 것이 아닌, 라스트 끝에 추가된다.
print(a)
'''
* insert(0,요소) : 리스트의 맨 처음에 요소를 추가
* insert(len(리스트), 요소) : 리스트의 맨 끝에 요소 추가
'''
a.insert(0,5) # insert는 파이썬 상 속도를 많이 잡아먹는다. -> stack, queue, deque 같은 자료구조를 써서 insert를 진행
# insert는 index 바탕으로 어느 지점에 값을 넣어야 하는지 '검색 로직'도 포함하기 때문에 -> 느린 메서드!
# a.insert(len(a),101) # 굳이 할 필요는 없다. append가 있다
print(a)



### 리스트 요소 삭제
print("삭제 전 :",a)
del a[0]
print("삭제 후 :",a)

store = [10000, 2000, 5162]
# 가장 마지막 결제한 금액을 확인해서 print하고, 해당 값을 (리스트에서) 삭제
print(store)
print(store[-1])
del store[-1]
print(store)


###
store = [10000, 2000, 5162]
# 가장 마지막 결제한 금액을 확인해서 print하고, 해당 값을 (리스트에서) 삭제
print(store)
# print(store[-1])
# del store[-1]
# pop()은 리스트의 마지막 요소를 삭제한 뒤 삭제한 요소를 반환
p = store.pop() # == pop(-1) or pop(len(store)-1)
print(p)
print(store)
print(store.pop(0)) # 인덱스 -> 인덱스 번째의 값을 반환하고, 해당 값을 리스트에서 삭제
# 리스트객체.pop(Index) : 해당 인덱스의 값을 꺼내옴. (인덱스가 없으면 -1로 default 값)

# pop : 마지막 요소 또는 특정 인덱스 요소를 삭제


### 리스트에서 특정 값을 찾아서 삭제
cookies = ["마카다미아 쿠키", "치즈 쿠키", "오레오 쿠키", "레드벨벳 쿠키"]
print("삭제 전 :",cookies)
cookies.remove("치즈 쿠키") # pop 처럼 삭제된 결과값이 반환 X / pop은 반환!
# 특정한 값을 찾는 기능
print("삭제 후 :",cookies)
## 리스트.remove(값) -> 해당 값의 요소를 삭제

print(cookies.index("오레오 쿠키"))
print(cookies)
## 리스트.index(값) -> 해당 값의 요소의 인덱스를 반환
# idx = cookies.index("오레오 쿠키")
# del cookies[idx]
cookies.remove("오레오 쿠키")
print(cookies)


## index or remove 사용했을 때, 무엇을 검색 or 삭제할까요?
cookies = ["치즈 쿠키","치즈 쿠키","마카다미아 쿠키", "치즈 쿠키", "오레오 쿠키", "마카다미아 쿠키", "레드벨벳 쿠키", "마카다미아 쿠키", "마카다미아 쿠키"]
print("원본 cookies :",cookies)
print("cookies.index(\"마카다미아 쿠키\") :",cookies.index("마카다미아 쿠키"))    # 1개만 나옴.
# index 0부터 시작해서 가장 먼저 발견되는 1개.

## 위와 같은 내용
idx = 0
value = "마카다미아 쿠키"
for i in cookies:
    if i == value:
        break
    idx +=1
print(idx)

print()
print(cookies)
# print(cookies.index("초코 쿠키"))   # ValueError: '초코 쿠키' is not in list
print("초코 쿠키" in cookies)
# cookies.remove("초코 쿠키") # ValueError: list.remove(x): x not in list

# store = ["마제소바", "토리동", "부타동"]
# # while store : 리스트 -> False ? : 리스트 안에 요소가 없을 때 False 반환.
# while store:
#     print(store)
#     order = input("무엇을 주문하시겠습니까? : ")
#     if order in store:
#         store.remove(order)
#         print(order + "을(를) 드리겠습니다")
#     else:
#         print(order + "은(는) 현재 없는 메뉴입니다")
# print("장사 끝났습니다")
#
#
# ### while 조건문에 True, 무한 루프값을 넣은 경우, break 문을 통해 무한 루프를 탈출하게한 경우
# store = ["마제소바", "토리동", "부타동"]
# # while store:  # 리스트 -> False? -> 그 안에 요소가 없을 때...
# while True:
#     print(store)
#     order = input("무엇을 주문하시겠습니까? : ")
#     if order in store:
#         store.remove(order)  # 요소를 계속 제거...
#         print(order + "을(를) 드리겠습니다")
#     else:
#         print(order + "은(는) 현재 없는 메뉴입니다")
#     if len(store) == 0: # if not store:
#         break
# print("장사 끝났습니다")
print()

### 특정 값의 개수 구하기, count method
cookies = ["치즈 쿠키","치즈 쿠키","마카다미아 쿠키", "치즈 쿠키", "오레오 쿠키", "마카다미아 쿠키", "레드벨벳 쿠키", "마카다미아 쿠키", "마카다미아 쿠키"]
# 쿠키 개수
print("'cookies.count(\"치즈 쿠키\")' :",cookies.count("치즈 쿠키"))  # 정확하게 일치하는지
song = "'마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '치즈 쿠키', '레드벨벳 쿠키', '치즈 쿠키'"
print(song.count("쿠키"))  # 문자열(string) -> 특정한 단어가 몇 개 존재하는지?



### 리스트의 뒤집기
print(cookies)
print(cookies[::-1])    # 슬라이스 음수 증가폭
print(list(reversed(cookies)))  # reversed 활용
print("원본 쿠키 리스트 :",cookies) # 원본에 반영이 안됨!!

cookies.reverse()   # 원본에 영향 O
print("cookies.reverse(), 뒤집힌 쿠키 리스트 :",cookies)
print()


### 리스트의 요소 정렬
'''
sort()는 리스트의 요소을 작은 순서대로 정렬합니다(오름차순).

sort() 또는 sort(reverse=False): 리스트의 값을 작은 순서대로 정렬(오름차순)
sort(reverse=True): 리스트의 값을 큰 순서대로 정렬(내림차순)
'''
import random
r_number = random.choices(range(1000),k=10)
print(r_number)

print("<오름차순>")
for i in sorted(r_number):
    print(i)
# 무작위 리스트의 정렬
print("sorted(리스트) :", sorted(r_number))
# 오름차순(ascending) - ASC 정렬, 작은 것부터 큰 순서대로
# <-> 내림차순(descending) - DESC 정렬, 큰 거부터 작은 순서대로
print(sorted(r_number)[::-1])   # 뒤집기를 통해 오름차순을 내림차순으로 바꿈
print(sorted(r_number,reverse=True))    # sorted 정렬 : 오름차순 -> reverse=True -> 내림차순
print(list(reversed(sorted(r_number))))
print()

# reversed(함수) & 리스트.reverse()
# sorted(함수) & 리스트.sort()
r_number = random.choices(range(1000),k=10)

print("정렬 전 :",r_number)
r_number.sort()
print("(오름차순)정렬 후 :",r_number)  # sort() default : 오름차순 정렬
r_number.sort(reverse = True)       # sort(reverse = True) : 내림차순 정렬
print("(내림차순)정렬 후 :",r_number)



### 리스트의 모든 요소 삭제
print("cookies :",cookies)
cookies.clear()
print("cookies :",cookies)



### 리스트의 할당과 복사
'''
어떠한 값을 새로운 곳에 복사하는 방법
1. 할당 (assignment)
2. 얕은 복사 (shallow copy)
3. 깊은 복사 (deep copy)
'''
a = [0] * 5
print("a :",a)
b = a   # b에 a를 할당하다.
print("b :",b)
a[0] = 100
a[1] = 150
print("a :",a)
print("b :",b)
print("a is b :", a is b)    # 2개가 같습니까?
c = a[:]  # 슬라이스로 복사한 경우에는 할당이 아니라 '얕은 복사'이므로 서로 영향을 미치지 X
print("a is c :",a is c)  # 2개의 주소가 같습니까?
a[0] = 1200
a[1] = 100
a[2] = 50
print("c :",c)
d = a.copy() # 얕은 복사.
print("c is d :",c is d)

e = [a, b, c] # 리스트를 담은 리스트.
f = e.copy() # e[:] -> 얕은 복사
print("e is f :", e is f)
print("f :",f)
a[0] = 1338
print("f :",f)

import copy  # copy
g = copy.deepcopy(e)
print("g :", g)
a[0] = 21381238
print("g :", g)

'''
# 1. 할당 - 얕은 복사의 차이 : 할당 -> 특정한 데이터를 저장한 주소를 넘기는 것.
                            얕은 복사 -> 같은 데이터지만, 다른 주소를 가지도록 사본을 만드는 것
                                        (그러나 리스트 안의 리스트, 내부에 들어있는 주소의 연결을 끊지 못한다.)
# 깊은 복사 (import copy.deepcopy()) : 모든 주소들의 연결을 끊어버려서 사본을 만드는 것. 내부의 주소까지도 연결 끊는다.
'''



# 리스트(튜플) 가장 작은 수, 가장 큰 수, 합계
# 가장 작은 수, 가장 큰 수
a = random.choices(range(1, 1000), k=4)
print("a", a)
a.sort()
print("a", a)
print("최소값", a[0])
print("최대값", a[-1])

b = random.choices(range(1, 1000), k=10)  # 이중에 가장 큰 값을 구하세요 (sort 쓰지 않고)
n = 0  # 외부에 저장된 값
for v in b:
    print("n:", n, "v:", v)
    # 최대값을 구하는 방법
    # if n < v:
    #     n = v  # 더 큰 값을 n에 대입해서...
    # 최소값...
    if n == 0 or n > v:
        n = v
# 전체 반복을 끝내고 나면...
print(b, n)

# 최대값 : maximum -> max
# 최소값 : minimum -> min
print(max(b))
print(min(b))

# 합계
s = 0
for i in range(1,10): # 1~9
    s += i
print(s)
# summarization -> sum
print(sum(range(1,10)))
print(sum([5468464,84646,785454541]))

s = ["원숭이","엉덩이","빨강","현아"]
# sum(s)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 문자열들은 sum이 불가능하다.
c =""
for i in s:
    c +=i
print(c)



# 리스트 표현식 (리스트 컴프리헨션 - List comprehension)
## -> 리스트 안에 for 반복문과 if 조건문으로 -> 값들의 묶음을 표현
## -> 리스트 안에 식, for 반복문, if 조건문 등을 지정하여 리스트를 생성 == 리스트 컴프리헨션
## [식 for 변수 in 시퀀스]

a = []
for i in range(10):
    a.append(i**2)  # **은 제곱
print(a)
a = [i ** 0.5 for i in range(5, 10, 2)]
print(a)
a = [k ** 3.5 for k in range(3, 12, 3)]
print(a)


a = [i**2 for i in range(10)]   # 리스트 컴프리헨션
print(a)

b = ["아메리카노", "카푸치노","아이스티"]
# c = []  # 맨 끝 2자리 옮기기 c-> 카노 치노 스티
# for v in b:
#     c.append(v[-2:])
# print(c)
c = [ i[-2:] for i in b]    ## 위의 for문을 컴프리헨션으로 표현한 것.
print(c)
print()



# 리스트 컴프리헨션 + if 조건문
'''
[식 for i in 리스트 if 조건식] => if 조건식을 만족하는 값만 식으로 표현
'''
d = []
for i in b:
    # print(i)
    if '카' in i:
        d.append(i)
print("'카' 글자가 들어간  음료 d :",d)

e = [ i for i in b if '카' in i]
print("e :",e)


# 조건부 표현식 (삼항연산자) -> for 앞에 (식)
ee = ["나 단거 좋아해" if i =="카푸치노" else "나 단거 싫어해" for i in b if '카' in i]  # 삼항연산자
print("ee :",ee)    # 아메리카노 -> 나 단거 싫어해 / 카푸치노 -> 나 단거 좋아해
# 리스트 컴프리헨션의 if문은 -> 만족을 안 시키면 필터링. -> continue -> len이 바뀜 !!!!
# 조건부 표현식(삼항연산자)는 조건의 T/F와는 상관없이 각 행이 여전히 존재. => 값. -> len 안바뀜
# else가 있음.


# 이중 for 문
for i in range(1,10): # i <- 안 겹치게만.
    for j in range(1,10):  # 시퀀스에서 값을 빼내올 때 쓰는 변수명이 안겹치게만 조심. j
        print(i, "*", j ,"=", i*j)
        # 삼중... 사중 ...

# 이중 리스트 컴프리헨션
print([(i, j, i * j) for j in range(1,10) for i in range(1,10)])
# 리스트 컴프리헨션 -> 바깥에서 안쪽으로 우선 순위를 갖는다.
