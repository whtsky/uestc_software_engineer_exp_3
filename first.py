def isTriangle(a, b, c):
    return (
        a > abs(b-c) and a < (b+c) and
        b > abs(a-c) and b < (a+c) and
        c > abs(a-b) and c < (a+b)
    )


def isIsoscelesTriangle(a, b, c):
    return a == b or b == c or a == b


def isEquilateralTriangle(a, b, c):
    return a == b == c


a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

if not isTriangle(a, b, c):
    print('不是三角形')
elif isEquilateralTriangle(a, b, c):
    print('正三角形')
elif isIsoscelesTriangle(a, b, c):
    print('等腰三角形')
else:
    print('普通三角形')