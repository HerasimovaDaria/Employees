import csv
from datetime import date
import matplotlib.pyplot as plt

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def analyze_employees(filename):
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Пропустити рядок заголовка

            male_ages = {'18-45': 0, '45-70': 0, 'older_70': 0}
            female_ages = {'18-45': 0, '45-70': 0, 'older_70': 0}

            for row in reader:
                gender = row[3]
                birth_date = date.fromisoformat(row[4])

                age = calculate_age(birth_date)

                if gender == 'Male':
                    if 18 <= age <= 45:
                        male_ages['18-45'] += 1
                    elif 46 <= age <= 70:
                        male_ages['45-70'] += 1
                    else:
                        male_ages['older_70'] += 1
                elif gender == 'Female':
                    if 18 <= age <= 45:
                        female_ages['18-45'] += 1
                    elif 46 <= age <= 70:
                        female_ages['45-70'] += 1
                    else:
                        female_ages['older_70'] += 1

            print("Аналіз співробітників за віковими категоріями:")
            print("Чоловіки:")
            print("Вік 18-45:", male_ages['18-45'])
            print("Вік 45-70:", male_ages['45-70'])
            print("Старше 70:", male_ages['older_70'])
            print("Жінки:")
            print("Вік 18-45:", female_ages['18-45'])
            print("Вік 45-70:", female_ages['45-70'])
            print("Старше 70:", female_ages['older_70'])

            # Побудова діаграми
            labels = ['18-45', '45-70', 'Старше 70']
            male_counts = [male_ages['18-45'], male_ages['45-70'], male_ages['older_70']]
            female_counts = [female_ages['18-45'], female_ages['45-70'], female_ages['older_70']]

            x = range(len(labels))
            width = 0.35

            fig, ax = plt.subplots(figsize=(10, 6))  # Розмір фігури
            rects1 = ax.bar(x, male_counts, width, label='Чоловіки')
            rects2 = ax.bar(x, female_counts, width, label='Жінки', bottom=male_counts)

            ax.set_ylabel('Кількість')
            ax.set_title('Вікова категорія співробітників за статтю')
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            ax.legend()

            # Вивести діаграму на екран
            plt.tight_layout()  # Для покращення відображення
            plt.show()

    except FileNotFoundError:
        print("Помилка: файл CSV не знайдено або не вдалося відкрити.")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    analyze_employees("employees.csv")
