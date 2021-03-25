def get_letter_count(word):
       word = (input("Écrire un mot ou une phrase: "))
       longueur = len(word)
       print(longueur)
       return

def run():
   assert get_letter_count("Oui") == 3
   assert get_letter_count("Bonjour") == 7
   assert get_letter_count("") == 0
   assert get_letter_count(".........hein???") == 4
   assert get_letter_count("Attention y'a quatre mots !") == 21
