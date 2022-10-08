import json
import datetime
import os.path


class UserProfile:

    def __init__(self, user_name,
                 user_last_name,
                 birth_day,
                 completed_years,
                 previous_jobs,
                 create_date,
                 worked_years):

        self.user_name = user_name
        self.user_last_name = user_last_name
        self.birth_day = birth_day
        self.completed_years = completed_years
        self.previous_jobs = previous_jobs
        self.create_date = create_date
        self.worked_years = worked_years

    def __str__(self):
        return f'Имя:{self.user_name}\n' \
               f'Фамилия: {self.user_last_name}\n' \
               f'Дата рождения: {self.birth_day}\n' \
               f'Полных лет:{self.completed_years}\n' \
               f'Места работы: {" ".join(self.previous_jobs)}\n' \
               f'Дата создания:{self.create_date}'

    def __len__(self):
        """
        Returns:
            Количество пользователей
        """
        return f'Количество пользователей:{self.read_profiles()}'

    def __int__(self):
        """
        Returns:
            Количество отработанных лет
        """
        today = self.now()
        self.worked_years = int(today) - int(self.create_date)
        return self.worked_years

    def now(self):
        """
        Returns:
            Текущую дату
        """
        now = datetime.datetime.now()
        return now.strftime("%d-%m-%Y")

    def user_birth_day(self, day: int, month: int, year: int):
        """
        Метод записывает день рождение пользователя

        Args:
            day: День рождения
            month: Месяц рождения
            year:Год рождения

        Returns:
            День рождения
        """
        self.birth_day = datetime.date(day, month, year).strftime("%d-%m-%Y")
        return self.birth_day

    def user_completed_years(self):
        """
        Returns:
            Количество полных лет
        """
        today = self.now()
        return self.completed_years == int(today) - int(self.birth_day)

    def read_profiles(self):
        """
        Метод проверяет существование файла
        Если файл существует, то открывает его
        Если файла не существует, создаёт его с пустым списком

        Returns:
            Список профилей
        """
        check_file = os.path.exists('profiles.json')
        if not check_file:
            data = []
            self.save_changes(data)
        else:
            with open('profiles.json', 'r') as write_file:
                data = json.load(write_file)
        return data

    def save_changes(self, data):
        """
            Метод сохраняет изменения в файле
        """
        with open('profiles.json', 'w') as write_file:
            json.dump(data, write_file)

    def create_profiles(self, user_name: str,
                        user_last_name: str,
                        previous_jobs: list, ):
        """
        Метод для создания профиля
        
        Args:
            user_name: День рождения
            user_last_name: Месяц рождения
            previous_jobs:
        """
        data = self.read_profiles()
        self.user_name = user_name
        self.user_last_name = user_last_name
        self.completed_years = self.user_completed_years()
        self.previous_jobs = previous_jobs
        self.create_date = self.now()
        user_profile = {
            'user_name': self.user_name,
            'user_last_name': self.user_last_name,
            'birth_day': self.birth_day,
            'completed_years': self.completed_years,
            'create_date': self.create_date,
            'previous_jobs': self.previous_jobs
        }
        data.append(user_profile)
        self.save_changes(data)
