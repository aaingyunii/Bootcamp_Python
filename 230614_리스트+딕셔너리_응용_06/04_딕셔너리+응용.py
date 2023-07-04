# 딕셔너리 응용

## 딕셔너리 조작하기

x ={
    'a' : 10,
    'b' : 20,
    'c' : 30,
    'd' : 40
}

print(x)
x['a'] = 100
print(x)
x['e'] = 70
print(x)


# 객체.메서드(...)
x.update(a=1000)    # 변수로 만들 수 있는 키 이름.
x.update(f=1000)    # 변수로 만들 수 있는 키 이름.
print("Updated x dic :",x)

# update를 통해 2개 이상의 키를 넣을 수 있다. 일괄 업데이트 가능
# x['key'] <- 한번에 하나만 가능
x.update(a=50,b=60238,c=2023)
print("Updated x dic :",x)
# 키가 변수화할 수 있는 문자열. (숫자, Boolean, 특수문자가 혼합된 문자열,...-> update 불가!)
# x.update(1=50)  #SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
x[1] = 50   # 이렇게는 가능, But update 메서드는 사용 불가
print(x)  # x[키] -> 할당 -> 키 -> 제약조건이 리스트, 딕셔너리만 아니면 됨
# x.update(...) -> 다중 업데이트가 가능, 키의 조건이 까다로움.

# 딕셔너리 키-값 쌍의 삭제
print(x)
del x['a']  # del
print(x)
# x.pop() # 딕셔너리는 순서가 없어서 pop() 기본값 처리가 안된다.
print(x.pop('b'))   # 딕셔너리의 pop은 키와 함께..
print(x)
# print(x.pop('hello'))   #KeyError: 'hello'
print(x.pop('hello',0)) # 만약 해당 삭제대상의 key가 없다면... default값이 나옴
# 딕셔너리.pop(key, default)
print()

# 전체 삭제 clear
print(x)
x.clear()
print(x)


# get을 통한 값 가져오기
x ={
    'a' : 10,
    'b' : 20,
    'c' : 30,
    'd' : 40
}
# print(x['e'])   #KeyError: 'e'
if 'e' in x:
    print(x['e'])

print(x.get('a'))
print(x.get('e'))   # 없는 키를 실행하면 None 반환. -> 오류가 발생하지 않는다.
print(x.get('e',0))   # 없는 키일 경우, 설정한 default 값으로 반환 가능.
                        # default 값을 설정하지 않았으면 None이 기본값으로 설정되어있다. null
# 딕셔너리.get('key',기본값=None)
print()


# 딕셔너리 키-값-아이템
for i in x:
    print(i)    # i로 키값들이 반환
    # 시퀀스 취급해서 반복 -> key

# for 문 반복시 요소로는 key.

print(x.keys()) # 딕셔너리의 key 리스트를 받는 메서드
print(x.values()) # 딕셔너리의 value 리스트를 받는 메서드
print(x.items()) # 딕셔너리의 (key, value) 튜플 쌍의 리스트를 받는 메서드

for i in x.items():
    print(i)

for k,v in x.items():   # (튜플) 언패킹!
    print(f"키:{k}, 값:{v}")  # f-string을 활용한 출력문



############### -> 계층형 딕셔너리, 딕셔너리 얕은 복사 / 깊은 복사
a = {}
a['b'] = {}
a['b']['c'] ={} # 딕셔너리 안에 있는 딕셔너리를 '키'를 사용해서 호출

"""
딕셔너리[키][키]
딕셔너리[키][키] = 값
"""

print(a)    # 딕셔너리는 key에 못들어가고, value에는 들어갈 수 있다.
a['b']['a'] = 100
print(a)

b=a # 할당
print(f"b is a : {b is a}")
a['b']['b'] = 100
print(b)

c=a.copy()
print(f"c is a : {c is a}")
a['b']['b'] = 1000
print(c)    # 주소값을 복사한 '얕은 복사' 발생

import copy
d = copy.deepcopy(a)
print(f"d is a : {d is a}")
a['b']['b'] = 10000
print(a)
print(d)

# 딕셔너리 컴프리헨션도 있다.