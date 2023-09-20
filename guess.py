import random

def play_again():
    choice = input("Хотите сыграть снова? (да/нет): ")
    return choice.lower() == 'да'

def main():
    print("Добро пожаловать в игру 'Угадай число'!")
    play = True
    while play:
        number = random.randint(1, 100)
        attempts = 0

        while True:
            guess = int(input("Угадайте число от 1 до 100: "))
            attempts += 1

            if guess < number:
                print("Загаданное число больше.")
            elif guess > number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляю! Вы угадали число {number} за {attempts} попыток.")
                break

            if abs(guess - number) <= 5:
                print("Вы очень близки к загаданному числу!")
            elif abs(guess - number) <= 10:
                print("Вы близки к загаданному числу.")
            else:
                print("Вы далеки от загаданного числа.")

        play = play_again()

    print("Спасибо за игру! До свидания!")

if __name__ == "__main__":
    main()