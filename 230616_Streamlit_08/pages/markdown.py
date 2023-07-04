import streamlit as st  # streamlit -> import (가져오기) -> as (st 이름)

st.title("MarkDown_mark_down")
st.divider()
# st.write / st.markdown
# st.write -> 입력하는 것에 맞춰서 알아서 결정
# st.markdown -> 명백하게 마크다운을 사용하겠다.

# 제목 마크다운
st.write("""
# 가장 큰 제목 텍스트 (h1 = headline1 = st.title)
## 두번째 제목 텍스트 (h2 = headline2 = st.header)
### 세번째 (h3 = headline3 = st.subheader)
#### 네번째 (h4)   
##### 다섯번째 (h5)
###### 마지막 (h6)
""")
# 문자열 삽입 가능
# 서식
text = """
기울임 : *별표* or _언더바_  하나씩 써주면

진하게(bold) : **별표**  or  __언더바__  두개씩 써주면

기울임 + 진하게(bold) : ***별표***  or  ___언더바___    세개씩 써주면

취소선 : ~물결표~

밑줄 : <u>밑줄</u>

형광펜 : <mark>형광펜</mark>
"""
# st.write(text)
# 태그를 허용하는 옵션 : unsafe_allow_html=True
st.markdown(text, unsafe_allow_html=True)

# 레이아웃
st.divider()
st.subheader("레이아웃")
st.write("""
    #### 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서 없는 리스트
        * 들여쓰기 1
            * 들여쓰기 2
                * 들여쓰기 3

    - (-)대시를 여백 1칸 이상과 사용하면 순서 없는 리스트
    - (-)대시를 여백 1칸 이상과 사용하면 순서 없는 리스트
    - (-)대시를 여백 1칸 이상과 사용하면 순서 없는 리스트
        - 들여쓰기 1
            - 들여쓰기 2
                - 들여쓰기 3

    #### 순서가 있는 리스트
    1. 순서가
    2. 있는
    3. 리스트
    5. 숫자를 건너 뛰어도 무시하고 순서를 따른다.
        1. 들여쓰기 1
            1. 들여쓰기는 1로 시작해야 먹힌다.
    1. 순서가
    1. 1로 계속 넣어도
    1. 증가됨.

    #### 가로줄(- or _ 3개씩)
    ---
    ___

    #### 테이블(표)
    |이름|직업|
    |-|-|
    |파이썬|백수|
    |자바|일잘러|
""")

# 링크
st.divider()
st.subheader("링크")
l1 = "https://naver.com"
l2 = "https://i.imgur.com/qBpMFOsb.jpg"
st.write(f"""
    * [네이버](https://naver.com)  
    * ![이미지이미지]({l2})
    * [![이미지이미지]({l2})]({l1}) 이미지에 링크 삽입 
""")

# 인용
st.divider()
st.subheader("인용")
st.write(f"""
    > 명언 - 유명한 사람


    > 코드코드 - 어느 사람

    책이나, 사람 말을 인용할 때...
    > 인용 첫줄
    >> 인용문 안에 인용임

    #### 코드
    `코드를 나타낼 때 주로 쓰이는 묶음 표시 (한줄)`
    ```
    여러 줄로 코드를 나타내고
    줄바꿈도 반영하고 싶으면...
    print("파이썬!")
    ```
    ```python
    print("파이썬!")
    ```
""")


