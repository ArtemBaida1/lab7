def is_palindrome(word):
    return word == word[::-1]

def shortest_palindrome(sentence):
    words = sentence.split()
    shortest_word = min(words, key=len)
    if is_palindrome(shortest_word):
        print(f"Найкоротше слово '{shortest_word}' є паліндромом.")
    else:
        print(f"Найкоротше слово '{shortest_word}' не є паліндромом.")

sentence = input("Введіть рядок слів розділених пробілами: ")
shortest_palindrome(sentence)
