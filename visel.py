import random

def get_word(theme):
    themes = {
        "фрукты": ["яблоко", "банан", "апельсин", "груша", "слива", "aбрикос", "айва", "арбуз", "виноград", "гранат"],
        "животные": ["кот", "собака", "лошадь", "тигр", "крокодил", "панда", "олень", "гиппопотам", "львица", "жираф"],
        "страны": ["россия", "сша", "китай", "франция", "бразилия", "узбекистан", "германия", "япония", "нидерланды", "швейцария"]
    }
    words = themes.get(theme)
    if words:
        return random.choice(words)
    else:
        return None

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def get_guess():
    guess = input("Угадайте букву: ")
    return guess.lower()

def update_guessed_letters(guess, guessed_letters):
    guessed_letters.append(guess)

def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def play_again():
    choice = input("Хотите сыграть снова? (да/нет): ")
    return choice.lower() == 'да'

def main():
    print("Добро пожаловать в игру 'Виселица'!")
    play = True
    while play:
        theme = input("Выберите тему (фрукты, животные, страны): ")
        word = get_word(theme)
        if word:
            guessed_letters = []
            attempts = 6

            while attempts > 0:
                print(f"У вас осталось {attempts} попыток.")
                displayed_word = display_word(word, guessed_letters)
                print(displayed_word)

                guess = get_guess()
                update_guessed_letters(guess, guessed_letters)

                if guess not in word:
                    attempts -= 1

                if is_word_guessed(word, guessed_letters):
                    print(f"Вы угадали слово: {word}!")
                    break

            if attempts == 0:
                print(f"Вы не угадали слово: {word}.")

        else:
            print("Некорректная тема.")

        play = play_again()

    print("Спасибо за игру! До свидания!")

if __name__ == "__main__":
    main()