# object oriented programming in python

# you can place a class in a new python file
# class Car:
    # constructor
    # def __init__(self, model, year, color, for_sale):
    #     self.model = model
    #     self.year = year
    #     self.color = color
    #     self.for_sale = for_sale
    
from car import Car
        
# to construct the car object we need a unique name for the car object
car1 = Car("Mustang", 2024, "red", False)
       
# print(car1.model)