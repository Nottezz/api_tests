import requests

class Categories_joke():
    """Отображение шуток по всем категороиям"""

    def __init__(self):
        pass

    def categories_joke(self):
        url = 'https://api.chucknorris.io/jokes/categories'
        print(url)
        request = requests.get(url)
        print('Стасус код ' + str(request.status_code))
        assert 200 == request.status_code
        request.encoding = 'utf-8'
        print(request.text + '\n')  # Показывает весь список категорий
        categories = request.json()

        """Основной цикл, который при запуске будет показывать шутки по категориям"""
        for result in categories:
            url = f'https://api.chucknorris.io/jokes/random?category={result}'
            request = requests.get(url)
            joke_categories = request.json()
            joke_result = joke_categories.get('value')
            print(f'\nШутка из категории {result}\n'+ joke_result)




joke = Categories_joke()
joke.categories_joke()