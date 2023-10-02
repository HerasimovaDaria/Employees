import xlsxwriter
import random
from faker import Faker

fake = Faker('uk_UA')

def generate_employee():
    gender = random.choice(['Male', 'Female'])
    first_name = fake.first_name_male() if gender == 'Male' else fake.first_name_female()
    last_name = fake.last_name_male() if gender == 'Male' else fake.last_name_female()
    middle_name = fake.first_name_male() if gender == 'Male' else fake.first_name_female()
    birth_date = fake.date_of_birth(tzinfo=None, minimum_age=25, maximum_age=70)
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, middle_name, gender, birth_date, position, city, address, phone, email]

def create_xlsx_file(data, filename):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    for row_num, row_data in enumerate(data):
        for col_num, cell_data in enumerate(row_data):
            worksheet.write(row_num, col_num, cell_data)

    workbook.close()  # Закрити робочу книгу, щоб зберегти її

if __name__ == "__main__":
    num_records = 2000  # Кількість записів
    header = ["Прізвище", "Ім'я", "По батькові", "Стать", "Дата народження", "Посада", "Місто", "Адреса", "Телефон", "Email"]
    data = [header] + [generate_employee() for _ in range(num_records)]

    create_xlsx_file(data, "employees.xlsx")
