def factorial(number):
    n = int(input("Donner un nombre entier: "))
    print(n)
    a = 1
    for i = 2, i < n
        a = a*i
        i
    print("La factorielle est de", a)
    return

def run():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(8) == 40320
    assert factorial(-8) == -40320