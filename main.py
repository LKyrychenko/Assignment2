import random
import time

# Привітання та авторизація
print("Привіт!✨")
print("Будь ласка, введи своє ім'я")
nickname = input()
print(f"Приємно познайомитися, {nickname}")
print("Вітаю в грі <<Вгадай число>>")
time.sleep(3)

# Інструкція до гри
print("^^^" * 50)
print("ПРАВИЛА ГРИ:")
print("Комп'ютер обирає ціле число від 1 до 50 включно.")
print("Тобі потрібно його відгадати за 6 спроб.")
print("Якщо твоє число менше, я скажу 'Моє число більше'.")
print("Якщо твоє число більше, я скажу 'Моє число менше'.")
print("Також ти можеш завершити гру в будь-який момент, просто написавши 'exit")
print("^^^"*50)
time.sleep(5)
while True:
    start = input("Якщо ти готовий, напиши 'Go' або 'Exit' для завершення: ").lower()
    if start == 'exit':
        break
    if start != 'go':
        print("Перечитай уважніше правила гри🌞")
        continue

    print("Let's go!")
    time.sleep(1)

    attempts = 0
    max_attempts = 6
    computer = random.randint(1, 50)
    print(f"У тебе є {max_attempts} спроб, щоб відгадати число.")
    while attempts < max_attempts:
        user_input = input(f"Спроба {attempts + 1}: ")

        if user_input.lower() == 'exit':
            print("🚪 Ти завершив гру. До зустрічі!")
            break

        if not user_input.isdigit():
            print("❌ Помилка! Потрібно вводити тільки цілі числа.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < computer:
            print("Моє число більше!")
        elif guess > computer:
            print("Моє число менше!")
        else:
            print(f"🥳 Ти переміг за {attempts} спроб. Вітаю!")
            break
    else:
        print(f"😵 Твоя кількість спроб вичерпана. Загадане число було {computer}.")

    play_again = input("Хочеш зіграти ще раз? (Yes/No): ").lower()
    if play_again != "yes":
        print("Дякую за гру! До зустрічі 👋")
        break