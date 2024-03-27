import sqlite3

# Ma'lumotlar bazasini yaratish va bog'lash
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Foydalanuvchilar jadvalini yaratish
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Ma'lumotlarni saqlash uchun funksiya
def register(email, password):
    cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    print("Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi.")

# Foydalanuvchi kiritgan pochta va parolni tekshirish
def login(email, password):
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    if user:
        print("Muvaffaqiyatli kirish.")
    else:
        print("Kirishda xatolik. Bunday elektron pochtaga ega shaxs mavjud emas.")

# Elektron pochta va parolni kiritish
entered_email = input("Elektron pochta: ")
entered_password = input("Parol: ")

# Kirishni tekshirish
login(entered_email, entered_password)

# Ulanishni yopish
conn.close()