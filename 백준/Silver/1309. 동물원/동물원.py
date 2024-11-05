import sys
input = sys.stdin.readline
n = int(input())

# 초기 상태 설정
prev_left, prev_right, prev_none = 1, 1, 1

for i in range(2, n + 1):
    # 현재 상태 계산
    curr_left = (prev_right + prev_none) % 9901 
    curr_right = (prev_left + prev_none) % 9901
    curr_none = (prev_left + prev_right + prev_none) % 9901
    
    # 이전 상태 갱신
    prev_left, prev_right, prev_none = curr_left, curr_right, curr_none

# 최종 결과 출력
print((prev_left + prev_right + prev_none) % 9901)
