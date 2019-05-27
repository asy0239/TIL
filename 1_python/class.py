class Course:
    name = '4차4기'

    def introduce(self):
        return self.name


course = Course()
x = course.introduce()
print(x)

def greeting():
    return 'Hello'


y = greeting()
print(y)
