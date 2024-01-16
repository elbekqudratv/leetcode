#birinchi korinish

def powerOf1(n):
    return n > 0 and (n & (n - 1)) == 0

#ikkinchi korinish

def powerOF2(n):
    if n <= 0:
        return False

    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2

    return True

