#Pavel Ahamed 
#ID: 221074002
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    digits = '0123456789'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'

    res = []
    for i in range(a):
        res.append(digits[i % 10])
    for i in range(b):
        res.append(upper[i % 26])
    for i in range(c):
        res.append(lower[i % 26])

    password = []
    for i in range(len(res)):
        if i == 0 or res[i] != password[-1]:
            password.append(res[i])
        else:
            # swap with the next one if repeated
            res[i], res[i-1] = res[i-1], res[i]
            password.append(res[i])
    print(''.join(password))