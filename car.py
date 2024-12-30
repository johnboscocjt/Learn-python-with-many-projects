class Car:
    # constructor and attributes
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    # methods
    def drive(self):
        print(f"You drive the {self.model}")
        
    def stop(self):
        print(f"You stopped the {self.color} car")
        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
        
        