def add(a, b):
    """두 수를 더한다"""
    return a + b


def subtract(a, b):
    """두 수를 뺀다"""
    print("DEBUG:", a, b)
    return a - b


def multiply(c, d):
    """두 수를 곱한다"""
    return a * b


def divide(a, b):
    """a를 b로 나눈다. b가 0이면 ValueError."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b
