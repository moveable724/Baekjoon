a, b = map(int, input().split())

if b == 1:
    print(-1)
else:
    result = (a * b + (b - 2)) // (b - 1)  # Adding (b-2) ensures ceiling behavior
    print(result)
