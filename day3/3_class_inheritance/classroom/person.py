#!/usr/bin/python3

class Person(object):

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printName(self):
        return "%s %s" % (self.firstname, self.lastname)   

class Student(Person):

    def __init__(self, firstname, lastname, subject):
        super(Student, self).__init__(firstname, lastname)
        self.subject = subject

    def printNameSubject(self):
        return "%s %s, %s" % (self.firstname, self.lastname, self.subject) 

class Teacher(Person):
    
    def __init__(self, firstname, lastname, course):
        super(Teacher, self).__init__(firstname, lastname)
        self.course = course

    def printNameCourse(self):
        return "%s %s, %s" % (self.firstname, self.lastname, self.course)
