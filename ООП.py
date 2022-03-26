class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return output

    def rate_lecturer(self, specific_lecturer, course, grade):
        if isinstance(specific_lecturer, Lecturer) \
                and course in specific_lecturer.courses_attached \
                and course in self.courses_in_progress \
                and 0 < grade <= 10:
            specific_lecturer.grades.append(grade)
        else:
            return 'Ошибка'
        
        
    def average_grade(self, all_grades):
        if type(all_grades) is dict:
            amount_grades = []
            for grades in all_grades.values():
                for grade in grades:
                    amount_grades.append(grade)
            return averege_grade(amount_grades)
        elif type(all_grades) is list and all_grades[0] != None:
            average = round(sum(all_grades) / len(all_grades), 2)
            return average
        else:
            return "Ошибка!"
        

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return average_grade(self.grades) < average_grade(other_student.grades)
        else:
            return None
        
     


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
        return output
    
    
        def average_grade(self, all_grades):
        if type(all_grades) is dict:
            amount_grades = []
            for grades in all_grades.values():
                for grade in grades:
                    amount_grades.append(grade)
            return self.averege_grade(amount_grades)
        elif type(all_grades) is list and all_grades[0] != None:
            average = round(sum(all_grades) / len(all_grades), 2)
            return average
        else:
            return "Ошибка!"
        
        

    def __lt__(self):
        if isintasnce(other_lecturer, Lecturer):
            return average_grade(self.grades) < average_grade(other_lecturer.grades)
        else:
            return 'None'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Функция расчета среднего значения оценок:

    def average_grade(all_grades):
        if type(all_grades) is dict:
            amount_grades = []
            for grades in all_grades.values():
                for grade in grades:
                    amount_grades.append(grade)
            return averege_grade(amount_grades)
        elif type(all_grades) is list and all_grades[0] != None:
            average = round(sum(all_grades) / len(all_grades), 2)
            return average
        else:
            return "Ошибка!"

    # Функция расчета среднего значения оценокЖ

    def average_course_grade(all_students, current_course):
        all_course_grades = []
        for current_student in all_students:
            if current_course in current_student.grades.keys():
                for every_grade in current_student.grades.get(current_course):
                    all_course_grades.append(every_grade)
            else:
                print(f'Курс {current_course} отсутствует у студента {current_student.name} {current_student.surname}')
            return average_grade(all_course_grades)

    # Функция расчета среднего значения оценок:

    def average_lecturers_grade(all_lecturers):
        all_lecturers_grades = []
        for current_lecturer in all_lecturers:
            for every_grade in current_lecturer.grades:
                all_lecturers_grades.append(every_grade)
        return average_grade(all_lecturers_grades)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

# экземпляр студент1
student_1 = Student('Roy', 'Eman', '25')
student_1.courses_in_progress = ['Python']
student_1.courses_in_progress = ['English for IT']
student_1.finished_courses = ['Git']
student_1.grades['Python'] = [10, 10, 10, 10, 10, 10, 8]
student_1.grades['English for IT'] = [10, 10, 7]

# экземпляр студент2
student_2 = Student('Mike', 'Red', '40')
student_2.courses_in_progress = ['Python']
student_2.finished_courses = ['Git']
student_2.grades['Python'] = [4, 5, 6, 10]

student_list = [student_1, student_2]

# Экземпляр лектор1
lecturer_1 = Lecturer('Bill', 'Boops')
lecturer_1.courses_attached = ['Python']
lecturer_1.courses_attached = ['English for IT']
lecturer_1.courses_attached = ['Git']

# Экземпляр лектор2

lecturer_2 = Lecturer('Ray', 'Bitts')
lecturer_2.courses_attached = ['Python']
lecturer_2.courses_attached = ['English for IT']
lecturer_2.courses_attached = ['Git']

lecturer_list = [lecturer_1, lecturer_2]

# экземпляр  Эксперт:

cool_reviewer = Reviewer('Anton', 'Green')
cool_reviewer.courses_attached = ['Python']

# экземпляр  Эксперт2:

cool_reviewer_2 = Reviewer('Eddy', 'Grey')
cool_reviewer_2.courses_attached = ['Git']

print(student_1.name)

print(student_1 < student_2)
