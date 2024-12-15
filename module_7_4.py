team1 = 'Мастера кода'
team2 = 'Волшебники данных'


def team_num(team1_num, team2_num):
    print('В команде %s участников: %s !' % (team1, team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))


def score_team(score_1, score_2):
    if score_1 < score_2:
        return "Команда {} решила задач: {} !".format(team2, score_2)
    else:
        return "Команда {} решила задач: {} !".format(team1, score_1)


def time_team(team1_time, team2_time):
    if team1_time < team2_time:
        return "{} решили задачи за: {} c !".format(team2, round(team2_time, 1))
    else:
        return "{} решили задачи за: {} c !".format(team1, round(team1_time, 1))


def challenge_result(tasks_total, time_avg):
    print(f'Команды решили {score1} и {score2} задач')
    if score1 > score2:
        print(f'Результат битвы: победа команды {team1} !')
    else:
        print(f'Результат битвы: победа команды {team2} !')

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')


team_num(team1_num=5, team2_num=6)
score1 = 40
score2 = 42
time_team(team1_time=1552.512, team2_time=2153.31451)
challenge_result(tasks_total=82, time_avg=45.2)