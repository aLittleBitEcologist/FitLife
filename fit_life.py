# Проект FitLife - MVP версия 1.0
"""Module providing a function for interrupting incorrect input"""
import sys

# Константные значения проекта
WATER_PER_KG = 30   # норма воды на 1 кг веса
ML_TO_L = 1000      # коэффициент перевода милилитров в литры
MAX_HEIGHT = 2.5    # макисмально возможный рост
MAX_WEIGHT = 300    # максимально возможный вес
MIN_VALUE = 0       # минимальное значение парамтеров

# 1. Знакомство
print('Привет! Я консольный бот помощник FitLife.')
print('Помогу рассчитать твои физиологические параметры.')
print()

while True:
    user_name = input('Введите ваше имя: ')
    if not user_name.strip():
        print('Ошибка! Имя не может быть пустым.')
    else:
        break

while True:
    try:
        user_age = int(input('Введите свой возраст: '))
        if MIN_VALUE <= user_age >= MAX_HEIGHT:
            print('Ошибка! Вы ввели неверный возраст. Вы ввели:', user_age)
    except ValueError:
        print('Введено неверное значение! Используйте целые числа.')
        print('Ожидаемый формат: 24')
    except KeyboardInterrupt:
        print('Вы завершили программу')
        sys.exit()
    else:
        break

# 2. Сбор данных
while True:
    try:
        user_weight = float(input('Введите свой текущий вес в кг (Пример: 93.2): '))
        if MIN_VALUE <= user_weight >= MAX_WEIGHT:
            print('Ошибка! Вы ввели неверный вес. Вы ввели:',
                  user_weight, '\n')
    except ValueError:
        print('Введено неверное значение! Вы ввели:', user_weight)
        print('Ожидаемый формат: 93.2')
    except KeyboardInterrupt:
        print('Вы завершили программу')
        sys.exit()
    else:
        break

while True:
    try:
        user_height = float(
            input('Введите свой рост в метрах (Пример: 1.92): '))
        if MIN_VALUE <= user_height >= MAX_HEIGHT:
            print('Ошибка! Введён неверный рост. Вы ввели:',
                  user_height, '\n')
    except ValueError:
        print('Введено неверное значение! Вы ввели:', user_height)
        print('Ожидаемый формат: 1.92')
    except KeyboardInterrupt:
        print('Вы завершили программу')
        sys.exit()
    else:
        break

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)
# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_TO_L

# 4. Вывод красивого результата
print(f'Отчёт для пользователя: {user_name} ({user_age} г.)')
print(f'Индекс массы тела (ИМТ): {round(bmi, 1)}')
print(f'Норма воды в день (л): {round(water_l, 1)}\n')
print("Расчет окончен. Будьте здоровы!")
