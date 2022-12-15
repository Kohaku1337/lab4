import datetime as dt

USD_TO_RUB = 63.80
EURO_TO_RUB = 67.88


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)

    def get_today_limit_balance(self):
        print(self.get_today_stats())
        return self.limit - self.get_today_stats()

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        return sum([record.amount if record.date == self.today else 0 for record in self.records])

    def get_week_stats(self):
        return sum([record.amount if self.week_ago <= record.date <= self.today else 0 for record in self.records])


class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency='rub'):
        currencies = {'usd': ('USD', USD_TO_RUB), 'eur': ('Euro', EURO_TO_RUB),
                      'rub': ('Rub', 1)}

        cash_remained = self.get_today_limit_balance()
        if cash_remained == 0:
            return 'Денег осталось'

        if currency not in currencies:
            return f'Здесь нет валюты: {currency} (поддерживаемой {", ".join(currencies.keys())})'

        name, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        return f'{cash_remained} {name} осталось' if cash_remained > 0 else f'Денег осталось (Валюта: {name})'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.get_today_limit_balance()
        return f'Калорий осталось: {calories_remained}.' if calories_remained > 0 else 'Ты не имеешь права потреблять калории.'


print('\n# КалькуляторДенег')
cash_calculator = CashCalculator(10000)
cash_calculator.add_record(Record(amount=3000, comment='видеоигра'))
cash_calculator.add_record(Record(amount=5000, comment='наушники'))
print(f'Недельный кэш: {cash_calculator.get_week_stats()}')
print(f'Сколько сегодня осталось кэша: {cash_calculator.get_today_cash_remained()}')
print(f'Остаточный баланс от кэша: {cash_calculator.get_today_limit_balance()}')

print('\n# Калькулятор калорий')
calories_calculator = CaloriesCalculator(3000)
calories_calculator.add_record(
    Record(amount=700, comment='мега пончик'))
calories_calculator.add_record(Record(amount=500, comment='бергер', ))
calories_calculator.add_record(
    Record(amount=50, comment='трава', ))
print(
    f'Сколько сегодня осталось калорий: {calories_calculator.get_calories_remained()}')