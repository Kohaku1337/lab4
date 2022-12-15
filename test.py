import pytest
from main import Record, CashCalculator, CaloriesCalculator


@pytest.fixture()
def cal_calc():
    calories_calculator = CaloriesCalculator(3220)
    calories_calculator.add_record(
        Record(amount=1337, comment='Ice cream'))
    calories_calculator.add_record(
        Record(amount=444, comment='Chocolate milk', ))
    return calories_calculator.get_calories_remained()


@pytest.fixture()
def cash_calc():
    cash_calculator = CashCalculator(500)
    cash_calculator.add_record(Record(amount=888, comment='Infinity Carbonara'))
    cash_calculator.add_record(Record(amount=777, comment='Jakpot Rice'))
    return cash_calculator.get_today_cash_remained()


def test_cashCalc(cash_calc):
    assert cash_calc == 'Денег осталось (Валюта: Руб)'


def test_CalCalc(cal_calc):
    assert cal_calc == 'Калорий осталось: 233.'