class Student(object):
    def __init__(self):
        self.__school = 'Full Sail'
        self._job = 'Student'
        self.degree = 'Web'
        self.medium = 'Code'
        self.language = 'Python'

    #prints out all the data
    def print_out(self):
        print self.__school
        print self._job
        print self.degree
        print self.medium
        print self.language

danny = Student()

Student.print_out(danny)