# in Terminal
# pip install streamlit -> streamlit hello : streamlit 패키지 / ctrl + c : 종료
# streamlit run app.py

import streamlit as st  # streamlit -> import (가져오기) -> as (st 이름)
# st라는 변수명으로 streamlit의 기능들을 사용하겠다

# st. -> ctrl + space -> 다양한 기능(함수, 메소드)을 가지고 있다

st.title("강아지-고양이 사진-영상방")
st.header("구경 중")
st.subheader("Don't touch!")
st.write("streamlit을 활용해서 만들 수 있었다")

# 기능이 실행되는 순서대로 화면에서 표현
# 여러 가지 옵션을 넣어서 세부 기능들을 차이
st.image("img/dog_soldier.jpg",use_column_width=True, width=1000)   # 파일 경로 (app.py)
st.image(image="img/dog_soldier.jpg")  # 키워드를 사용해서...
st.video("img/dog_friendship.mp4")
st.video("https://i.imgur.com/UV51E6q_lq.mp4")
st.image("https://i.imgur.com/Ngnup8d_d.webp?maxwidth=520&shape=thumb&fidelity=high",width=1000)  # 인터넷 링크

st.write("""
░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░█▀▀░█▀█░█▀▀░█░█░░░░░░
░░░░░█▀▀░█▀█░▀▀█░▀█▀░░░░░░
░░░░░▀▀▀░▀░▀░▀▀▀░░▀░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░


⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞
""")
# https://imgur.com/        # 저작권 신경 안써도 되는 이미지 동영상 사이트
