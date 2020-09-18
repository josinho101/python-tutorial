class course:
    #class initializer
    def __init__(self, name):
        self.__name = name  # __ will mark property as private
        self.students = []

    #add student
    def add_student(self, name):
        self.students.append(name)
        self.__log_student(name)

    #return student count
    def get_student_count(self):
        return len(self.students)

    #get course name
    def get_course_name(self):
        return self.__name

    # log student name
    def __log_student(self, name): # __ will mark function as private
        print(name + " added as a student") 
                 
