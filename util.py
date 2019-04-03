import os
import csv
from os import listdir
from os.path import isfile, join


def add_columns():
    # add columns for data/csv
    mypath = 'data/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for filename in onlyfiles:
        with open('data/' + filename, 'r') as original:
            lines = original.readlines()

        new_lines = []
        for line in lines:
            if '--' not in line:
                new_lines.append(line)

        with open('data/' + filename, 'w') as modified:
            modified.writelines(new_lines)


def convert_time():
    all = os.listdir('data/')
    for _ in all:
        with open('data/' + _, 'r') as fp:
            tp = open('old/' + _, 'w')
            for i, line in enumerate(fp.readlines()):
                if i == 0:
                    tp.write(line.__str__())
                    continue
                time = line.split(',')
                s = time[0].split('/')
                s[0] = str(int(s[0]) + 1911)
                t = '-'.join(s)
                time[0] = t
                tp.write(','.join(time))


def get_list(name, bound=0):
    f = open(f'config/{name}.csv', 'r')
    lists = csv.reader(f)

    r = [] 
    for stock in lists:
        sid = stock[0]
        title = (stock[1]).strip()

        try:
            if int(sid) >= int(bound):
                # yield sid, title
                r.append((sid, title))
        except ValueError as e:
            r.append((sid, title))

    f.close()
    return r


if __name__ == '__main__':
    r = get_list('otc')
    for sid, title in r:
        # print(sid, title)
        import os
        os.remove('data/'+sid+'.csv')
