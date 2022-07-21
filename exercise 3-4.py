class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_co(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_reading:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        average = {}
        for courses, rating in self.grades.items():
            average = sum(rating) / len(rating)
        return average

    def __str__(self):
        word = str(self.courses_in_progress)[1:-1].replace("'", "")
        res = f'Имя: {self.name}' '\n' \
              f'Фамилия: {self.surname}' '\n' \
              f'Средняя оценка за домашние задания: {self.average_rating()}''\n' \
              f'Курсы в процессе изучения: {word}''\n' \
              f'Завершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Game Over")
            return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_reading = []
        self.grades = {}

    def average_rating(self):
        average = {}
        for courses, rating in self.grades.items():
            average = sum(rating) / len(rating)
        return average

    def __str__(self):
        res = f'Имя: {self.name}' '\n'\
              f'Фамилия: {self.surname}' '\n'\
              f'Средняя оценка за лекции: {self.average_rating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Game Over2")
            return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}''\n' \
              f'Фамилия: {self.surname}'
        return res

# Экземляры


Anton_student = Student('Anton', 'Smith', 'guy')
Anton_student.courses_in_progress += ['Python']

Vitaly_student = Student('Vitaly', 'Smath', 'guy')
Vitaly_student.courses_in_progress += ['Python']

Gleb_lecturer = Lecturer('Gleb', 'Smoth')
Gleb_lecturer.courses_reading += ['Python']

Daniil_lecturer = Lecturer('Daniil', 'Smeth')
Daniil_lecturer.courses_reading += ['Python']

Ivan_reviewer = Reviewer('Ivan', 'Stiv')
Ivan_reviewer.courses_attached += ['Python']

Kirill_reviewer = Reviewer('Kirill', 'Steh')
Kirill_reviewer.courses_attached += ['Python']

# Проверка методов

Anton_student.rate_co(Gleb_lecturer, 'Python', 5)
Anton_student.rate_co(Gleb_lecturer, 'Python', 7)

Vitaly_student.rate_co(Daniil_lecturer, 'Python', 10)
Vitaly_student.rate_co(Daniil_lecturer, 'Python', 8)

Ivan_reviewer.rate_hw(Anton_student, 'Python', 5)
Ivan_reviewer.rate_hw(Anton_student, 'Python', 9)

Kirill_reviewer.rate_hw(Vitaly_student, 'Python', 10)
Kirill_reviewer.rate_hw(Vitaly_student, 'Python', 6)

# функции

student_list = [Anton_student, Vitaly_student]
lecturer_list = [Gleb_lecturer, Daniil_lecturer]


def rate_student():
    sum_all = 0
    count_all = 0
    for student in student_list:
        if isinstance(student, Student):
            for b1, b2 in student.grades.items():
                sum_all += student.average_rating()
                count_all += 1
    average_all = sum_all / count_all
    return average_all


def rate_lecturer():
    sum_all = 0
    count_all = 0
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer):
            for b1, b2 in lecturer.grades.items():
                sum_all += lecturer.average_rating()
                count_all += 1
    average_all = sum_all / count_all
    return average_all


print(rate_student())
print(rate_lecturer())

print(Anton_student)
print()
print(Vitaly_student)
print()
print(Ivan_reviewer)
print()
print(Kirill_reviewer)
print()
print(Gleb_lecturer)
print()
print(Daniil_lecturer)
print()
