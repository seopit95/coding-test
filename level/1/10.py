class Calculation:

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def onesPlaceCalc(self):
        onesPlace = self.second_num % 10
        return self.first_num * onesPlace

    def tensPlaceCalc(self):
        tensPlace = (self.second_num // 10) % 10
        return self.first_num * tensPlace

    def hundredsPlaceCalc(self):
        hundredsPlace = (self.second_num // 100) % 10
        return self.first_num * hundredsPlace

    def calc(self):
        return self.first_num * self.second_num

calculation = Calculation(472, 385)
print(calculation.onesPlaceCalc())
print(calculation.tensPlaceCalc())
print(calculation.hundredsPlaceCalc())
print(calculation.calc())