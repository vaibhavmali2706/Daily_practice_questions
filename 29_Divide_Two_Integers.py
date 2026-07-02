dividend = 10
divisor = 3

sign = -1 if (dividend < 0) or (divisor < 0) else 1

dividend = abs(dividend)
divisor = abs(divisor)

ans = 0

while dividend >= divisor:

    temp = divisor
    multiple = 1

    while dividend >= (temp << 1):
        temp <<= 1
        multiple <<= 1

    dividend -= temp
    ans += multiple

print(sign * ans)