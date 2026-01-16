def safe_int(text):
    while True:
        try:
            value = int(input(text))
            break
        except ValueError:
            print("Введи число!")
    result = value