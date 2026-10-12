"""Module providing a function for interrupting incorrect input"""
import sys
# Проект FitLife - MVP версия 1.0

# Константные значения проекта
# норма воды на 1 кг веса
WATER_PER_KG = 30
# коэффициент перевода милилитров в литры
ML_TO_L = 1000

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
        if 0 <= user_age >= 120:
            print('Ошибка! Вероятно, вы ввели неверный возраст. Вы ввели:', user_age)
    except ValueError:
        print('Введено неверное значение! Используйте целые числа.')
        print('Ожидаемый формат: 24')
    except KeyboardInterrupt:
        print("Вы завершили программу")
        sys.exit()
    else:
        break

# 2. Сбор данных
while True:
    try:
        user_weight = float(input('Введите свой текущий вес (кг): '))
        if 0 <= user_weight >= 300:
            print('Ошибка! Вероятно, вы ввели неверный вес. Вы ввели:', user_weight)
    except ValueError:
        print('Введено неверное значение! Используйте числа с разделителем в виде точки.')
        print('Ожидаемый формат: 93.2')
    except KeyboardInterrupt:
        print("Вы завершили программу")
        sys.exit()
    else:
        break

while True:
    try:
        user_height = float(input('Введите свой рост (м): '))
        if 0 <= user_height >= 2.5:
            print('Ошибка! Вероятно введён неверный рост. Вы ввели:', user_height)
    except ValueError:
        print('Введено неверное значение! Введите свой рост в метрах с разделителем в виде точки.')
        print('Ожидаемый формат: 1.92')
    except KeyboardInterrupt:
        print("Вы завершили программу")
        sys.exit()
    else:
        break
print()

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)
# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_TO_L

# 4. Вывод красивого результата
print(f'Отчёт для пользователя: {user_name} ({user_age} г.)')
print(f'Индекс массы тела (ИМТ): {round(bmi, 1)}')
print(f'Норма воды в день (л): {round(water_l, 1)}')
print()
print("Расчет окончен. Будьте здоровы!")
