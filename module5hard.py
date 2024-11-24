from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


    def __contains__(self, item):
        for user in item:
            if self.nickname == user.nickname:
                return True
        return False


    def __str__(self):
        return self.nickname



class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def log_in(self, nickname, password:str):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user


    def register(self, nickname, password:str, age):
        user = False

        for i in self.users:
            if i.nickname == nickname:
                user = True
                print(f"Пользователь {nickname} уже существует")
                break

        if not user:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user


    def log_out(self, nickname):
        self.current_user = None


    def add(self, *video):
        videos_list = [*video]
        for addvideo in videos_list:
            if isinstance(addvideo, Video):
                title = addvideo.title
                if title in self.videos:
                    continue
                else:
                    self.videos.append(addvideo)


    def get_videos(self, search_word):
        videos_list = []
        for srch in self.videos:
            if isinstance(srch, Video):
                title = srch.title
                if search_word.lower() in title.lower():
                        videos_list.append(title)
            else:
                continue
        return videos_list


    def watch_video(self, movie):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for i in self.videos:
            if i.title == movie:
                if i.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for j in range(1, 11):
                    print(j, end=' ')
                    sleep(1)
                    i.time_now += 1
                i.time_now = 0
                print('Конец видео')


if __name__ == '__main__':

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

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')