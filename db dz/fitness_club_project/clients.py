import sqlite3

conn = sqlite3.connect("fitness_club.db")
cursor = conn.cursor()

print("\n--- КЛІЄНТИ ---")
print("1. Додати клієнта")
print("2. Переглянути клієнтів")
print("3. Оновити клієнта")
print("4. Видалити клієнта")

choice = int(input("Вибір: "))

if choice == 1:
    first_name = input("Ім'я: ")
    last_name = input("Прізвище: ")
    cursor.execute(
        "INSERT INTO clients (first_name, last_name) VALUES (?, ?)",
        (first_name, last_name)
    )
    conn.commit()
    print("Клієнта додано")

elif choice == 2:
    cursor.execute("SELECT * FROM clients")
    for client in cursor.fetchall():
        print(client)

elif choice == 3:
    cid = int(input("ID клієнта: "))
    fn = input("Нове ім'я: ")
    ln = input("Нове прізвище: ")
    cursor.execute(
        "UPDATE clients SET first_name=?, last_name=? WHERE id=?",
        (fn, ln, cid)
    )
    conn.commit()
    print("Оновлено")

elif choice == 4:
    cid = int(input("ID клієнта: "))
    cursor.execute("DELETE FROM clients WHERE id=?", (cid,))
    conn.commit()
    print("Видалено")

conn.close()