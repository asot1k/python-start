from datetime import datetime

name = input("Как тебя зовут? ")
now = datetime.now()
print(f"Привет, {name}!")
print(
    f"Сейчас {now.strftime('%H:%M:%S')} — хорошее время, чтобы начать учиться Python 😉")
