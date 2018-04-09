# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 다른 딕셔너리나 긴 튜플을 값으로 담은 딕셔너리를 생성하지 말자
* 정식 클래스의 유언성이 필요 없다면 가벼운 불변 데이터 컨테이너에ㅐ는 namedtuple을 사용하자
* 내부 상태를 관리하는 딕셔너리가 복잡해지면 여러 헬퍼 클래스를 사용하는 방식으로 관리 코드를 바꾸자
'''

import collections


class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = []
    
    def report_grade(self, name, score):
        self._grades[name].append(score)
    
    def average_grades(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = SimpleGradebook()
book.add_student("Isaac Newton")
book.report_grade("Isaac Newton", 90)

print(book.average_grades("Isaac Newton"))

'''
90
'''


class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = {}
    
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)
    
    def average_grades(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count
    

book = BySubjectGradebook()
book.add_student("Albert Einstein")
book.report_grade("Albert Einstein", "Math", 75)
book.report_grade("Albert Einstein", "Math", 65)
book.report_grade("Albert Einstein", "Gym", 90)
book.report_grade("Albert Einstein", "Gym", 95)

print(book.average_grades("Albert Einstein"))

'''
81
'''


class WeightedGradebook(object):
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = {}
    
    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))
    
    def average_grades(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                # ...
                pass
            # ...
            pass
        return score_sum / score_count

# ..
# book.report_grade("Albert Einstein", "Math", 80, 0.10)


grades = []
grades.append((95, 0.45))

total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grades = total / total_weight

print(average_grades)

'''
95.0
'''


grades = []
grades.append((95, 0.45, "Great job"))

total = sum(score * weight for score, weight, _ in grades)
total_weight = sum(weight for _, weight, _ in grades)
average_grades = total / total_weight

print(average_grades)

'''
95.0
'''


Grade = collections.namedtuple("Grade", ("score", "weight"))

'''
'''


class Subject(object):
    def __init__(self):
        self._grades = []
    
    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))
    
    def average_grades(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student(object):
    def __init__(self):
        self._subjects = {}
    
    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]
    
    def average_grades(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grades()
            count += 1
        return total / count

class Gradebook(object):
    def __init__(self):
        self._students = {}
    
    def student(self, name):
        if name not  in self._students:
            self._students[name] = Student()
        return self._students[name]

book = Gradebook()

albert = book.student("Albert Einstein")
math = albert.subject("Math")
math.report_grade(80, 0.10)

print(albert.average_grades())

'''
80.0
'''
