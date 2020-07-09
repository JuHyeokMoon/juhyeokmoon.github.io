# class car :
#     def color(self, car_color):
#         self.car_color = car_color

# yellowcar = car()
# yellowcar.color("yellow")
# print(yellowcar.car_color)

# class car :
#     def color(self, car_color):
#         self.car_color = car_color
#         self.carPrint()

#     def carPrint(self):
#         print("class Car")

# yellowcar = car()
# yellowcar.color("yellow")
# print(yellowcar.car_color)

class Car:
    def __init__(self, colorV, speedV):
        self.c_color = colorV
        self.speed = speedV
    def upSpeed(self, up_value):
        self.speed = up_value
    def downSpeed(self, down_value):
        self.speed = down_value
    def color(self, car_color):
        self.c_color = car_color
    
redCar = Car("red",10)
blueCar = Car("blue", 20)
lowcar = Car("dd",30)
lower_car = lowcar.upSpeed(50)
print(redCar.c_color, redCar.speed, lower_car.speed)