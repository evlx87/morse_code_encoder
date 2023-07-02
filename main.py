"""
Программа помощник для изучения азбуки морзе
"""
import random

answers = []
words = ["code", "bit", "list", "soul", "next"]


def morse_encode(word):
    """Перевод слова в код морзе"""
    cods_dictionary = {
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "a": ".-",
        "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
        "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
        "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...",
        "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
        "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--",
        "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"
    }

    encoded = []

    for char in word:
        if char in cods_dictionary:
            encoded.append(cods_dictionary[char])

    return ' '.join(encoded)


def get_word(words_list):
    """Выбираем случайное слово из списка"""
    random_word = random.choice(words_list)

    return random_word


# def print_statistics(answers):


print('''Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем
''')

print(morse_encode("test"))
