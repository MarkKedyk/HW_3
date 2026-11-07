class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return "[" + str(self.year) + "] [" + self.make + "] [" + self.model + "]"


Lamborghini = Car(make="Lamborghini", model="Huracan", year=2024)
print(Lamborghini.get_info())