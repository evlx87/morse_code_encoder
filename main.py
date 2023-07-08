"""
Программа помощник для изучения азбуки морзе
"""
import random

CODE_DICTIONARY = {
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "a": ".-",
    "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
    "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
    "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...",
    "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
    "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--",
    "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"
}
WORDS = ["code", "bit", "list", "soul", "next"]

answers = []
count = 0


def morse_encode(word, morse_encode_dict):
    """Перевод слова в код морзе"""
    encoded = []

    for char in word:
        if char in morse_encode_dict:
            encoded.append(morse_encode_dict[char])

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
    print(f"Угадай что загадано -  {morse_encode(word, CODE_DICTIONARY)}")
    answer = input("Мой ответ: ")
    if answer == word:
        print("Ответ верный!!!")
        answers.append(True)
    else:
        print(f"Вы ошиблись. Верный ответ: {word}")
        answers.append(False)


print("Сегодня мы потренируемся расшифровывать морзянку.")

start_command = input("Нажмите Enter и начнем")

if start_command == "":
    while count < 5:
        question()
        count += 1

    if count == 5:
        print_statistics(answers)
else:
    print("Упс. Что-то пошло не так.")
