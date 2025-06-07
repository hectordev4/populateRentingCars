import json
import random
from datetime import datetime

current_year = datetime.now().year

makes = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
models = ["Camry", "Civic", "Mustang", "Impala", "Altima"]
cars = []

for i in range(50):
    operation = f"car#{current_year}#{i+1:03d}"
    car = {
        "delegationId": f"DELEG#001",
        "operation": operation,
        "make": random.choice(makes),
        "model": random.choice(models),
        "year": current_year,
        "color": random.choice(["Blue", "Red", "Black", "White", "Green"]),
        "rentedDates": f"{operation}#calendar",
        "price": random.randint(50, 100)
    }
    cars.append(car)

with open('cars.json', 'w') as f:
    json.dump(cars, f, indent=2)

