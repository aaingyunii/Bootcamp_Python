# 옹알이 (1)
# 문제 설명
# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다.
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 1 ≤ babbling의 길이 ≤ 100
# 1 ≤ babbling[i]의 길이 ≤ 15
# babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.
# 즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가 한 번씩만 등장합니다.
# 문자열은 알파벳 소문자로만 이루어져 있습니다.
#
#
# 입출력 예시
# babbling	                             result
# ["aya", "yee", "u", "maa", "wyeoo"]	        1
# ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	3

# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    # babbling -> 외부로부터 주어짐
    # babbling <= 단어들이 요소들로 묶여져 있는 형태
    # 묶여져있다 -> 발음을 할 수 있는지 '검사'해야한다

    pron = ["aya", "ye", "woo", "ma"]
    answer = 0  # 답을 주면 되겠구나 -> 발음 여부

    for b in babbling:  # 검사하고 싶은 단어들의 리스트 -> 단어(요소) b
        print(f"원래 b : {b}")
        # b -> pron을 돌아가면서 '제거'해주면... => 발음할 수 없는 것만 남는다
        # 제거를 했는데 b의 길이가 0 초과면? => 이 조합으로 발음할 수 없는...
        for p in pron:
            # b = b.replace(p, "")
            b = b.replace(p, "*")
        print(f"제거 b : {b}")  # wyeoo -> ppron의 순서에 따라서 먼저 ye가 제거가 되면, woo -> 발음?
        b = b.replace("*", "")
        if len(b) == 0:
            answer += 1
    return answer

### 다시