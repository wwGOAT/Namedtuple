class User:
    def __init__(self, first_name: str, last_name: str, username: str, password: str, email: str, gender: str, address: str, telephone: int, birth_date: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.gender = gender
        self.address = address
        self.telephone = telephone
        self.birth_date = birth_date

    def ful_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def get_address(self):
        return self.address

    def ful_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Name: {self.ful_name()} \nUsername: {self.username}, \nPassword: {str(self.get_password())}, \nGender: {self.get_gender()}, \nAddress: {self.get_address()}, \nBirthday: {self.birth_date}"

user =  User("Ali", "Aliyev", "eldor7", "ELDOR1234", "bekeldor10@gmail.com",  "Erkak", "Toshkent", 931244520, "01.01.2000")
print(user.ful_name())


class Person(User):
    def __init__(self, first_name: str, last_name: str, username: str, password: str, email: str, gender: str, address: str,telephone_number: str, birth_date: str):
        User.__init__(self, first_name, last_name, username, password, email, gender, address)
        self.telephone_number = telephone_number
        self.birth_date = birth_date

    def get_telephone_number(self):
        return f"Telefon number : {self.telephone_number}"

foydalanuvchi = Person("Eldor", "Bek", "eldor7", "ELDOR1234", "bekeldor123@gmail.com", "Erkak", "Tashkent", 931244520, "01/01/2008")

print(foydalanuvchi.get_telephone_number())