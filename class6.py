class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember: %s' % self.name)

    def tell(self):
        print('Name: ', self.name, 'Age: ', self.age)

class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher: %s' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "%d"' % self.salary)

class Student(SchoolMember):

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialized Student: %s' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "%d"' % self.marks)

t = Teacher('Shravan Shankar', 40, 70000)
s = Student('Jagdish', 22, 75)

members = [t,s]

for member in members:
    member.tell()
