import os
import codecs


TICKER_LIST_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ticker-lists')


def load_ticker_list(filename):
    data_file = os.path.join(TICKER_LIST_ROOT, filename)
    with codecs.open(data_file, 'r', encoding='utf8') as fr:
        return {row.strip()[-7:-1]: row.strip()[:-8] for row in fr.readlines()}


def main(data_path, ticker_list):

    tickers = load_ticker_list(ticker_list)

    for t, name in tickers.items():
        print t, name

    print os.listdir(data_path)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print 'usage: python pickup_ticker.py /mnt/data/stock'

    ticker_list_filename = 'blue-chip-v1.csv'
    main(sys.argv[1], ticker_list_filename)
