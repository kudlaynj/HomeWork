import pandas as pd
from urllib.parse import quote


def farm_1(self):
    data = {
        'Baralginum': [59, 34, 127],
        'Analgin': [33, 45, 56],
        'Paracytomol': [24, 45, 33]
    }
    farm_list_1 = pd.DataFrame.from_dict(data)
    farm_list_1
    print(farm_list_1)


print(farm_1(3))

url = quote(
    "https://ru.wikipedia.org/wiki/Таблица", safe=":/")  # Кодируем кириллицу
pd.read_html(url)  # Берём первую таблицу из списка всех найденных на веб-странице
print(url)

f = pd.read_csv("farm2.cvs")
print(f)
