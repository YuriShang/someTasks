"""
Задача №2.

В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли
объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы
генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного,
имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". Для генерации таких
имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и вывести количество
животных на каждую букву алфавита. Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....

"""
from bs4 import BeautifulSoup as Soup
import requests
from datetime import datetime


start_time = datetime.now()
result = {}
link = 'https://inlnk.ru/jElywR'

print('Proccessing...')
while True:
    page = requests.get(link).text
    soup = Soup(page, "lxml")
    animals = soup.find_all('div', class_='mw-category-group')
    l = []

    for data in animals:
        if 'Знаменитые животные по алфавиту' in data.text or 'Породы собак по алфавиту' in data.text:
            continue
        l.append(data.text.split('\n'))

    for i in l:
        for j in i:
            if len(j) == 1:
                let = i[0]
                if not result.get(let):
                    result.setdefault(let, 0)
                continue
            result[let] += 1

    if result.get('A'):
        del result['A']
        break

    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница' and a.get('href'):
            link = 'https://ru.wikipedia.org/' + a.get('href')
        else:
            link = None

total = 0
for k, v in result.items():
    total += v
    print(f"{k}: {v}")

print()
print(f"Total animals: {total}")
print(f"Time: {datetime.now() - start_time}")