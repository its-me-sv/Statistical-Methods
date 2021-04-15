def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a = [0.012128, 47.810, 46742.435]

result = a[0]
for i in a[1:]:
    result = gcd(result, i)

print(result)