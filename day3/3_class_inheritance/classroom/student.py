#!/usr/bin/python3

class Student(Person):

    def __init__(self, firstname, lastname, subject):
        super(Student, self).__init__(firstname, lastname)
        self.subject = subject

    def printNameSubject(self, firstname, lastname, subject):
        return "%s %s, %s" % (self.firstname, self.lastname, self.subject) 
