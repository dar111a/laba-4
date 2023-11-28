import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

try:
    df = pd.read_csv('employees.csv', encoding='utf-8')

    # Перевірка наявності даних
    if df.empty:
        raise pd.errors.EmptyDataError("Файл CSV порожній або містить некоректні дані")

    # Виведення повідомлення про успішне відкриття файлу
    print('Ok')

    # Обчислення віку співробітників
    current_date = datetime.now()
    df['Дата народження'] = pd.to_datetime(df['Дата народження'], format='%d.%m.%Y')
    df['Вік'] = (current_date - df['Дата народження']).dt.days // 365

    # Розподіл співробітників за статтю
    gender_counts = df['Стать'].value_counts()
    print('Унікальні значення в колонці "Стать":', df['Стать'].unique())
    print('Кількість співробітників чоловічої статі:', gender_counts.get('Чоловік', 0))
    print('Кількість співробітників жіночої статі:', gender_counts.get('Жінка', 0))

    # Будуємо діаграму розподілу статі
    gender_counts.plot(kind='bar')
    plt.title('Розподіл співробітників за статтю')
    plt.xlabel('Стать')
    plt.ylabel('Кількість співробітників')
    plt.show()

    # Розподіл співробітників за віком у вказаних категоріях
    age_categories = ['all', 'younger_18', '18-45', '45-70', 'older_70']

    for category in age_categories:
        if category == 'all':
            age_filtered_df = df
            age_title = 'всі'
        elif category == 'younger_18':
            age_filtered_df = df[df['Вік'] < 18]
            age_title = 'до 18 років'
        elif category == '18-45':
            age_filtered_df = df[(df['Вік'] >= 18) & (df['Вік'] <= 45)]
            age_title = 'від 18 до 45 років'
        elif category == '45-70':
            age_filtered_df = df[(df['Вік'] > 45) & (df['Вік'] <= 70)]
            age_title = 'від 45 до 70 років'
        elif category == 'older_70':
            age_filtered_df = df[df['Вік'] > 70]
            age_title = 'понад 70 років'

        print(f"Кількість співробітників у віковій категорії '{age_title}': {len(age_filtered_df)}")

        # Будуємо діаграму розподілу віку
        age_filtered_df['Вік'].plot(kind='hist', bins=20, edgecolor='black')
        plt.title(f'Розподіл віку співробітників у віковій категорії "{age_title}"')
        plt.xlabel('Вік')
        plt.ylabel('Кількість співробітників')
        plt.show()


except pd.errors.EmptyDataError as e:
    print(e)
except FileNotFoundError:
    print("Файл CSV не знайдено")
except pd.errors.ParserError:
    print("Помилка при обробці файлу CSV")
except Exception as e:
    print(f"Сталася помилка: {str(e)}")
