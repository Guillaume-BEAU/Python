def is_number_correct(number):
    number = int(input("Donnez un nombre positif ou négatif: "))
    print(number)
    while number < 10 or number > 20
    print(number)
    if number < 10:
        print("Le nombre est plus grand !")
    else:
        print("Le nombre est plus petit !")
    if number == 10 or number == 20
        print("Bravo vous avez trouvé le nombre")
        True
    else
        False
    return

def run():
    assert is_number_correct(0) == (False, 10)
    assert is_number_correct(10) == (True, 0)
    assert is_number_correct(20) == (True, 0)
    assert is_number_correct(21) == (False, -1)
    assert is_number_correct(50) == (False, -30)
    assert is_number_correct(15) == (True, 0)
