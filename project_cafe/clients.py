import sqlite3

conn = sqlite3.connect("cafe.db")
cursor = conn.cursor()

print("\n--- КЛІЄНТИ ---")
print("1. Додати клієнта")
print("2. Переглянути клієнтів")
print("3. Оновити клієнта")
print("4. Видалити клієнта")

choice = int(input("Вибір: "))

if choice == 1:
    name = input("Ім'я: ")
    balance = input("Баланс: ")
    cursor.execute(
        "INSERT INTO clients (name, balance) VALUES (?, ?)",
        (name, balance)
    )
    conn.commit()
    print("Клієнта додано!")

elif choice == 2:
    cursor.execute("SELECT * FROM clients")
    for client in cursor.fetchall():
        print(client)

elif choice == 3:
    cid = int(input("ID клієнта: "))
    fn = input("Нове ім'я: ")
    ln = input("Новий баланс: ")
    cursor.execute(
        "UPDATE clients SET name=?, balance=? WHERE id=?",
        (fn, ln, cid)
    )
    conn.commit()
    print("Оновлено!")

elif choice == 4:
    cid = int(input("ID клієнта: "))
    cursor.execute("DELETE FROM clients WHERE id=?", (cid,))
    conn.commit()
    print("Видалено!")

conn.close()