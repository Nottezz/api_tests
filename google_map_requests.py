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
            check_post = result_post.json()
            place_id = check_post.get('place_id')
            print('Place ID сформирован - ' + place_id)
            with open('place_id.txt', mode='a') as file:  # Запись информации по place_id в файл
                file.write(place_id + "\n")

        print('\nPlace ID сохранены\n')

        file = open('place_id.txt')
        read_file = file.readlines()  # Чтение созданного файла списком

        """Метод GET"""
        print('МЕТОД GET\n')
        for place_id_list in read_file:
            get_resourece = "/maps/api/place/get/json"
            get_url = base_url + get_resourece + key + "&place_id=" + place_id_list.rstrip('\n')
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)
            print(f'Статус код - {result_get.status_code}')
            assert 200 == result_get.status_code
            print('Успешно! Проверка пройдена')

        """Метод DELETE"""
        print('\nМЕТОД DELETE\n')

        delete_place = [read_file[1], read_file[3]]  # Выбираем какие именно удаляем.
        for delete_list in delete_place:
            delete_resource = '/maps/api/place/delete/json'
            delete_url = base_url + delete_resource + key
            json_for_delete_new_location = {
                "place_id": delete_list.rstrip('\n')  # Вставляется тот place id, который нужно удалить из списка.
            }
            result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
            check_delete = result_delete.json()
            status = check_delete.get('status')
            print('Place ID - ' + delete_list.rstrip('\n'))
            print('Статус удаления локации -' + status)

        """Метод GET"""
        print('\nМЕТОД GET\n')
        for place_id_list in read_file:

            get_resourece = "/maps/api/place/get/json"
            get_url = base_url + get_resourece + key + "&place_id=" + place_id_list.rstrip('\n')
            print(get_url)
            result_get = requests.get(get_url)
            print(f'Статус код - {result_get.status_code}')
            if result_get.status_code == 200:   # Проверяем какие place id остались
                with open('place_id_new.txt', mode='a') as file:    # И записываем их в файл
                    file.write(place_id_list + "\n")

        print('Place ID обновлены!')

        print('\nПроверка New_location пройдена!')


location = New_location()
location.create_new_location()