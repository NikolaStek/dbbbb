import sqlite3
import database

while True:
    print("\n=== КАФЕ ===")
    print("1. Клієнти")
    print("2. Послуги")
    print("3. Придбати Послугу")
    print("4. Вийти")

    try:
        choice = int(input("Вибір: "))
    except ValueError:
        print("Введіть число")
        continue

    if choice == 1:
        import clients

    elif choice == 2:
        import services

    elif choice == 3:
        conn = sqlite3.connect("cafe.db")
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
            print("Клієнта не знайдено!")
            conn.close()
            continue

        cursor.execute("SELECT * FROM services")
        services = cursor.fetchall()

        if not services:
            print("Немає послуги!")
            conn.close()
            continue

        print("\nПослуги:")
        for m in services:
            print(m)

        try:
            mid = int(input("Введіть ID Послуги: "))
        except ValueError:
            print("Невірний ID")
            conn.close()
            continue

        service = None
        for m in services:
            if m[0] == mid:
                service = m
                break

        if service is None:
            print("Послугу не знайдено!")
            conn.close()
            continue


        if client[2] < service[2]:
            print("Недостатньо коштів!")
            conn.close()
            continue

        new_balance = client[2] - service[2]
        cursor.execute(
            "UPDATE clients SET balance=? WHERE id=?",
            (new_balance, client[0])
        )

        cursor.execute(
            "INSERT INTO orders (client_name, service_name, price) VALUES (?, ?, ?)",
            (client[1], service[1], service[2])
        )

        conn.commit()
        conn.close()

        print(f"Клієнт {client[1]} придбав послугу {service[1]} за {service[2]} грн")

    elif choice == 4:
        print("До побачення!")
        break

    else:
        print("Невірний пункт меню")