def is_product_negative(a, b):
    a = int(input("Donnez un nombre: "))
    b = int(input("Donnez un deuxième nombre: "))
    if a or b < 0:
        print("Votre nombre est négatif !")
        True
    else: 
        print("Votre nombre est positif ! ")
        False
    return

def run():
    assert is_product_negative(6, 7) == False
    assert is_product_negative(1, 0) == False
    assert is_product_negative(-1, 5) == True
    assert is_product_negative(1, -5) == True
    assert is_product_negative(-1, -5) == False
