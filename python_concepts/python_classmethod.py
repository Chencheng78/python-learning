class date_test:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def show_date(self):
        print(f'today is {self.year}-{self.month}-{self.day}')


    @classmethod
    def get_date(cls, date_str):
        y,m,d = map(int, date_str.split('-'))
        dateo = cls(y, m, d)
        return dateo

    # def get_date(cls, date_str):
    #     y,m,d = map(int, date_str.split('-'))
    #     cls.year, cls.month, cls.day = y, m, d
        # return cls


if __name__ == '__main__':
    d = date_test(2022, 1, 2)
    d.show_date()

    a = date_test.get_date('2021-11-11')
    d.show_date()

    a.show_date()