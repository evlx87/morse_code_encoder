"""
Программа помощник для изучения азбуки морзе
"""
import random

ANSWERS = []
WORDS = ["code", "bit", "list", "soul", "next"]
COUNT = 0


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


def print_statistics(answers_list):
    """Вывод статистики верных/неверных ответов"""
    count_correct = answers_list.count(True)
    count_incorrect = answers_list.count(False)
    print(f'''
    Отвечено верно: {count_correct}
    Отвечено неверно: {count_incorrect}
    ''')


def question():
    """Вывод вопроса и получение ответа"""
    word = get_word(WORDS)
    print(f"Угадай что загадано -  {morse_encode(word)}")
    answer = input("Мой ответ: ")
    if answer == word:
        print("Ответ верный!!!")
        ANSWERS.append(True)
    else:
        print(f"Вы ошиблись. Верный ответ: {word}")
        ANSWERS.append(False)


print("Сегодня мы потренируемся расшифровывать морзянку.")

start_command = input("Нажмите Enter и начнем")

if start_command == "":
    while COUNT < 5:
        question()
        COUNT += 1

    if COUNT == 5:
        print_statistics(ANSWERS)
else:
    print("Упс. Что-то пошло не так.")
