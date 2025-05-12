import datetime

class Year:
    calc_buddhist_year = 544  # 서기 = 불기 - 544년

    def calcYear(self, buddhist_year):
        gregorian_year = buddhist_year - self.calc_buddhist_year
        print('서기: ' + str(gregorian_year) + '년')

year = Year()
buddhist_year = 2562

year.calcYear(buddhist_year)
# 서기: 2018년