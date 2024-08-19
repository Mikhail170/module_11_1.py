import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Работа с библиотекой requests:

#GET-запрос (позволяет получить данные с веб-страницы)

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.text)

# POST-запрос: Отправка данных на сервер

url = 'https://httpbin.org/post'
data = {'name': 'Alice', 'age': 30}
response = requests.post(url, data=data)
print(response.status_code)
print(response.json())

# Передача заголовков:

url = 'https://api.github.com/search/repositories'
params = {'q': 'requests+language:python'}
response = requests.get(url, params=params)
print(response.json())


# Работа с библиотекой pandas:


# Создание DataFrame из словаря
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Вывод первых двух строк DataFrame
print(df.head(2))

# Добавление нового столбца
df['Salary'] = [70000, 80000, 60000]

# Фильтрация данных: выбор людей старше 23 лет
filtered_df = df[df['Age'] > 23]

print(filtered_df)


# Загрузка данных из CSV файла
df = pd.read_csv('data.csv')

# Просмотр информации о данных
print(df.info())

# Статистический обзор данных
print(df.describe())

# Группировка данных и вычисление среднего значения
mean_salary_by_city = df.groupby('City')['Salary'].mean()
print(mean_salary_by_city)

# Работа с библиотекой matplotlib:

#Пример 1: Линейный график
#показывает как построить простой линейный график.

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Построение графика
plt.plot(x, y)

# Добавление заголовка и меток осей
plt.title("Линейный график")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Отображение графика
plt.show()

#Пример 2: Диаграмма рассеяния (Scatter Plot)
#Этот пример показывает, как создать диаграмму рассеяния, которая полезна
# для отображения зависимости между двумя переменными.



# Данные для диаграммы рассеяния
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# Построение диаграммы рассеяния
plt.scatter(x, y, color='r')

# Добавление заголовка и меток осей
plt.title("Диаграмма рассеяния")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Отображение графика
plt.show()

# Пример 3: Гистограмма
# Этот пример показывает, как построить гистограмму для распределения случайных данных.

data = np.random.randn(1000)

# Построение гистограммы
plt.hist(data, bins=30, edgecolor='black')

# Добавление заголовка и меток осей
plt.title("Гистограмма")
plt.xlabel("Значения")
plt.ylabel("Частота")

# Отображение графика
plt.show()
