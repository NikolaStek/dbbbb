import sqlite3
import db_manager

while True:
    print("\n=== ФІТНЕС-КЛУБ ===")
    print("1. Клієнти")
    print("2. Абонементи")
    print("3. Придбати абонемент")
    print("4. Вийти")

    try:
        choice = int(input("Вибір: "))
    except ValueError:
        print("Введіть число")
        continue

    if choice == 1:
        import clients

    elif choice == 2:
        import memberships

    elif choice == 3:
        conn = sqlite3.connect("fitness_club.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()

        if not clients:
            print("Немає клієнтів")
            conn.close()
            continue

        print("\nКлієнти:")
        for c in clients:
            print(c)

        try:
            cid = int(input("Введіть ID клієнта: "))
        except ValueError:
            print("Невірний ID")
            conn.close()
            continue

        client = None
        for c in clients:
            if c[0] == cid:
                client = c
                break

        if client is None:
            print("Клієнта не знайдено")
            conn.close()
            continue

        cursor.execute("SELECT * FROM memberships")
        memberships = cursor.fetchall()

        if not memberships:
            print("Немає абонементів")
            conn.close()
            continue

        print("\nАбонементи:")
        for m in memberships:
            print(m)

        try:
            mid = int(input("Введіть ID абонемента: "))
        except ValueError:
            print("Невірний ID")
            conn.close()
            continue

        membership = None
        for m in memberships:
            if m[0] == mid:
                membership = m
                break

        if membership is None:
            print("Абонемент не знайдено")
            conn.close()
            continue

        print(f"\n Клієнт {client[1]} придбав абонемент «{membership[1]}»")

        conn.close()

    elif choice == 4:
        print("До побачення!")
        break

    else:
        print("Невірний пункт меню")
