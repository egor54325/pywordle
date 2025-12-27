from random import choice

with open("words.txt", 'r') as f:
    original_word = choice(f.readlines())
word = '_' * len(original_word)
attempts = 5
w = 'w'
battery_pictures = {
    0: """ ____________                                                   
|             |
|             |#     Это ваша батарея жизней.
|____________ |""",
    1: """ ____________                                                   
|             |
| ⬛           |#     Это ваша батарея жизней.
|____________ |""",
    2: """ ____________                                                   
|             |
| ⬛ ⬛        |#     Это ваша батарея жизней.
|____________ |""",
    3: """ ____________                                                   
|             |
| ⬛ ⬛ ⬛      |#     Это ваша батарея жизней.
|____________ |""",
    4: """ ____________                                                   
|             |
| ⬛ ⬛ ⬛ ⬛   |#     Это ваша батарея жизней.
|____________ |""",
    5: """ ____________                                                   
|             |
| ⬛ ⬛ ⬛ ⬛ ⬛ |#     Это ваша батарея жизней.
|____________ |"""
}
with open("picture5.txt", w) as f:
    f.write(battery_pictures[5])


def add_letter_to_word(answer, current_word, letter):
    new_string = ""
    for n, i in enumerate(current_word):
        if i == '_':
            if answer[n] == letter:
                new_string += letter
            else:
                new_string += '_'
        else:
            new_string += current_word[n]
    return new_string


def main():
    global attempts
    global words
    global original_word
    global battary_pictures
    while True:
        guess = input("Введите букву: ")
        if len(guess) > 1 and guess == original_word:
            print(f"Вы победили! Загаданное слово - это {original_word}")
        elif guess in original_word:
            word = add_letter_to_word(original_word, word, guess)
            print(f"Удачная попытка!\n{battery_pictures[attempts]}\n буквы в слове: {word}")
        else:
            attempts -= 1
            print(f"Неудачная попытка.\n{battery_pictures[attempts]}\n буквы в слове: {word}")
        if word == original_word:
            print(f"Вы победили! Загаданное слово - это {original_word}")
        if attempts == 0:
            print(f"Вы проиграли. Загадоное слово: {original_word}")
            break


if __name__ == "__main__":
        main()
        while True:
            want_to_play = input("Хочешь играть заново? (да/нет)")
            if want_to_play == "да":
                want_to_play = True
                main()
            elif want_to_play == "нет":
                want_to_play = False
                break
            else:
                print("Введите да или нет.")
