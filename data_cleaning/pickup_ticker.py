import os


def scan(path):
    print os.listdir(path)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print 'usage: python pickup_ticker.py /mnt/data/stock'

    scan(sys.argv[1])
