# Высокий уровень 30 вариант
def to_hex_classic(n):
    if n == 0: return "0"
    digits = "0123456789ABCDEF"
    result = ""
    while n > 0:
        result = digits[n % 16] + result
        n //= 16
    return result

num = int(input("Число: "))
print(to_hex_classic(num))