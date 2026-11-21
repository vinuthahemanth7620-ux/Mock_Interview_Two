
from abc import ABC, abstractmethod

class Appliance(ABC):
    def __init__(self, brand, model, power_rating):
        self.brand = brand
        self.model = model
        self.power_rating = power_rating

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class Fan(Appliance):
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")

    def display_details(self):
        print("Appliance: Fan")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Power Rating:", self.power_rating, "W")


class AC(Appliance):
    def turn_on(self):
        print("AC is ON")

    def turn_off(self):
        print("AC is OFF")

    def display_details(self):
        print("Appliance: AC")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Power Rating:", self.power_rating, "W")


class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine is ON")

    def turn_off(self):
        print("Washing Machine is OFF")

    def display_details(self):
        print("Appliance: Washing Machine")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Power Rating:", self.power_rating, "W")

fan = Fan("Usha", "Cool", 105)
ac = AC("Samsung", "Dual Inverter", 1500)
wm = WashingMachine("Dor", "EcoWash", 600)

print("********Smart Appliance Management *********")
print("1. Fan")
print("2. AC")
print("3. Washing Machine")

try:
    choice = int(input("Select an appliance (1-3): "))

    if choice == 1:
        appliance = fan
    elif choice == 2:
        appliance = ac
    elif choice == 3:
        appliance = wm
    else:
        raise ValueError("Invalid appliance selection")

    print("\n ***********Appliance Details *********")
    appliance.turn_on()
    appliance.display_details()

    hours = float(input("\nEnter usage hours: "))

    if hours < 0:
        raise ValueError("Usage hours cannot be negative")

    units = appliance.power_rating * hours / 1000
    cost = units * 8

    print("\n **********Electricity Bill **********")
    print(f"Units Consumed: {units:.2f} kWh")
    print(f"Total Cost: Rs. {cost:.2f}")

    appliance.turn_off()

except ValueError as e:
    print("Error:", e)
