# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중
# 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(num_list):
    # answer = [0,0]
    even = 0 # 짝수
    odd = 0 # 홀수
    for i in num_list:
        if i % 2 ==0:
            even +=1
        else:
            odd +=1
    # answer[0] = even
    # answer[1] = odd
    # return answer
    return [even, odd]

def solution(num_list):
    # num_list -> 정수가 담긴 리스트
    # 짝수와 홀수의 개수를 담은 -> return
    answer = [0, 0]
    # even = 0 # 짝수의 개수
    # odd = 0 # 홀수의 개수
    for n in num_list: # 처음부터 끝까지 for를 통해서 순회.
        # 짝수라면 even += 1
        print(n)
        if n % 2 == 0:
            print(str(n) + "는 짝수입니다")
            # even += 1
            answer[0] += 1
        else:
            print(str(n) + "는 홀수입니다")
            # odd += 1
            answer[1] += 1
    # print(even, odd)
    # answer = [even, odd]
    return answer





