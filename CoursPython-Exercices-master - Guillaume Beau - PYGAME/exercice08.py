def get_word_count(sentence):
       phrase = (input("Écrire un mot ou une phrase: "))
       prec, nbmots=' ', 0
       for char in sentence:
              nbmots += int(prec == ' ' and char != ' ')
              prec = char
       return

def run():
   assert get_word_count("Bonjour") == 1
   assert get_word_count("Bonjour toi") == 2
   assert get_word_count("Bonjour ca va ?") == 3
   assert get_word_count("Bonjour ca va toi ?!") == 4
   assert get_word_count("") == 0
