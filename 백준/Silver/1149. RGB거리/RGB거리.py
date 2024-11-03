import sys
input = sys.stdin.readline

m = int(input())
lst = list(map(int, input().split()))

# dp 배열 크기를 m으로 설정
dp_r = [0] * m
dp_g = [0] * m
dp_b = [0] * m

# 첫 번째 집 초기화
dp_r[0], dp_g[0], dp_b[0] = lst[0], lst[1], lst[2]

# 두 번째 집부터 m번째 집까지 비용 계산
for i in range(1, m):
    lst = list(map(int, input().split()))
    dp_r[i] = min(dp_g[i-1], dp_b[i-1]) + lst[0]
    dp_g[i] = min(dp_r[i-1], dp_b[i-1]) + lst[1]
    dp_b[i] = min(dp_r[i-1], dp_g[i-1]) + lst[2]

# 마지막 집까지 칠했을 때의 최소 비용 출력
print(min(dp_r[m-1], dp_g[m-1], dp_b[m-1]))
