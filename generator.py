import pandas as pd
import random

class SyntheticDataGenerator:
    def __init__(self):
        self.first_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah"]
        self.last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia"]
        self.cities = ["New York", "London", "Berlin", "Tokyo", "Sydney", "Toronto", "Paris", "Singapore"]

    def generate_records(self, num_rows: int = 100):
        data = []
        for i in range(num_rows):
            record = {
                "id": f"REC-{10000 + i}",
                "first_name": random.choice(self.first_names),
                "last_name": random.choice(self.last_names),
                "age": random.randint(18, 70),
                "city": random.choice(self.cities),
                "income": round(random.uniform(30000, 150000), 2),
                "churn_risk": random.choice(["Low", "Medium", "High"])
            }
            data.append(record)
        return pd.DataFrame(data)
