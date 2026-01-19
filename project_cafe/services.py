import sqlite3

conn = sqlite3.connect("cafe.db")
cursor = conn.cursor()

print("\n--- ПОСЛУГИ ---")
print("1. Додати послугу")
print("2. Переглянути послугу")
print("3. Оновити послугу")
print("4. Видалити послугу")

choice = int(input("Вибір: "))

if choice == 1:
    t = input("Назва: ")
    p = float(input("Ціна: "))
    d = int(input("Тривалість (днів): "))
    cursor.execute(
        "INSERT INTO services (name, price, duration) VALUES (?, ?, ?)",
        (t, p, d)
    )
    conn.commit()
    print("Послугу додано!")

elif choice == 2:
    cursor.execute("SELECT * FROM services")
    for m in cursor.fetchall():
        print(m)

elif choice == 3:
    mid = int(input("ID послуги: "))
    t = input("Нова назва: ")
    p = float(input("Нова ціна: "))
    d = int(input("Нова тривалість: "))
    cursor.execute(
        "UPDATE services SET name=?, price=?, duration=? WHERE id=?",
        (t, p, d, mid)
    )
    conn.commit()
    print("Оновлено!")

elif choice == 4:
    mid = int(input("ID послуги: "))
    cursor.execute("DELETE FROM services WHERE id=?", (mid,))
    conn.commit()
    print("Видалено!")

conn.close()