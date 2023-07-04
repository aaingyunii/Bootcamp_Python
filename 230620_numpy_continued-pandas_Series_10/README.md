# 230620_numpy_continued & pandas_Series🐍💪
### 수업 내용 : 

#### ✔ 이전 수업 내용 복습

#### ✔ Streamlit을 이용해 Numpy 패키지 활용 관련 사이트 개발 안내
#### ✔ Numpy - 배열의 연산, 기술통계, 난수 발생, 카운팅 관련 예제를 작성하고 개념을 학습
#### ✔ random 모듈의 내장 메서드를 다양하게 활용하여 예시 코드 작성 및 실행
***
#### ✔ pandas 라는 새로운 모듈을 배웠고, 이 중 Series 클래스에 대한 기초를 학습하였습니다.
```python
# $pip install pandas
import pandas as pd

data = [9904312, 3448737, 2890451, 2466052]
index = ["서울", "부산", "인천", "대구"]
s = pd.Series(data, index = index)
s
# s의 결과값
# 서울    9904312
# 부산    3448737
# 인천    2890451
# 대구    2466052
# dtype: int64

pd.Series(range(10,14))

# 0    10
# 1    11
# 2    12
# 3    13
# dtype: int64
```

### 🔗[TIL](https://github.com/aaingyunii/Bootcamp_TIL/issues/10)

