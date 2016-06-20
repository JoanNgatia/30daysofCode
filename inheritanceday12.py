# You are given two classes, Person and Student, where Person is the base
# class and Student is the derived class. Completed code for Person and a
# declaration for Student are provided for you in the editor. Observe that
# Student inherits all the properties of Person.

# Complete the Student class by writing the following:

# A Student class constructor, which has  parameters:
# A string, firstName.
# A string, lastName .
# An integer, id.
# An integer array scores (or vector) of test scores, .
# A char calculate() method that calculates a Student object's average and
# returns the grade character representative of their calculated average:


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.scores = scores
        self.idNumber = idNumber

    def calculate(self):
        total = 0
        subjects = len(self.scores)
        for val in self.scores:
            total += val
        average_grade = (total / subjects)
        if average_grade >= 90:
            return 'O'
        elif average_grade >= 80:
            return 'E'
        elif average_grade >= 70:
            return 'A'
        elif average_grade >= 55:
            return 'P'
        elif average_grade >= 40:
            return 'D'
        else:
            return 'T'
