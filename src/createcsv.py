import csv
import random
from faker import Faker
from datetime import date

fake = Faker()

def generate_employee():
    gender = random.choice(['Male', 'Female'])
    first_name = fake.first_name_male() if gender == 'Male' else fake.first_name_female()
    last_name = fake.last_name_male() if gender == 'Male' else fake.last_name_female()
    middle_name = fake.first_name_male() if gender == 'Male' else fake.first_name_female()  # Використовуємо first_name_female() для middle_name
    birth_date = fake.date_of_birth(tzinfo=None, minimum_age=25, maximum_age=70)
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, middle_name, gender, birth_date, position, city, address, phone, email]



def create_employee_csv(filename, num_records):
    header = ["Прізвище", "Ім'я", "По батькові", "Стать", "Дата народження", "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"]
    data = [header] + [generate_employee() for _ in range(num_records)]

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    create_employee_csv("employees.csv", 2000)
