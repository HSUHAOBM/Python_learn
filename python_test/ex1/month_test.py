from datetime import datetime
from dateutil.relativedelta import relativedelta

# python3 -m pytest tests/month_test.py -v -s

def transfor_logic_date(date, month_end_date, month_end_days, payment_day):
    oringin_day = date.day

    if oringin_day > month_end_date:
        # 算下個月
        date = date + relativedelta(months=1)

    if oringin_day <= month_end_date:
        # 算當月
        # 算出當月月底
        date = date + relativedelta(day=1, months=1) - relativedelta(days=1)

    # 依照 month_end_days
    date = date + relativedelta(months=month_end_days)

    if not payment_day:
        # 直接算當月月底
        date = date + relativedelta(day=1, months=1) - relativedelta(days=1)
    elif date.day > payment_day:
        # 往後推一個月
        date = date + relativedelta(day=payment_day, months=1)
    else:
        # 不需要往後推一個月
        pass
        print()

    return date


def test01_A_answer():
    # 月結日
    month_end_date = 20

    # 月結天數
    month_end_days = 1

    # 付款日
    payment_day = 5

    result_1 = transfor_logic_date(datetime(2018, 2, 20), month_end_date, month_end_days, payment_day)
    assert result_1 == datetime(2018, 4, 5)

    result_2 = transfor_logic_date(datetime(2018, 2, 21), month_end_date, month_end_days, payment_day)
    assert result_2 == datetime(2018, 5, 5)

    result_3 = transfor_logic_date(datetime(2018, 3, 19), month_end_date, month_end_days, payment_day)
    assert result_3 == datetime(2018, 5, 5)

    result_4 = transfor_logic_date(datetime(2018, 3, 23), month_end_date, month_end_days, payment_day)
    assert result_4 == datetime(2018, 6, 5)

test01_A_answer()

def test02_A_answer():
    # 月結日
    month_end_date = 22

    # 月結天數
    month_end_days = 2

    # 付款日
    payment_day = 3

    result_1 = transfor_logic_date(datetime(2018, 2, 20), month_end_date, month_end_days, payment_day)
    assert result_1 == datetime(2018, 5, 3)

    result_2 = transfor_logic_date(datetime(2018, 2, 21), month_end_date, month_end_days, payment_day)
    assert result_2 == datetime(2018, 5, 3)

    result_3 = transfor_logic_date(datetime(2018, 3, 19), month_end_date, month_end_days, payment_day)
    assert result_3 == datetime(2018, 6, 3)

    result_4 = transfor_logic_date(datetime(2018, 3, 23), month_end_date, month_end_days, payment_day)
    assert result_4 == datetime(2018, 7, 3)


test02_A_answer()

def test03_A_answer():
    # 月結日
    month_end_date = 22

    # 月結天數
    month_end_days = 2

    # 付款日
    payment_day = 0

    result_1 = transfor_logic_date(datetime(2018, 2, 20), month_end_date, month_end_days, payment_day)
    assert result_1 == datetime(2018, 4, 30)

    result_2 = transfor_logic_date(datetime(2018, 2, 21), month_end_date, month_end_days, payment_day)
    assert result_2 == datetime(2018, 4, 30)

    result_3 = transfor_logic_date(datetime(2018, 3, 19), month_end_date, month_end_days, payment_day)
    assert result_3 == datetime(2018, 5, 31)

    result_4 = transfor_logic_date(datetime(2018, 3, 23), month_end_date, month_end_days, payment_day)
    assert result_4 == datetime(2018, 6, 30)

test03_A_answer()

def test04_A_answer():
    # 月結日
    month_end_date = 25

    # 月結天數
    month_end_days = 1

    # 付款日
    payment_day = 10

    result_1 = transfor_logic_date(datetime(2018, 4, 1), month_end_date, month_end_days, payment_day)
    assert result_1 == datetime(2018, 6, 10)

    result_2 = transfor_logic_date(datetime(2018, 4, 10), month_end_date, month_end_days, payment_day)
    assert result_2 == datetime(2018, 6, 10)

    result_3 = transfor_logic_date(datetime(2018, 5, 1), month_end_date, month_end_days, payment_day)
    assert result_3 == datetime(2018, 7, 10)

    result_4 = transfor_logic_date(datetime(2018, 5, 10), month_end_date, month_end_days, payment_day)
    assert result_4 == datetime(2018, 7, 10)

test04_A_answer()

def test05_A_answer():
    # 月結日
    month_end_date = 20

    # 月結天數
    month_end_days = 2

    # 付款日
    payment_day = 5

    result_1 = transfor_logic_date(datetime(2018, 3, 1), month_end_date, month_end_days, payment_day)
    assert result_1 == datetime(2018, 6, 5)

    result_2 = transfor_logic_date(datetime(2018, 3, 5), month_end_date, month_end_days, payment_day)
    assert result_2 == datetime(2018, 6, 5)

    result_3 = transfor_logic_date(datetime(2018, 4, 1), month_end_date, month_end_days, payment_day)
    assert result_3 == datetime(2018, 7, 5)

    result_4 = transfor_logic_date(datetime(2018, 4, 3), month_end_date, month_end_days, payment_day)
    assert result_4 == datetime(2018, 7, 5)

test05_A_answer()

def test06_A_answer():
    # 月結日
    month_end_date = 23

    # 月結天數
    month_end_days = 2

    # 付款日
    payment_day = 0

    result_1 = transfor_logic_date(datetime(2018, 2, 20), month_end_date, month_end_days, payment_day)
    assert result_1 == datetime(2018, 4, 30)

    result_2 = transfor_logic_date(datetime(2018, 2, 24), month_end_date, month_end_days, payment_day)
    assert result_2 == datetime(2018, 5, 31)

    result_3 = transfor_logic_date(datetime(2018, 3, 23), month_end_date, month_end_days, payment_day)
    assert result_3 == datetime(2018, 5, 31)

    result_4 = transfor_logic_date(datetime(2018, 3, 24), month_end_date, month_end_days, payment_day)
    assert result_4 == datetime(2018, 6, 30)

test06_A_answer()

# def test01_answer():

#     # 月結日
#     month_end_date = 25

#     # 月結天數
#     month_end_days = 1

#     # 付款日
#     payment_day = 10

#     result_1 = transfor_logic_date(datetime(2018, 2, 26), month_end_date, month_end_days, payment_day)
#     assert result_1 == datetime(2018, 5, 10)

#     result_2 = transfor_logic_date(datetime(2018, 3, 25), month_end_date, month_end_days, payment_day)
#     assert result_2 == datetime(2018, 5, 10)

#     result_3 = transfor_logic_date(datetime(2018, 3, 26), month_end_date, month_end_days, payment_day)
#     assert result_3 == datetime(2018, 6, 10)

#     result_4 = transfor_logic_date(datetime(2018, 4, 25), month_end_date, month_end_days, payment_day)
#     assert result_4 == datetime(2018, 6, 10)

# test01_answer()


# def test05_A_answer():
#     # 月結日
#     month_end_date = 30

#     # 月結天數
#     month_end_days = 1

#     # 付款日
#     payment_day = 5

#     result_1 = transfor_logic_date(datetime(2018, 2, 28), month_end_date, month_end_days, payment_day)
#     assert result_1 == datetime(2018, 4, 5)

