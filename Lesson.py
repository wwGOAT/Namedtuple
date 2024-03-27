class Bace:
    def __init__(self, homework: str, data: str, reyting: str, status: str, comment: str, name: str, id: int, teacher: str):
        self.homework = homework
        self.data = data
        self.reyting = reyting
        self.status = status
        self.homework = homework
        self.comment = comment
        self.name = name
        self.id = id
        self.teacher = teacher

    def ful_name(self):
        return self.name, self.id

    def ful_homework(self):
        return self.homework, self

    def ful_reyting(self):
        return self.reyting

    def __str__(self):
        return self.name, self.id, self.homework, self.data, self.reyting, self.status


bas = Bace("OOT", "qwefyu", "27", "g76934g", "irbqrv", "Mustafo", 24379, "qwefyu")

class Lesson(Bace):
    def __init__(self, homework, data, reyting, status, comment, name, id, teacher, active_students: str):
        super().__init__(homework, data, reyting, status, comment, name, id, teacher)
        self.active_students = active_students

    def ful_name(self):
        return self.name, self.id

    def ful_homework(self):
        return self.homework, self

    def ful_reyting(self):
        return self.reyting

vazifa = Lesson("Vazifa", "hbnqwuh", "12", "jnuenh", "nhucnhen", "Bob", 51525, "Ali", "1xfb048")


class Subject(Lesson):
    def __init__(self, homework, data, reyting, status, comment, name, id, teacher, active_students, teacher_name):
        super().__init__(homework, data, reyting, status, comment, name, id, teacher, active_students)
        self.teacher_name = teacher_name

fan = Subject("OOP", "qwefyu", "27", "g76934g", "irbqrv", "Eldor", 21515, "qwefyu", "qwefyu", "Ali")
print(bas.ful_name())
print(vazifa.ful_name())
print(fan.ful_name())