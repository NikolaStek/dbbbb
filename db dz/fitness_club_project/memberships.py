import sqlite3

conn = sqlite3.connect("fitness_club.db")
cursor = conn.cursor()

print("\n--- АБОНЕМЕНТИ ---")
print("1. Додати абонемент")
print("2. Переглянути абонементи")
print("3. Оновити абонемент")
print("4. Видалити абонемент")

choice = int(input("Вибір: "))

if choice == 1:
    t = input("Тип: ")
    p = float(input("Ціна: "))
    d = int(input("Тривалість (днів): "))
    cursor.execute(
        "INSERT INTO memberships (type, price, duration) VALUES (?, ?, ?)",
        (t, p, d)
    )
    conn.commit()
    print("Абонемент додано")

elif choice == 2:
    cursor.execute("SELECT * FROM memberships")
    for m in cursor.fetchall():
        print(m)

elif choice == 3:
    mid = int(input("ID абонемента: "))
    t = input("Новий тип: ")
    p = float(input("Нова ціна: "))
    d = int(input("Нова тривалість: "))
    cursor.execute(
        "UPDATE memberships SET type=?, price=?, duration=? WHERE id=?",
        (t, p, d, mid)
    )
    conn.commit()
    print("✏Оновлено")

elif choice == 4:
    mid = int(input("ID абонемента: "))
    cursor.execute("DELETE FROM memberships WHERE id=?", (mid,))
    conn.commit()
    print("🗑Видалено")

conn.close()