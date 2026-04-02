def is_armstrong(n):
    num = n
    result = 0
    while num > 0:
        ld = num % 10
        result = result + (ld**3)
        num = num // 10
    return result == n


n = 153
print(is_armstrong(n))