
#=======================================10. Inheritance====================================

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def introduce(self):
        return f"Hi, I'm {self.name}."

class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id


    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} My student ID is {self.student_id}."



class Teacher(Person):
    def __init__(self, name, email, teacher_id):
        super().__init__(name, email)
        self.teacher_id = teacher_id


    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} My teacher ID is {self.teacher_id}."

student = Student("Anchita", "Anchita@school.edu", "S12345")
print(student.introduce())
teacher = Student("Ousmane", "Ousmane@school.edu", "24193900")
print(teacher.introduce())



#=========Intermediate: Combining Mixins============
class LoggableMixin:
    def log(self, message):
        print(f"[LOG]: {message}")


class ExportableMixin:
    def to_dict(self):
        return self.__dict__


class UserProfile(LoggableMixin, ExportableMixin):
    def __init__(self, username):
        self.username = username
        self.log(f"User profile created for {username}")


user = UserProfile("clark_kent")

print(user.to_dict())