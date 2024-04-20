import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з CSV файлу
data = pd.read_csv('Population,total.csv')

# Вибірка даних для України та Франції
ukraine_data = data[data['Country Name'] == 'Ukraine'].iloc[0, 4:-1]
france_data = data[data['Country Name'] == 'France'].iloc[0, 4:-1]

# Конвертація значень у числовий тип
ukraine_values = pd.to_numeric(ukraine_data)
france_values = pd.to_numeric(france_data)

# Отримання років
years = [int(year.split(' ')[0]) for year in ukraine_data.index]


# Функція для побудови графіку динаміки популяції
def plot_population_dynamics():
    plt.figure(figsize=(12, 6))
    plt.plot(years, ukraine_values, marker='o', label='Ukraine')
    plt.plot(years, france_values, marker='o', label='France')
    plt.title('Population Dynamics: Ukraine vs France (2000-2022)')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    plt.grid(True)
    plt.show()





# Функція для побудови стовпчастої діаграми для вибраної країни
def plot_bar_chart(country):
    if country == 'Ukraine':
        values = ukraine_values
        title = 'Population of Ukraine (2000-2022)'
    elif country == 'France':
        values = france_values
        title = 'Population of France (2000-2022)'
    else:
        print("Country not found.")
        return

    plt.figure(figsize=(12, 6))
    plt.bar(years, values, color='skyblue')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True, axis='y')
    plt.show()


# Виклик функції для візуалізації динаміки популяції
#plot_population_dynamics()

# Користувацький ввід для вибору країни
#country_input = input("Enter the country (Ukraine or France): ")
#plot_bar_chart(country_input)

while True:
    print("\nМеню:")
    print("1. Виклик функції для візуалізації динаміки популяції")
    print("2. Користувацький ввід для вибору країни")
    print("3. Вихід")

    choice = input("Оберіть опцію: ")

    if choice == '1':
        plot_population_dynamics()
    elif choice == '2':
        country_input = input("Enter the country (Ukraine or France): ")
        plot_bar_chart(country_input)
    elif choice == '3':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")