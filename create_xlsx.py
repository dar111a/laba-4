import pandas as pd
from datetime import datetime, timedelta

# Зчитування даних з CSV файлу
try:
    # Зчитування даних з CSV файлу та збереження їх у об'єкт DataFrame (структура даних Pandas)
    df = pd.read_csv('employees.csv')

    # Перевірка наявності даних
    if df.empty:
        raise pd.errors.EmptyDataError("Файл CSV порожній або містить некоректні дані")

    # Перетворення рядка у формат дати та розрахунок віку
    df['Дата народження'] = pd.to_datetime(df['Дата народження'], format='%d.%m.%Y')
    df['Вік'] = (datetime.now() - df['Дата народження']) // timedelta(days=365.25)  # Замінено timedelta64[ns] на days

    # Створення XLSX файлу з різними аркушами
    with pd.ExcelWriter('employees_data.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='all', index=False)

        age_ranges = [(0, 18), (18, 45), (45, 70), (70, 200)]
        sheet_names = ['younger_18', '18-45', '45-70', 'older_70']

        for sheet_name, (start_age, end_age) in zip(sheet_names, age_ranges):
            age_filtered_df = df[(df['Вік'] >= start_age) & (df['Вік'] < end_age)]
            age_filtered_df.to_excel(writer, sheet_name=sheet_name, index=False)

    print('Ok')  # Успішне завершення програми

except FileNotFoundError:
    print('Помилка: файл CSV не знайдено')

except pd.errors.EmptyDataError:
    print('Помилка: файл CSV порожній або містить некоректні дані')

except Exception as e:
    print(f'Помилка: {e}')