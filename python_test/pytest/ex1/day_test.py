from datetime import datetime
from dateutil.relativedelta import relativedelta

# python3 -m pytest tests/day_test.py -v -s

def transfor_logic_date(date, month_end_date, month_end_days, payment_day):
    oringin_day = date.day

    if oringin_day > month_end_date:
        # 算下個月
        date = date + relativedelta(day=1, months=2) - relativedelta(days=1)

    if oringin_day <= month_end_date:
        # 算當月
        # 算出當月月底
        date = date + relativedelta(day=1, months=1) - relativedelta(days=1)

    # 依照 month_end_days
    date = date + relativedelta(days=month_end_days)

    if not payment_day:
        # 月節日 不需要 算當月月底
        pass
    elif date.day > payment_day:
        # 往後推一個月
        date = date + relativedelta(day=payment_day, months=1)
    else:
        # 不需要往後推一個月
        date = date + relativedelta(day=payment_day)
        print()

    return date


def test01_A_answer():
    # 月結日
    month_end_date = 20

    # 月結天數
    month_end_days = 45

    # 付款日
    payment_day = 25

    result_1 = transfor_logic_date(datetime(2018, 2, 19), month_end_date, month_end_days, payment_day)
    assert result_1 == datetime(2018, 4, 25)

    result_2 = transfor_logic_date(datetime(2018, 2, 20), month_end_date, month_end_days, payment_day)
    assert result_2 == datetime(2018, 4, 25)

    result_3 = transfor_logic_date(datetime(2018, 3, 19), month_end_date, month_end_days, payment_day)
    assert result_3 == datetime(2018, 5, 25)

    result_4 = transfor_logic_date(datetime(2018, 3, 23), month_end_date, month_end_days, payment_day)
    assert result_4 == datetime(2018, 6, 25)

test01_A_answer()

def test02_A_answer():
    # 月結日
    month_end_date = 22

    # 月結天數
    month_end_days = 90

    # 付款日
    payment_day = 10

    result_1 = transfor_logic_date(datetime(2018, 2, 20), month_end_date, month_end_days, payment_day)
    assert result_1 == datetime(2018, 6, 10)

    result_2 = transfor_logic_date(datetime(2018, 2, 21), month_end_date, month_end_days, payment_day)
    assert result_2 == datetime(2018, 6, 10)

    result_3 = transfor_logic_date(datetime(2018, 3, 19), month_end_date, month_end_days, payment_day)
    assert result_3 == datetime(2018, 7, 10)

    result_4 = transfor_logic_date(datetime(2018, 3, 23), month_end_date, month_end_days, payment_day)
    assert result_4 == datetime(2018, 8, 10)

test02_A_answer()

def test03_A_answer():
    # 月結日
    month_end_date = 22

    # 月結天數
    month_end_days = 70

    # 付款日
    payment_day = 0

    result_1 = transfor_logic_date(datetime(2018, 2, 20), month_end_date, month_end_days, payment_day)
    assert result_1 == datetime(2018, 5, 9)

    result_2 = transfor_logic_date(datetime(2018, 2, 21), month_end_date, month_end_days, payment_day)
    assert result_2 == datetime(2018, 5, 9)

    result_3 = transfor_logic_date(datetime(2018, 3, 19), month_end_date, month_end_days, payment_day)
    assert result_3 == datetime(2018, 6, 9)

    result_4 = transfor_logic_date(datetime(2018, 3, 23), month_end_date, month_end_days, payment_day)
    assert result_4 == datetime(2018, 7, 9)

test03_A_answer()

