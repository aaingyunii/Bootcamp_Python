# while (동안에~~~)
# 조건문 + 반복문
# -> 조건식을 만족시키는 (True) 동안에 계속 반복하는 코드
'''
while 조건식(True or False) : # 조건식이 불변이면? -> 무한 반복
    실행할 코드 *
    반화식 *
'''
money = 1000
while money > 0:
    print(money)
    money -=100 # 100씩 차감되고 그 값을 대입 (변화식*)
print("돈 다씀. 잔고 :",money)

'''
while 반복문의 실행 과정입니다. 먼저 초기식부터 시작하여 조건식을 판별합니다.
이때 조건식이 참(True)이면 반복할 코드와 변화식을 함께 수행합니다.
그리고 다시 조건식을 판별하여 참(True)이면 코드를 계속 반복하고,
거짓(False)이면 반복문을 끝낸 뒤 다음 코드를 실행합니다.
여기서는 조건식 → 반복할 코드 및 변화식 → 조건식으로 순환하는 부분이 루프(loop)입니다.
'''

'''
초기식 (변수에 값을 저장)
while 조건식 (변수의 현재 상황을 감시):
    1. 반복할 코드 (...)
    2. 변화식 (초기식에 넣은 변수를 변화)
'''
w = 0 # 초기식
while w < 100: # while 조건식
    print("반복~ 반복~") # 반복 코드
    w += 2 # => range의 증가폭.
    print("변화가 발생... ",w)
print("while문에 포함되지 않은 코드\n")
# 이런건 for문으로 짜는게 나음

w = 10
print("While문 예시")
while w < 50:
    w+=5
    print(w)

print("For문 예시")
for i in range(10,50,5):
    print(i)

### 위의 예시들은 반복 횟수가 정해져있거나, 구조가 명확한 경우.
### <- while문보단 for문이 더 쉽게 가능

#### 반복 횟수가 정해져 있지 않은 경우 -> while
import random # random 모듈

# 무작위의 수 or 조합들을 가져오는(만들어주는) 기능
print(random.random())  # 0~1 사이의 실수
# random.randint(a,b) => a와 b사이의 정수 1개를 무작위로 호출 **a,b 둘다 포함**
print(random.randint(1,6),"\n")

for i in range(10):
    w=0
    v=0
    while w != 3: # w가 3이 아니면, 즉, 3이면 while문 종료
        w = random.randint(1,10)
        print(w,"이(가) 나왔습니다.")
        v += 1
    print("위의 랜덤 while문은",v,"번 반복하였습니다.")

# 무한루트
while 1:
    print("o",end="")
    i +=1
    if i == 100:
        break     # 무한루프를 제어하기 위한 장치
print("\n")
# break, continue
'''
break는 for와 while 문법에서 제어흐름을 벗어나기 위해 사용합니다.
즉, 루프를 완전히 중단하죠. continue는 break와 비슷하지만 약간 다른 점이 있습니다.
break는 제어흐름을 중단하고 빠져 나오지만,
continue는 제어흐름(반복)을 유지한 상태에서 코드의 실행만 건너뛰는 역할을 합니다.
마치 카드 게임을 할 때 패가 안 좋으면 판을 포기하고 다음 기회를 노리는 것과 비슷합니다.

* break: 제어흐름 중단
* continue: 제어흐름 유지, 코드 실행만 건너뜀
'''

# break -> 반복문 정지
## while -> break
i = 0
while True: # 무한 루프
    print(i)
    i += 1
    if i > 10:
        break
# 반복문 안에서 break를 실행하면 반복문은 바로 끝난다

for i in range(1, 10000):
    print(i)
    if i % 5 == 0:
        break

# for -> break
for i in range(1, 10000):
    print(i)
    if i == 20:
        break
    # if i % 5 == 0:
    # if not i % 5: #  not i % 5 == True
    #     break

# continue - 코드 실행 건너뛰기

## for - continue
for i in range(1,100):
    # 2의 배수는 print 하지않고, range는 건들일 수 없다면?
    if i % 2==0: # if not i % 2:
        continue # 뒤의 코드 실행 X
    print(i)
print()

# for -> 시퀀스
actors = ["송강호","이병헌","하정우","송중기","류승범"]
for a in actors:
    # 송씨 배우만 print 하고 싶다.
    #  일반적인 방법
    if a[0] == "송":
        print(a)

    # continue 활용방법
    if a[0] != "송":
        continue
    print(a)

# while 문 - continue
w = 0
while w != 3: # 3이 아니면,
    w = random.randint(1,6)
    print(w)
    if w == 6:
        continue
    print(w,"이(가) 나왔습니다.")