from time import sleep
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    def __init__(self, nickname, password,age):
        self.nickname = nickname
        self.password = password
        self.age = age


class UrTube:
    current_user = None
    age = 0
    def __init__(self):
        self.videos = []
        self.user_base = {}

    def log_in(self, nickname, password):
        if nickname in self.user_base:
            self.current_user = nickname

    def register(self, nickname, password, age):
        if nickname in self.user_base:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.user_base[nickname] = nickname
            self.user_base[password] = hash(password)
            self.age = age
            self.current_user = nickname


    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            spisok =[]
            spisok.append(i.title)
            spisok.append(i.duration)
            spisok.append(i.time_now)
            spisok.append(i.adult_mode)
            self.videos.append(spisok)


    def get_videos(self, poisk_text):
        self.poisk_text = poisk_text
        poisk_video = []
        for i in self.videos:
            if self.poisk_text.lower() in i[0].lower():
                poisk_video.append(i[0])
        return poisk_video

    def watch_video(self, name_film):
        self.name_film = name_film


        if self.current_user != None:
            for i in self.videos:
                if name_film == i[0]:

                    if not i[3] or self.age >= 18:
                        for j in range(1,i[1]+1):
                            print(j, end=' ')
                            sleep(0.5)
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)