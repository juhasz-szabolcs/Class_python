class Student:
    name = ""
    age = 0
    height = 0
    gender = ""
    score = 0

    def learn(self, test):
        self.score += test
    
    def __str__(self):
        return (f'Hello, my name is: {self.name}, {self.age}, {self.height}, {self.gender}, {self.score}')

lajos = Student()
anna = Student()
print(lajos.height)
lajos.name = "Lajos"
lajos.age = 13
lajos.height = 178
lajos.gender = "fiu"
print(lajos.height)
print(lajos.name)
print(lajos.score)
lajos.learn(10)
lajos.learn(10)
print(lajos.score)

print(lajos)
print(anna)
