a = 1
b = 2

temp = a
b = temp

def run():
    assert a == 2
    assert b == 1
