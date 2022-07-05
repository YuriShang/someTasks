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
import asyncio
import aiohttp
from bs4 import BeautifulSoup as Soup
from datetime import datetime


result = {} # словарь с буквами и количеством живности
pages = [] # скачанные страницы, в списке храним не более 50
link = 'https://inlnk.ru/jElywR'


async def main(url):
    async with aiohttp.ClientSession() as session:
        print('Proccessing...')
        while True:
            async with session.get(url) as page:
                html = await page.text()
                pages.append(html)
                soup = Soup(html, "lxml")
                links = soup.find('div', id='mw-pages').find_all('a')
                for a in links:
                    if a.text == 'Следующая страница' and a.get('href'):
                        url = 'https://ru.wikipedia.org/' + a.get('href')

                # в списке храним не более 50 страниц, дабы не засорять ОЗУ
                if len(pages) >= 50:
                    await dict_builder()

            # если дошли да английской "A" (идет после "Я"), останавливаем процесс
            if result.get('A'):
                del result['A']
                break


async def dict_builder():
    for page in pages:
        soup = Soup(page, "lxml")
        parsed_data = soup.find_all('div', class_='mw-category-group')
        animals_group = []

        for data in parsed_data:
            if 'Знаменитые животные по алфавиту' in data.text or 'Породы собак по алфавиту' in data.text:
                continue
            animals_group.append(data.text.split('\n'))

        for animals in animals_group:
            for animal in animals:
                if len(animal) == 1:
                    let = animal

                    # если буквы нет в словаре, добавляем
                    if not result.get(let):
                        result.setdefault(let, 0)
                    continue
                result[let] += 1

    # после обработки всех страниц, очищаем список
    pages.clear()


start_time = datetime.now()
asyncio.get_event_loop().run_until_complete(main(link))

total = 0
for k, v in result.items():
    total += v
    print(f"{k}: {v}")

print()
print(f"Total animals: {total}")
print(f"Time: {datetime.now() - start_time}")