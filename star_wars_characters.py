import requests


class Darth_Vader():
    """Список актёров, которые играли с Дартом Вейдером"""

    def list_of_actors(self):
        """Запрос списка фильмов"""

        base_url = 'https://swapi.dev/api/'
        key = 'people/4/'

        "Метод GET для получения списка фильмов"

        get_url = base_url + key
        print(get_url)

        result_get = requests.get(get_url)
        assert 200 == result_get.status_code
        print('Статус код соответсвует!')
        films_list = result_get.json()
        films = films_list.get('films')
        print(films)

        "Метод GET для получения всех фильмов где снимался Вейдер"

        for list_films in films:
            films_url = list_films

            films_get = requests.get(films_url)

            characters_json = films_get.json()
            characters = set(characters_json.get('characters'))

        "Метод GET для получения списка героив из списка с фильмами"

        for list_characters in characters:
            characters_url = list_characters

            characters_get = requests.get(str(characters_url))

            characters_name = characters_get.json()
            name = characters_name.get('name')
            print(name)

            with open('characters_name.txt', 'a', encoding='utf-8') as file:
                if name == 'Darth Vader':
                    continue
                else:
                    file.write(f"{name}" + '\n')


actors = Darth_Vader()
actors.list_of_actors()
