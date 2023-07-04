# 리스트와 튜플
## 리스트 : 1개 이상의 연속된 값들의 묶음
'''
지금까지의 변수와 값들 -> 값을 하나씩 다뤘음.
'''
a = 10
b = 20

# 30개의 숫자를 저장한다면 (1~30)
'''
a1=1
a2=2
...
a30=30...???
'''

# list -> 목록, 값을 일렬로 (순서 있게) 늘어놓은 형태
# Make list
'''
* 변수에 값을 저장할 때 []로 묶어주면 리스트가 됨. 각 값은 ,(콤마)로 구분
* list = [값1, 값2,...]
'''
fruits = ["사과","배","포도","딸기"]
print("과일 리스트 :",fruits)
numbers =[1,2,3,4,5,6,7]
print("숫자 리스트 :",numbers)

# 리스트에 여러 가지 자료형 저장 가능 혼합해서!
teacher = ["name",170,77.8,True] # 리스트-나열 -> 대개 다른 언어에서는 다 같은 타입이 되도록 제한되어 있다.
print(teacher)
# 파이썬에서의 리스트는 여러 가지 자료형(타입)들을 편하게 넣을 수 있다.

# 빈 리스트 만들기
'''
* 빈 리스트를 만들 때는 [ ]만 사용하거나, list()를 사용하면 됨.
* 리스트 = []
* 리스트 =list()
'''
a= []
print("a :",a)
b= list()
print("b :",b)

# range를 사용하여 리스트 만들기
'''
range는 연속된 숫자를 생성하는 기능
range(10) # 시작은 0부터 9까지, 끝은 입력한 값의 직전,(9)까지의 나열
* 0~9까지의 수의 나열
'''
print("0~9 리스트 :",range(10)) # range(n) : 0부터 n 직전까지의 숫자를 생성
# range(0,10) <- 위의 출력값, 앞으로 사용될 range로 대기 상태.
print("0~9 리스트 :",list(range(10))) # list()로 캐스팅하여 range(0,10)을 풀어서 출력한 결과값
# 수를 나열한 리스트를 만들 때
# 리스트 = list(range(횟수)) : 횟수 -> 횟수-1의 값까지 숫자를 만들겠다. (0부터 시작해서)

# 시작점과 끝점이 모두 있는 range
rr = range(8,14) # 8~13 까지의 정수들의 집합.
print(rr) # 이것은 list가 아니다.
print("rr 리스트 :",list(rr))
# 시작점은 포함, 끝점은 포함X

# 시작점, 끝점, 증가폭이 모두 포함된 range
rr2 = range(100,1000,100) # list(range(시작점,끝점,증가폭)) -> 증가폭만큼, 늘어나면서 숫자 리스트 생성
print(list(rr2)) # 100 200 300 400 500 600 700 800 900
print(list(range(100,950,100))) # 끝점을 초과하면 멈추는 개념

rr3= range(1000,100,-100)
print(list(rr3)) # 증가폭은 음수도 가능하다.
print(list(range(1000,99,-100)))
print(list(range(10,0,1))) # 빈 리스트 출력, 시작점에서 검사를 해보니까 끝점을 추월했기 때문이다.
print()
#  튜플 (tuple)
'''
* 리스트처럼 요소(원소, element)들이 있다.
* 튜플은 요소를 수정할 수 없다. 읽기 전용(read only)
* 리스트가 []라면, 튜플은 () 입니다. 각 값은 ,(콤마)로 구분
* 변수 한개에 => 여러 값을 (괄호 없이) ,로 구분해서 넣으면 => 역시나 튜플
* 튜플 = (값1,값2,값3...)
* 튜플 = 값1,값2,값3,...
'''
a1=(23,25,24,11,55)
print(a1)
a2=3,2,412,121,546
print(a2)
a3 = "py","python",123,"pypy",True
print(a3) # 튜플도 리스트와 마찬가지로 여러 가지 자료형(타입)을 섞어도 문제 없다.

# range를 사용해서 튜플 만들기
# list(...) -> range -> list
# tuple(...) -> range -> tuple
print("Range to Tuple :", tuple(range(0,10)))
# tuple(range(끝점))
# tuple(range(시작점,끝점))
# tuple(range(시작점,끝점,증가폭))

# tuple을 list로 변경하고, list를 tuple로 변환한다면?
a = list(range(10)) # [0,1,...,9]
print("a 리스트 :", a)
b= tuple(a)
print("a 리스트 to 튜플 named b :",b)
# 반대도 똑같이 가능하다. 리스트 <-> 튜플 상호 변환 가능!

# 리스트와 튜플로 변수 만들기
'''
* 리스트 or 튜플을 사용하면 변수 여러 개를 한 번에 만들 수 있음.
* 이 때, 변수의 개수와 리스트(튜플)의 요소 개수는 같아야함.
'''
l = [1,2,3]
a,b,c=l
print("a :",a," b :",b," c :",c)
t = ("dog","cat","cow","bird")
d,e,f,g = t
print("d,e,f,g :",d,e,f,g)

d,e,f,g = ("dog","cat","cow","bird") # d,e,f,g = t
d,e,f,g = "dog","cat","cow","bird" # d,e,f,g = t
# 파이썬에서 변수의 수와 값의 수가 일치하면 한 번에 변수에 각 값을 대입할 수 있다. unpacking
# Unpacking -> tuple unpacking

a,b,c = [1,2,3] # 리스트를 분해해서 각각의 변수에 집어 넣음 : list unpacking.

v = 10,100,1000 # -> tuple 형태로 묶어서 넣는 것 -> packing -> tuple packing
l = [10,100,1000] # list packing


