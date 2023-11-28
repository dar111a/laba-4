from faker import Faker
import csv
import random
from datetime import datetime, timedelta

fake = Faker('uk_UA')
def MiddleNameMale(fake):
    male_middle_names = [
        "Васильович", "Ярославович", "Олегович", "Артемович", "Ігорович",
        "Максимович", "Романович", "Анатолійович", "Богданович", "Святославович",
        "Степанович", "Тарасович", "Віталійович", "Григорійович", "Зеновійович"
    ]
    return fake.random_element(male_middle_names)

def MiddleNameFemale(fake):
    female_middle_names = [
        "Василівна", "Ярославівна", "Олегівна", "Артемівна", "Ігорівна",
        "Максимівна", "Романівна", "Анатоліївна", "Богданівна", "Святославівна",
        "Степанівна", "Тарасівна", "Віталіївна", "Григоріївна", "Зеновіївна"
    ]
    return fake.random_element(female_middle_names)


# Створення CSV файлу
with open('employees.csv', mode='w', encoding='utf-8', newline='') as file:
    fieldnames = ['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    age_categories = ['all', 'younger_18', '18-45', '45-70', 'older_70']



    for category in age_categories:
        for _ in range(400):
            # Випадковий вибір статі
            gender = random.choice(['Чоловік', 'Жінка'])

            # Використання методу first_name_male або first_name_female
            first_name = fake.first_name_male() if gender == 'Чоловік' else fake.first_name_female()

            # Визначення віку в залежності від категорії
            if category == 'all':
                age = random.randint(20, 70)
            elif category == 'younger_18':
                age = random.randint(0, 17)
            elif category == '18-45':
                age = random.randint(18, 45)
            elif category == '45-70':
                age = random.randint(46, 70)
            elif category == 'older_70':
                age = random.randint(71, 100)

            # Запис у файл
            writer.writerow({
                'Прізвище': fake.last_name(),
                'Ім’я': first_name,
                'По батькові': MiddleNameMale(fake) if gender == 'Чоловік' else MiddleNameFemale(fake),
                'Стать': gender,
                'Дата народження': (datetime.now() - timedelta(days=365 * age)).strftime('%d.%m.%Y'),
                'Посада': fake.job(),
                'Місто проживання': fake.city(),
                'Адреса проживання': fake.address(),
                'Телефон': fake.phone_number(),
                'Email': fake.email(),
            })


print('Генерація завершена')
