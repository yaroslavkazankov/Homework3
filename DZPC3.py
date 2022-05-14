import requests
import pathlib
class Super_Hero:
    url = ' https://superheroapi.com/api/'
    access_token = '2619421814940190'
    def __init__(self, name):
        self.name = name
        self.id = ''
        self.intelligence = ''
    def get_id(self):
        self.id = requests.get(self.url + self.access_token + '/search/' + self.name).json()['results'][0]['id']
        return self.id
    def get_intelligence(self):
        if not self.id:
            self.get_id()
        self.intelligence = requests.get(self.url + self.access_token + '/' + self.id + '/powerstats').json()['intelligence']
        return self.intelligence
def most_intelligence(heros):
    for hero in heros:
        if not hero.intelligence:
            hero.get_intelligence()
    sorted_list_of_intelligence = sorted(heros, key=lambda hero: hero.intelligence)
    return sorted_list_of_intelligence[0]

class YaUploader:
    token = ''
    def __init__(self, file_path):
        self.file_path = file_path
    def upload(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': 'disk:/Netology/' + self.file_path.name,
                  'overwrite': 'true'}
        upload_link = requests.get(url, headers=headers, params=params).json()['href']
        res = requests.put(upload_link, data=open(self.file_path, 'rb'))
        res.raise_for_status()
        if res.status_code == 201:
            return 'Файл успешно загружен на Я.Диск'
        return 'Ошибка загрузки'

if __name__ == "__main__":
    Super_Heros = [Super_Hero('Hulk'),
                   Super_Hero('Captain America'),
                   Super_Hero('Thanos')]
    winner = most_intelligence(Super_Heros)
    print(f"Самый умный - {winner.name}, его интеллект равен {winner.intelligence}")

    uploader = YaUploader(pathlib.Path('files for yadisk', 'file1.txt'))
    print(uploader.upload())