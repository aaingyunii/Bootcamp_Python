# 문자열 String
## '' or "" 로 묶여진 글자들의 묶음(0자 이상의 글자들의 집합)

text = "hello playdata!"
print(text,'\n')

# 한글 문자열
korean = "아무말이나 쓴거"
print(korean)

# 문자열 만들기 : ""(double quotation marks)로 묶기.
dqm = "my name is python"
print(dqm)

# ''(single quotation)로 묶기
sqm = 'your name is python'
print(sqm,'\n')

# '''...~''' or """...~""" 로 묶기
t1 ='''hello guys'''
t2 = """good lunch"""
print(t1,t2)

# 여러 줄로 된 문자열 사용
m1 ='''
green red
red green
hello bye
'''
print(m1,"=\ngreen red\nred gree\nhello bye") ## 둘이 같은 결과값
# 여러 줄로 된 문자열은 큰따옴표나 작은따옴표 3개로 시작해서 3개로 마쳐주면 된다.
'''
이를 저장하는 변수 or 실행하는 구문이 없다면 이것은 그냥
여러 줄로 된 주석처럼 쓸 수 있게 된다.
'''

# 큰따옴표로 묶었을 때, 중간에 큰 따옴표가 들어가면?
# text = "안녕"안녕"  # 따옴표는 직전 따옴표와 직후 따옴표 간의 문자열을 묶는다고 인식
text = "이름하여 '파이썬'" # 전체를 큰따옴표로 묶었기 때문에, 안에 있는 작은 따옴표는 문자열 그 자체로 인식
print(text)
text2 = '큰따옴표("")'
print(text2)

text = "\"" # \" <- 큰따옴표 자체가 가지고 있는 문자열을 감싸주는 특수 기능 제거(이스케이프)
print(text)
# 여러 줄 문자열 안에서는 작은따옴표 or 큰따옴표가 섞여도 문제 없음.
t1 = '''
작은따옴표(')
큰따옴표(")
'''
print(t1)
t2 = """
작은따옴표(')
큰따옴표(")
"""
print(t2)
