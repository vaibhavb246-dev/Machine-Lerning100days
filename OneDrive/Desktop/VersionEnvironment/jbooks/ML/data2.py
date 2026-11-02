import csv
import random
from datetime import date, timedelta

random.seed(42)

filename = "machine_learning_pandas_practice_200x20.csv"

columns = [
    "id", "name", "age", "gender", "city",
    "salary", "price", "experience_years", "is_student",
    "is_employed", "department", "rating", "score", "quantity",
    "join_date", "has_license", "education", "income",
    "discount_percent", "purchase_amount"
]

names = ["Aarav", "Vivaan", "Aditya", "Arjun", "Rahul",
         "Rohan", "Neha", "Priya", "Sneha", "Ananya"]

genders = ["Male", "Female", "Other"]

cities = ["Nagpur", "Pune", "Mumbai", "Delhi",
          "Bengaluru", "Hyderabad", "Chennai", "Nashik"]

departments = ["IT", "HR", "Finance", "Marketing",
               "Sales", "Operations"]

education = ["10th", "12th", "Diploma", "B.Tech",
             "M.Tech", "MBA"]

start_date = date(2020, 1, 1)

with open(filename, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Column names
    writer.writerow(columns)

    # 200 rows
    for i in range(1, 201):

        age = random.randint(18, 55)

        salary = random.randint(18000, 150000)

        price = round(random.uniform(100, 100000), 2)

        experience = round(random.uniform(0, 15), 1)

        student = random.choice([True, False])

        employed = random.choice([True, False])

        rating = round(random.uniform(1, 5), 2)

        score = round(random.uniform(0, 100), 2)

        quantity = random.randint(1, 20)

        discount = round(random.uniform(0, 50), 2)

        purchase_amount = round(
            price * quantity * (1 - discount / 100), 2
        )

        join_date = (
            start_date +
            timedelta(days=random.randint(0, 2400))
        ).isoformat()

        row = [
            i,
            random.choice(names),
            age,
            random.choice(genders),
            random.choice(cities),
            salary,
            price,
            experience,
            student,
            employed,
            random.choice(departments),
            rating,
            score,
            quantity,
            join_date,
            random.choice([True, False]),
            random.choice(education),
            random.randint(15000, 200000),
            discount,
            purchase_amount
        ]

        writer.writerow(row)

print("CSV file created successfully!")
print("File name:", filename)
print("Rows: 200")
print("Columns: 20")