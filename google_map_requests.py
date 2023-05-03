import requests


class New_location():
    """Создание 5 новых локаций"""

    def create_new_location(self):
        """Создание локаций"""

        base_url = 'https://rahulshettyacademy.com'  # Базовый URL
        key = "?key=qaclick123"  # Параметр для всех запросов

        """Метод POST"""
        print('\nМЕТОД POST\n')

        for location in range(5):
            post_resourece = '/maps/api/place/add/json'  # Ресурст метода POST

            post_url = base_url + post_resourece + key
            print(post_url)

            json_for_create_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }

            result_post = requests.post(post_url, json=json_for_create_new_location)
            # print(result_post.text)
            print(f'Статус код - {result_post.status_code}')
            assert 200 == result_post.status_code
            print('Статус код соответсвует!')
            place_id = result_post.json().get('place_id')
            print('Place ID сформирован - ' + place_id)
            with open('place_id.txt', mode='w') as file:  # Запись информации по place_id в файл
                file.write(place_id + "\n")

        print('\nPlace ID сохранены\n')

        fr = open('place_id.txt', 'r')
        place_id = fr.readlines()
        fr.close()
        print(place_id)

        ""
        get_resource = '/maps/api/place/get/json'

        for places_id in place_id:
            places_id = places_id.rstrip()
            print(f'Place ID: {places_id}')
            get_url = f'{base_url} + {get_resource} + {key} + &place_id= + {places_id}'
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)
            assert result_get.status_code == 200
            print('Проверка локации успешна!')

        new_place_id = open('new_place_id.txt', 'w')

        ""
        delete_rosource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_rosource + key
        print(delete_url)

        for index in range(len(place_id)):
            if index % 2 != 0:
                places_id = place_id[index].rstrip()
                print(place_id)
                delete_json = {
                    'place_id': places_id
                }
                result_delete = requests.delete(delete_url, json=delete_json)
                print(result_delete.text)
                assert result_delete == 200
                print('Удаление прошло успешно')
            else:
                places_id = place_id[index].rstrip()
                get_url = base_url + get_resource + key + "&place_id=" + places_id
                print(get_url)
                result_get = requests.get(get_url)
                print(result_get.status_code)

                if result_get.status_code == 200:
                    new_place_id.write(f'{places_id}\n')
                    print(result_get.text)
                    assert result_get.status_code == 200
                    print('Проверка существующих локаций прошла успешно')

        print('Place ID обновлены!')

    print('\nПроверка New_location пройдена!')


location = New_location()
location.create_new_location()