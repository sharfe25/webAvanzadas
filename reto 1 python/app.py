def is_palindrome(word):
    inverted_word = word[::-1]
    if word == inverted_word:
        return True
    else:
        return False

word = input("Ingrese una palabra: ")

if is_palindrome(word):
    print(f"{word} es un palindromo.")
else:
    print(f"{word} no es un palindromo.")

