import os


FIXTURES_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_fixture')
OPEN_DAYS_FILENAME = 'open_days.csv'


def load_all_open_days():
    datafile = os.path.join(FIXTURES_ROOT, OPEN_DAYS_FILENAME)

    days = []

    with open(datafile, 'r') as f:
        for row in f.readlines():
            days.extend([d for d in row.strip().split(' ') if d])

    return sorted(days)


def load_open_days(begin, end):
    all_days = load_all_open_days()

    return [d for d in all_days if d >= begin and d <= end]


# print load_open_days('20080204', '20080213')