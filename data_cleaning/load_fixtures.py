# -*- coding: utf-8 -*-
import os
import codecs


FIXTURES_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_fixture')
OPEN_DAYS_FILENAME = 'open_days.csv'


def load_all_open_days():
    datafile = os.path.join(FIXTURES_ROOT, OPEN_DAYS_FILENAME)

    days = []

    with open(datafile, 'r') as f:
        for row in f.readlines():
            days.extend([d for d in row.strip().split(' ') if d])

    return sorted(days)


_all_open_days = load_all_open_days()


def load_open_days(begin, end):
    return [d for d in _all_open_days if d >= begin and d <= end]


def load_ticker_list(filename, name_idx=0, ticker_idx=1):
    data_file = os.path.join(FIXTURES_ROOT, filename)

    tickers = {}
    with codecs.open(data_file, 'r', encoding='utf8') as fr:
        for row in fr.readlines():
            r = row.strip().split(',')
            tickers[r[ticker_idx]] = r[name_idx]

        return tickers
