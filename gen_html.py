import csv

import pandas as pd

from util import get_list


def generator(name):
    DBX = dictionary()
    print(DBX)

    with open(f'templates/{name}.html', 'w') as f:
        print('Generating HTML of ' + name.upper() + ' ...')

        head = '''
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>{}</title>
            </head>
            <body >'''.format(name.upper())
        end = '</body> </html>'

        body = ''
        for sid, title in get_list(name):
            try:
                if '-' in sid:
                    body += "<hr width='95%' color='red'><hr width='95%' color='red'>"
                    continue

                body += f"<p align=center>{sid}, {title}\n"
                body += f"<a href='https://statementdog.com/analysis/tpe/{sid}'>財報狗</a>"
                body += f"<a href='http://www.wantgoo.com/stock/astock/index?StockNo={sid}'> 玩股網</a>"
                body += f"<a href='https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID={sid}'> Goodinfo</a>"
                body += f"<a href='https://histock.tw/stock/{sid}'> HiStock</a>"
                body += f"</br><img src='{(DBX[sid]).strip()}' height='91%' width='100%'  class='center' /></p>\n"

            except KeyError as e:
                # print(sid, e)
                pass

        text = head + body + end
        f.write(text)


def html():
    generator('tse')
    # generator('filter')


def dictionary():
    DBX = {}
    with open('links.csv', 'r') as f:
        lists = csv.reader(f)

        for pair in lists:
            item = {pair[0]: pair[1]}
            # print(pair)
            DBX.update(item)

    return DBX


if __name__ == '__main__':
    html()
