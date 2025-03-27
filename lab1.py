import math

def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x, y = extended_gcd(b, a % b)
        return (g, y, x - (a // b) * y)

print ('Халявка Иван Андреевич 090301ПОВа-о24')

a, b, c = map(int, input().split())

g, x0, y0 = extended_gcd(a, b)

if c % g != 0:
    print("Impossible")
else:
    x = x0 * (c // g)
    y = y0 * (c // g)
    
    k = -x * g // b
    x += k * (b // g)
    if x < 0:
        x += abs(b // g)
    y -= k * (a // g)
    
    print(x, y)
