class Cat:
    def __init__(self, name="", sex="", age=0):
        self.name = name
        self.sex = sex
        self.age = age
        self.setAge(age)

    def getAge(self):
        return self.age

    def setAge(self, age):
        if age >= 0 and isinstance(age, int):
            self.age = age
        else:
            self.age = "Недопустимый возраст!"

    def printAll(self):
        print(f"Кличка: {self.name} | Пол: {self.sex} | Возраст: {self.age}")
