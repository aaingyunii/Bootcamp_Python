import streamlit as st

st.title("Component")
st.divider()

st.write("💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣")
cols = st.columns(2)   # 컬럼 리스트
cols[0].write("🐍")
cols[1].write("💪")

cols = st.columns(3)
cols[0].write("😆")
cols[1].write("🤣")
cols[2].write("🤪")

cols = cols[0].columns(3) # 열의 열인 거임
cols[0].write("😆")
cols[1].write("🤣")
cols[2].write("🤪")
cols[0].write("🐦")
cols[1].write("🐦")
cols[-1].write("🐦")

col1,col2 = st.columns(2) # 리스트 언패킹
col1.write("왼쪽 열")
col2.write("오른쪽 열")

with col1 : # col1을 기준으로 streamlit을 써주겠다. -> with 구문을 통해서!!
    # 블록 (:)을 열면 -> 이 안에서는 streamlit 기능 실행시 col1에 종속
    st.write("왼쪽")

with col2 : # col2을 기준으로 streamlit을 써주겠다. -> with 구문을 통해서!!
    # 블록 (:)을 열면 -> 이 안에서는 streamlit 기능 실행시 col2에 종속
    st.write("오른쪽")

# tabs=st.tabs(["김치찌개","된장찌개","순두부찌개"])
tab1,tab2,tab3 = st.tabs(["김치찌개","된장찌개","순두부찌개"])
tab1.image("https://static.wtable.co.kr/image/production/service/recipe/291/a2421dff-e56c-40bd-8b40-06a91fc000a9.jpg")
tab2.image("https://static.wtable.co.kr/image/production/service/recipe/2166/4c5781b8-6091-4303-946f-bd845b5f38ac.jpg?size=1024x1024")

with tab3:
    img3= "https://static.wtable.co.kr/image-resize/production/service/recipe/1074/4x3/d3c0b5c1-2671-483e-9bbf-76496bb443fd.jpg"
    st.image(img3)

exp = st.expander("Surprise!!!", expanded=False)
exp.image("https://i.namu.wiki/i/5lWwYGj-VC8ZqJxug7Exm5-7rHE97fdZui3DWEAjm0zdLiBCbcdw4mLyGhcbZ_KecZOQr4rtwNJSFs63Rsdd_Q.webp")
# with exp: ...

# 입력
st.title("입력")
name = st.text_input("나의 이름은")  # 변수로 받을 수 있음
name2 = st.text_input("너의 이름은")  # 변수로 받을 수 있음
# st.text_input("")
# st.write(name)
# st.write(name2)
st.write(f"신랑 {name}과 신부 {name2}는...")
# number = st.number_input("당신의 나이는?")
age = st.number_input("당신의 나이는?", step=1)
st.write(f"나의 나이는 {age}세")
height = st.number_input("당신의 키는?", step=0.1)
st.write(f"나의 키는 {height}cm")

# https://docs.streamlit.io/library/api-reference/widgets

st.divider()
mode = st.checkbox("강사님 잔소리모드")  # bool (T/F)
col1, col2, col3 = st.columns(3)
r = col1.radio("잔소리 내용 선택", ["취업", "코딩", "지각"])
s = col2.slider("잔소리 강도 선택", min_value=1, max_value=10)
b = col3.selectbox("잔소리 말투 선택", ["친절하게", "반말", "모욕적"])
if mode:
    # r -> 취업, 코딩, 지각
    format = None
    if b == "친절하게":
        format = lambda x: f"여러분~ {x}"
    elif b == "반말":
        format = lambda x: f"야! {x}"
    elif b == "모욕적":
        format = lambda x: f"XXXXXX! {x}"
    if r == "취업":
        for i in range(s):
            st.write(format("8월에는 자소서 넣어야겠죠?"))
    elif r == "코딩":
        st.write(format("저보다 파이썬 잘해요?"))
    elif r == "지각":
        st.write(format("9시랑 9시 1분은 다른 거에요."))