class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.__password = password

    def login(self):
        return f"(User {self.first_name} is login)"

    def logout(self):
        return f"(User {self.first_name} is logout)"

    def get_password(self):
        return self.__password

    def __str__(self):
        return f"User {self.first_name} {self.last_name}, {self.username}, {self.get_password()}"

user = User("Eldor", "Bek", "<EMAIL>", "<PASSWORD>")



class Teacher(User):
    def __init__(self, first_name, last_name, username, password, teacher_id, phone_number, email):
        super().__init__(first_name, last_name, username, password)
        self.teacher_id = teacher_id
        self.phone_number = phone_number
        self.email = email

    def teacher(self):
        return f"(Teacher {self.teacher_id}"

    def phone_number(self):
        return self.phone_number

    def email(self):
        return self.email

    def __str__(self):
        return f"""Teacher 
        {self.teacher_id}, {self.phone_number}, 
        {self.email}, {self.get_password()}, 
        {self.teacher_id}, {self.phone_number}"""

ustoz = Teacher("Ali", "Bek", "alibek", "191583174", "7361", "8976270678", "bekali12@email.com")

class Assistent(Teacher):
    def __init__(self, first_name, last_name, username, password, teacher_id, phone_number, email, subjekt):
        super().__init__(first_name, last_name, username, password, teacher_id, phone_number, email)
        self.__subjekt = subjekt

    def get_subjekt(self):
        return self.__subjekt

    def __str__(self):
        return f"""Teacher 
           {self.teacher_id}, {self.phone_number}, 
           {self.email}, {self.get_password()}, 
           {self.teacher_id}, {self.phone_number}
           {Assistent.get_password(self)}
           """

yordamchi = Assistent("Aziz", "Jon", "Aziz Jon", "gap21345", "7462", "993344556", "aziz123@email.com","English")

class Mentor(Assistent):
    def __init__(self, first_name, last_name, username, password, teacher_id, phone_number, email, subjekt, group, working_teacher):
        super().__init__(first_name, last_name, username, password, teacher_id, phone_number, email, subjekt)
        self.working_teacher = working_teacher
        self.group = group

    def get_working_teacher(self):
        return self.working_teacher

    def get_group(self):
        return self.group

    def __str__(self):
        return f"""\nTeacher
        {self.teacher_id}, {self.phone_number}, 
        {self.email}, {self.get_password()}, 
        {self.teacher_id}, {self.phone_number}
        {self.__subjekt}, {self.group}, {self.working_teacher}
        """

ment = Mentor("Shaxzod", "Ali", "Shaxzod Ali", "27151637490", "0923", "952837456", "nmagap@email.com", "Adabiyot","9G", "2 soat")

print(user.login())
print(user.logout())

print(ustoz.login())
print(ustoz.logout())

print(yordamchi.login())
print(yordamchi.logout())

print(ment.login())
print(ment.logout())