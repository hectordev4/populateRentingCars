import json
import random
from datetime import datetime, timedelta

def generate_calendar():

    with open('cars.json', 'r') as f:
        cars = json.load(f)

    calendar_data = []

    for car in cars:
        operation = car["operation"]
        calendar_key = f"{operation}#calendar"

        start_date = datetime.now()
        dates = {}
        for _ in range(180):  # Generate 6 months of dates
            date = start_date.strftime("%y/%m/%d")
            dates[date] = True
            start_date += timedelta(days=1)

        calendar_entry = {
            "operation": calendar_key,
            "dates": dates
        }
        calendar_data.append(calendar_entry)

    with open('calendar.json', 'w') as f:
        json.dump(calendar_data, f, indent=2)

    print("Calendar data generated and saved to calendar.json")

if __name__ == "__main__":
    generate_calendar()