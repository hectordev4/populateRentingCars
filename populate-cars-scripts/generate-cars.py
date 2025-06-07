import json
import random
import string  # Import string for alphabet generation
from datetime import datetime

current_year = datetime.now().year

manufacturer = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
models = ["Camry", "Civic", "Mustang", "Impala", "Altima"]
cars = []

for i in range(50):
    #Number plate generator format: 1234-ABC
    number_plate = f"{random.randint(1000, 9999)}-{''.join(random.choices(string.ascii_uppercase, k=3))}"
    
    operation = f"car#{current_year}#{number_plate}"
    
    car = {
        "delegationId": f"DELEG#001",
        "operation": operation,
        "manufacturer": random.choice(manufacturer),
        "model": random.choice(models),
        "numberPlate": number_plate,
        "year": current_year,
        "color": random.choice(["Blue", "Red", "Black", "White", "Green"]),
        "price": random.randint(50, 150),
        "rentedDates": f"{operation}#calendar"
    }
    cars.append(car)

with open('cars.json', 'w') as f:
    json.dump(cars, f, indent=2)

