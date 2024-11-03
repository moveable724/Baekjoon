from collections import Counter

MOD = 1000000007

def modular_pow(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:  # 홀수 지수일 때
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result

def modular_inverse(a, mod):
    # 모듈러 역원을 계산하기 위해 Fermat's Little Theorem 사용
    return modular_pow(a, mod - 2, mod)

n, m = map(int, input().split())
count = Counter()

# 2의 배수 처리
while n % 2 == 0:
    count[2] += 1
    n //= 2

# 3 이상의 소수 처리
d = 3
sqrt = int(n ** 0.5) + 1  
while d <= sqrt:
    while n % d == 0:
        count[d] += 1
        n //= d
    d += 2

# 마지막 남은 소수 처리
if n > 1:
    count[n] += 1

# 각 소인수의 거듭제곱의 합 구하기
r_lst = []
for x in count:
    r = (modular_pow(x, count[x] * m + 1, MOD) - 1 + MOD) % MOD
    r = (r * modular_inverse(x - 1, MOD)) % MOD
    r_lst.append(r)

# 결과 계산
result = 1
for i in r_lst:
    result = (result * i) % MOD

print(result)
