class Student:

    def __init__(self, name_, age_, height_, gender_):
        self.name = name_
        self.age = age_
        self.height = height_
        self.gender = gender_
        self.score = 0

    def learn(self, test):
        self.score += test

    def introduce(self):
        return f'Hello, my name is: {self.name}. My age is: {self.age}'
    
    def __str__(self):
        return (f'Hello, my name is: {self.name}, {self.age}, {self.height}, {self.gender}, {self.score}')
