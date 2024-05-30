import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str
        self.password = hash("")
        self.age = int

    def __hash__(self):
        return self.password


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.verify_user = []
        self.nickname = []
        self.password = hash("")
        self.age = []
        self.get_videos = []
        self.my_str = []


    def add(self, *args):
        video = []
        check_video = False
        for i in args:
            video = [i.title, i.duration, i.time_now, i.adult_mode]
            if self.videos == []:
                self.videos.append(video)
            else:
                for j in self.videos:
                    if i.title != j[0]:
                        check_video = True
                    else:
                        check_video = False
                        break
                    if check_video == True:
                        self.videos.append(video)
                    else:
                        print(f"\033[31m фильм {i.title} уже существует !!! \033[0m")
                        time.sleep(1)
                video = []

    def get_videos(self, search_video):
        self.search_video = search_video.lower()
        self.my_search_list = ['']
        for i in self.videos:
            my_str = i[0]
            self.my_str = my_str.lower()
            if self.my_str.find(self.search_video) != -1:
                self.my_search_list.append(i[0])
            return self.my_search_list

    def watch_video(self, get_video):
        if self.current_user != None:

            for i in self.videos:
                if i[0] == self.get_videos and i[3] == True:
                    self.current_user = i[1]
                    self.current_time_now = i[2]

                    if self.age > 18:
                        print(f"\033[34m Воспроизводится: {self.get_videos}\033[0m")
                        for j in range(self.current_duration):
                            self.current_time_now = j
                            print("\033[35m * \033[0m", end="")
                            print(self.current_time_now, sep="", end="")
                            time.sleep(1)
                        print("\033[31m   Конец видео\033[0m")
                        time.sleep(2)
                    else:
                        print("\033[31m  Вам нет 18 лет, пожлуйста покиньте страницу\033[0m")
                    self.log_out()

        else:
            print("\033[31m Войдите в аккаунт чтобы смотреть видео\033[0m")

    def register(self, nickname, password, age):
        self.user = [self.nickname, self.password, self.age]
        self.verify_user = 0
        for i in self.users:
            if i[0] == self.nickname:
                self.log_in(self.nickname, self.password)

        if self.verify_user == 0:
            self.users.append(self.nickname, self.password)
        elif self.verify_user == 1:
            print(f"\033[32m Пользователь {self.nickname} уже существует\033[0m")
        elif self.verify_user == 2:
            print(f"\033[32m Пользователь {self.login} уже существует\033[0m")

    def log_in(self, login, password):
        self.login = login
        self.password = hash("")

        for i in self.users:
            if i[0] == self.login and i[1] == self.password:
                self.current_user = self.login
                self.verify_user = 1
            elif i[0] == self.login and i[1] != self.password:
                self.verify_user = 2

        return self.verify_user

    def log_out(self):
        self.current_user = None
        self.nickname = ""
        self.password = hash("")
        self.age = 0



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
watch_video('Лучший язык программирования 2024 года!')
