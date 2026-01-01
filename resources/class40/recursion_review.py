# What is g(17)? Show your reasoning using a stack diagram.
def g(n):
    assert isinstance(n, int)
    if n < 5:
        return 0
    return n + g(n//2)

# What is the value of the local variable `result` below? Show your reasoning using a stack diagram.
def f(s):
    assert isinstance(s, str)
    assert len(s) >= 2
    if len(s) > 8:
        return s
    t = f(s[1:] + s[0] + 'abc')
    if t.isupper():
        return t.lower()
    return t.upper()

result = f('pqrs')
print(result)

