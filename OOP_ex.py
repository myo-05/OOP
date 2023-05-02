import os
os.system("cls")

class Car:
    def __init__(self,model,color,speed):
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self,speed):
        self.speed = max(self.speed+speed,0)
        
    def brake(self,speed):
        self.speed = max(self.speed-speed,0)
    
    def get_speed(self):
        return self.speed

# ===========================================================    

class Animal:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def speak(self):
        print("동물소리")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def speak(self):
        print(f"{self.name}: 멍뭉!")
    
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def speak(self):
        print(f"{self.name}: 냥냥!")
        
# ===========================================================    

class Shape:
    def get_area(self):
        pass

class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.name = "Circle"

    def get_area(self):
        return int(3.14*self.radius**2)

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.name = "Rectangle"

    def get_area(self):
        return self.length*self.width

# ==============실행공간==============

#Car    
mycar=Car("붕붕이", "빨간색", 100)
mycar.accelerate(130)
print(f"나의 {mycar.color} {mycar.model}는 현재[{mycar.get_speed()}Km/h]속력으로 달리고 있다구..!")
mycar.brake(40)
print(f"나의 {mycar.color} {mycar.model}는 현재[{mycar.get_speed()}Km/h]속력으로 달리고 있다구..!")

#Animal
mydog=Dog("코댕이", 4)
mycat=Cat("코냥이", 4)
mydog.speak()
mycat.speak()

#Shape
C = Circle(10)
R = Rectangle(10, 15)
print(f"반지름이 {C.radius}m인 {C.name}의 넓이는 {C.get_area()}\u33A1 입니다.")
print(f"길이{R.length}m/너비{R.width}m인 {R.name}의 넓이는 {R.get_area()}m² 입니다.")
