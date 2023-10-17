from statistics import mean


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.current_courses = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in
            self.current_courses and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else: lecturer.grades[course] = [grade]
        else:
            return "Error"
        
    def average_grade(self):
        average_grades = 0
        loop = 0
        for key in self.grades.keys():
            loop += 1
            average_grades += sum(self.grades[key])/len(self.grades[key])
        res = None
        if loop > 0:
            res = average_grades/loop
        else: 
            res = "У студента нет оценок по текущим курсам"
        return res

        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за ДЗ: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.current_courses)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
        
    def __lt__(self, other):
        res = None
        try:
           res = self.average_grade() < other.average_grade()
        except:
            res = "Нет оценок для сравнения"
        return res


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        
class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        average_grades = 0
        loop = 0
        for key in self.grades.keys():
            loop += 1
            average_grades += sum(self.grades[key])/len(self.grades[key])
        res = None
        if loop > 0:
            res = average_grades/loop
        else: 
            res = "У лектора нет оценок по лекциям"
        return res

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade()}\n')
    
    def __lt__(self, other):
        res = None
        try:
           res = self.average_grade() < other.average_grade()
        except:
            res = "Нет оценок для сравнения"
        return res
          

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
            and course in student.current_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n ')
    

# Функция для подсчета средней оценки.  
# По заданию нужно написать отдельно и для студентов и для лекторов.  
# Не стал это делать так как они идентичны, а это копипаста и лишние строки.  

def mean_grade(list, course):
    res = []
    for person in list:
        if course in person.grades.keys():
            res.append(mean(person.grades.get(course)))
    return mean(res)


# Вводные данные для теста методов и функций.  

student_01 = Student('Филипп', 'Панкратов', 'Male')
student_02 = Student('Екатерина', 'Безрукова', 'Female')
student_03 = Student('Владимир', 'Данилин', 'Male')
students_list = [student_01, student_02, student_03]

lecturer_01 = Lecturer('Владислав', 'Бояров')
lecturer_02 = Lecturer('Олег', 'Газманов')
lecturer_list = [lecturer_01, lecturer_02]

reviewer_01 = Reviewer('Василий', 'Коряков')
reviewer_02 = Reviewer('Денис', 'Иванов')

student_01.current_courses += ['Python']
student_02.current_courses += ['Git']
student_03.current_courses += ['Python']

student_01.finished_courses += ['Вводный модуль']
student_02.finished_courses += ['Вводный модуль', 'Python']
student_03.finished_courses += ['Вводный модуль']

lecturer_01.courses_attached += ['Python']
lecturer_02.courses_attached += ['Git']

reviewer_01.courses_attached += ['Python']
reviewer_02.courses_attached += ['Git']


# Тест методов и функций.  

student_01.rate_lecturer(lecturer_01, 'Python', 9)
student_02.rate_lecturer(lecturer_01, 'Python', 10)
student_03.rate_lecturer(lecturer_01, 'Python', 7)

print(f'\nОценки лектора {lecturer_01.name} {lecturer_01.surname}:'
      f'{lecturer_01.grades}')

student_01.rate_lecturer(lecturer_02, 'Python', 9)
student_02.rate_lecturer(lecturer_02, 'Git', 10)
student_03.rate_lecturer(lecturer_02, 'Git', 7)

print(f'Оценки лектора {lecturer_02.name} {lecturer_02.surname}:'
      f'{lecturer_02.grades}\n')

reviewer_01.rate_hw(student_01, 'Python', 10)
reviewer_01.rate_hw(student_01, 'Python', 8)
reviewer_01.rate_hw(student_01, 'Python', 10)

print(f'Оценки студента {student_01.name} {student_01.surname}:'
      f'{student_01.grades}')

reviewer_01.rate_hw(student_02, 'Python', 7)
reviewer_01.rate_hw(student_02, 'Git', 5)
reviewer_01.rate_hw(student_02, 'Python', 9)
reviewer_02.rate_hw(student_02, 'Git', 1)
reviewer_02.rate_hw(student_02, 'Git', 9)
reviewer_02.rate_hw(student_02, 'Git', 9)


print(f'Оценки студента {student_02.name} {student_02.surname}:'
      f'{student_02.grades}')

reviewer_01.rate_hw(student_03, 'Python', 7)
reviewer_01.rate_hw(student_03, 'Python', 7)
reviewer_01.rate_hw(student_03, 'Python', 9)

print(f'Оценки студента {student_03.name} {student_03.surname}:'
      f'{student_03.grades}\n')

print(reviewer_01)
print(reviewer_02)

print(lecturer_01)
print(lecturer_02)

print(student_01)
print(student_02)
print(student_03)


print(lecturer_01 < lecturer_02)
print(lecturer_01 > lecturer_02)
print(lecturer_01 == lecturer_02)
print(lecturer_01 != lecturer_02)
print(student_01 < student_02)
print(student_01 == student_03)
print()


print(mean_grade(students_list, 'Python'))
print(mean_grade(students_list, 'Git'))
print(mean_grade(lecturer_list, 'Python'))
print(mean_grade(lecturer_list, 'Git'))