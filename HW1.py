class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, d_m_y):
        some_date = []
        for i in d_m_y.split():
            if i != '-':
                some_date.append(i)
        return int(some_date[0]), int(some_date[1]), int(some_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Правильно'
                else:
                    return f'Неверный год'
            else:
                return f'Неверный месяц'
        else:
            return f'Неверный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('10 - 11 - 2021')
today2 = Data.valid(11, 13, 2022)
today3 = Data.extract('11 - 11 - 2011')
print(today)
print(today2)
print(today3)
