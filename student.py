class Student:

    def __init__(self, name_, age_, height_, gender_):
        self.name = name_
        self.age = age_
        self.height = height_
        self.gender = gender_
        self.score = 0

    def learn(self, test):
        self.score += test
    
    def __str__(self):
        return (f'Hello, my name is: {self.name}, {self.age}, {self.height}, {self.gender}, {self.score}')

lajos = Student("Lajos", 18, 178, "fiu")
anna = Student("Anna", 15, 170, "lany")


print(lajos.height)
print(lajos.name)
print(lajos.score)
lajos.learn(10)
lajos.learn(10)
print(lajos)
print(lajos.score)
print(anna)
print(anna.score)
