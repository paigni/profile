import json
import datetime
import os.path


class UserProfile:

    def __init__(self,user_name,user_last_name,birth_day,completed_years,previous_jobs,create_date):
        self.user_name = user_name
        self.user_last_name = user_last_name
        self.birth_day = birth_day
        self.completed_years = completed_years
        self.previous_jobs = previous_jobs
        self.create_date = create_date


    def __str__(self):
        return f'Имя:{self.user_name}\n' \
               f'Фамилия: {self.user_last_name}\n' \
               f'Дата рождения: {self.birth_day}\n' \
               f'Полных лет:{self.completed_years}\n' \
               f'Места работы: {" ".join(self.previous_jobs)}\n' \
               f'Дата создания:{self.create_date}'


    def now(self):
        """
        """
        now = datetime.datetime.now()
        return now.strftime("%d-%m-%Y")


    def completed_years(self,day,month,year):
        self.birth_day = datetime.date(day, month, year).strftime("%d-%m-%Y")
        today = self.now()
        self.completed_years = int(today) - int(self.birth_day)



    def read_profiles(self):
        """
        """
        check_file = os.path.exists('notes.json')
        if not check_file:
            data = []
            self.save_changes(data)
        else:
            with open('profiles.json', 'r') as write_file:
                data = json.load(write_file)
        return data


    def __len__(self):
        return f'Количество пользователе:{self.read_profiles()}'


    def save_changes(self, data):
        """
            Метод сохраняет изменения в файле
        """
        with open('profiles.json', 'w') as write_file:
            json.dump(data, write_file)


    def action_with_note(self, user_name: str, user_last_name: str, birth_day: str,
                         completed_years:str, previous_jobs : list,):
        """
        """
        data = self.read_profiles()
        self.user_name = user_name
        self.user_last_name = user_last_name
        self.birth_day = birth_day
        self.completed_years = completed_years
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


