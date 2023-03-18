#davaleba 1
class Rectangle:
    def __init__(self,width, length, color):
        self.width = width
        self.length = length
        self.color = color
    def perimeter(self):
        return self.length * self.width
    def area(self):
        return 2 * (self.width * self.length)
    obj_one = Rectangle (5, 1, "blue")
    obj_two = Rectangle (3, 3, "green")
    obj_three = Rectangle (7, 3, "purple")
    print(obj_one.area())
#dav2
class car:
    def __init__(self, brand, model,  color):
        self.brand = brand
        self.model= model
        self.color = color
    def __str__(self):
        return f"მანქანის ბრენდი არის {self.brand} , მისი მოდელია {self.model}, ხოლო მანქანის ფერი არის {self.color}"
    car_1= car("mustang", "ford", "red")
    print(car_1)
    car_2=car("prius", "toyota", "blue")
    print(car_2)
    car_3 = car("golf", "volkswagen", "green")
    print(car_3)

#3 dav
class dog:
    def __init__(self, breed = "Neapolian Mastiff", size = "დიდი", age = "5 წლის", color = "შავი"):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color
    def __str__(self):
        return f"ძაგლის ჯიშია {self.breed}, ზომა {self.size}, წლოვანება {self.age}, მისი ფერია {self.color}"
    def sleep(self):
        return f"ძაღლს ოთახში ძინავს"
    def eat(self):
        return f"ფიზიკის წიგნს ჭამს"
    def sit(self):
        return f"მდივანზე ზის"
    def run(self):
        return f"ძაღლი ეზოში დარბის"

dog_1 = dog()
print(dog_1)
dog_2 = dog("Maltase", "small", "2years old", "white")
print(dog_2)
dog_3 = dog("chow chow", "medium", "3years old", "brown")
print(dog_3)




