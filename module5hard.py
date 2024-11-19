from time import sleep
import subprocess
# Исходные данные
    # Пользователи
user_nickname = ['Алекс', 'Den', 'Max']
user_password = ['HoTo1269', 'GAzx4590', 'LVqr1203']
user_age = [16, 27, 43]
    # Фильмы для начального заполнения
video_title = ['Маска', 'Калигула', 'Девчата', 'Высота', 'Спартак']
video_duration = [6060, 9360, 5520, 5640, 11820]
video_time_now = [3580, 9355, 1250, 590, 9867]
video_adult_mode = [False, True, False, False, False]
    # Фильмы для добавления
video_title_add = ['Чужой','Иван Грозный', 'Солярис','Калигула']
video_duration_add = [6960, 6000, 9600, 9360]
video_time_now_add = [4835, 5101, 2358, 1580]
video_adult_mode_add = [False, False, False, True]
# Описание классов работы
    # Класс User (пользователь)
class user():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    # Класс Video (фильмы)
class video():
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
# Формирование словарей объектов с присвоением каждому переменной
vars_user = {}
vars_video = {}
vars_video_add = {}

for i in range(0, len(user_nickname)):
    var_name = f'user{i}'
    vars_user[var_name] = user(user_nickname[i], hash(user_password[i]), user_age[i])

for i in range(0, len(video_title)):
    var_name = f'film{i}'
    vars_video[var_name] = video(video_title[i], video_duration[i], video_time_now[i], video_adult_mode[i])
# Описание класса UrTube (объект для работы с пользователями и видео)
class UrTube():
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    # Заполнение класса ссылками на объекты пользователи и видео
        for i in list(vars_user.values()):
            self.users.append(i)
        for i in list(vars_video.values()):
            self.videos.append(i)
    # Метод вход в объект
    def log_in(self, name, password):
        for i in self.users:
            if name == i.nickname and hash(password) == i.password:
                self.current_user = name
    # Метод выходя из объекта
    def log_out(self):
        self.current_user = None
    # Метод добавление нового пользователя в объект и словарь пользователей
    def register(self, nickname, password, age):
        lst_val = []
        max_key = 0
        for i, j in vars_user.items():
            lst_val.append(j.nickname)
            if j.nickname == nickname:
                self.current_user = nickname
            if int(i[4:]) > max_key:
                max_key = int(i[4:])
        if nickname not in lst_val:
            var_name = f'user{max_key+1}'
            vars_user[var_name] = user(nickname, hash(password), age)
            self.users.append(vars_user[var_name])
    # Метод добавления фильмов в объект и словарь видео
    def add_film(self,vars_video_add):
        lst_in = []
        max_key_video = 0
        for i in vars_video.keys():
            if int(i[4:]) > max_key_video:
                max_key_video = int(i[4:])
        for i in range(0, len(video_title_add)):
            var_name = f'film{i + max_key_video + 1}'
            vars_video_add[var_name] = video(video_title_add[i], video_duration_add[i], video_time_now_add[i],
                                             video_adult_mode_add[i])
        for i in self.videos:
            lst_in.append(i.title)
        for i in vars_video_add.values():
            if i.title not in lst_in:
                self.videos.append(i)
    # Метод поиска подстроки в названии фильмов
    def get_videos(self,find):
        lst_fnd = []
        for i in self.videos:
            if (i.title.lower().find(find.lower())) != -1:
                lst_fnd.append(i.title)
        return lst_fnd
    # Метод эмуляции просмотра от time_now
    def name_time(self, title, duration, time_now):
        dlit_move = duration - time_now
        print(f'{title}, просмотр с {time_now // 60}:{time_now % 60}')
        sleep(3)
        subprocess.run('cls', shell=True)
        for i in range(0, dlit_move):
            print(f'{title} - {(time_now + i) // 60}', ':',(time_now + i) % 60)
            sleep(1)
            subprocess.run('cls', shell=True)
        print(f'Конец фильма {title}')
        return
    # Метод просмотра фильма с проверкой возрастного ограничения
    def watch_video(self, film_name):
        if self.current_user:
            for i in self.users:
                if i.nickname == self.current_user:
                    user_age = i.age
            for i in self.videos:
                if i.title == film_name:
                    if i.adult_mode and user_age > 17:
                        time_now = i.time_now
                        i.time_now = 0
                        self.name_time(i.title, i.duration, time_now)
                        return
                    elif i.adult_mode and user_age < 18:
                        print(f'Фильм {i.title} 18+, вам {user_age}, покиньте страницу')
                        return
                    else:
                        print(i.title, i.time_now)
                        return
            print(f'Фильм: {film_name} не найден')
        else:
            print('Для просмотра войдите в систему')
# Выходные данные
urban = UrTube()
print('Фильмы UrTube')
for i in urban.videos:
    print(f'{i.title} - {(i.duration) // 60} : {(i.duration) % 60} , {(i.time_now) // 60} : {(i.time_now) % 60}, 18+ -{i.adult_mode}' )
print('-'*20)
# Добавление видео
print('Фильмы UrTube после добавления')
urban.add_film(vars_video_add)
for i in urban.videos:
    print(f'{i.title} - {(i.duration) // 60} : {(i.duration) % 60} , {(i.time_now) // 60} : {(i.time_now) % 60}, 18+ -{i.adult_mode}' )
print('-' * 20)
# Проверка на вход пользователя
print('Текущий пользователь')
print(f'До: {urban.current_user}')
urban.log_in('Den', 'GAzx4590')
print(f'После: {urban.current_user}')
    # Проверка входа в другой аккаунт
urban.log_in('kHan', 'skTY9563')
print(f'После: {urban.current_user}')
print('Проверка выхода')
urban.log_out()
print(f'После: {urban.current_user}')
# Проверка регистрации пользователя
print('-' * 20)
urban.register('Den', 'GAzx4590', 25)
for i in vars_user.values():
    print(i.nickname, i.password, i.age)
print('-' * 20)
urban.register('sTEN', 'LkRg65974', 23)
for i in vars_user.values():
    print(i.nickname, i.password, i.age)
# Проверка поиска
print('-' * 20)
fnd_word = ['та','Чужой']
print(f'Поиск фильмов с {fnd_word[0]}')
print(urban.get_videos(fnd_word[0]))
print(f'Поиск фильмов с {fnd_word[1]}')
print(urban.get_videos(fnd_word[1]))
# Просмотр видео и возрастное ограничение
print('-' * 20)
print(f'Просмотр видео "Калигула" пользователем: {urban.current_user}')
urban.watch_video('Калигула')
urban.log_in('Алекс', 'HoTo1269')
print(f'Просмотр видео "Калигула" пользователем: {urban.current_user}')
urban.watch_video('Калигула')
# Попытка воспроизведения несуществующего видео
urban.watch_video('Веселые ребята')