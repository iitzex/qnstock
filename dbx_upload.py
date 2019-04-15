import os
from multiprocessing import Pool

import dropbox

from util import get_list

TOKEN = 'zKrtNUrN93AAAAAAAAAADdLM3ZHigfrm5bntL0vUR0pCXhKDWxGYaVIEsq8cLXRs'
dbx = dropbox.Dropbox(TOKEN)
ll = []


def upload(basedir, fn):
    global dbx

    if basedir == '':
        fullname = f'{fn}'
    else:
        fullname = f'{basedir}/{fn}'

    path = f'/{fullname}'
    print(path)
    mode = dropbox.files.WriteMode.overwrite

    with open(fullname, 'rb') as f:
        data = f.read()

        f = dbx.files_upload(data, path, mode)
        link = dbx.sharing_create_shared_link(path)

        print(link)
        # raw_link = f'{link.url[:-4]}raw=1'
        # print(raw_link)

        return link


def pal_upload(items):
    global ll
    sid, title = items
    print('{}, {}'.format(sid, title))

    pic_path = 'pic'
    link = upload(pic_path, f'{sid}.svg')
    ll.append(link)


def get_links():
    if os.path.isfile('config/links.csv'):
        os.remove('config/links.csv')

    for sid, title in get_list('tse'):
        fn = f'{sid}.svg'

        global dbx
        basedir = 'pic'
        # fullname = f'{basedir}/{fn}'
        # path = f'/{fullname}'
        ln = upload(basedir, fn)
        print(sid, title, ln.url)

        raw_link = f'{ln.url[:-4]}raw=1'
        with open('config/links.csv', 'a') as f:
            f.write(f'{sid}, {raw_link}\n')
            # f.write(f'{sid}, {ln}\n')


def pic():
    lt = get_list('filter')
    for item in lt:
        pal_upload(item)
    # p = Pool(2)
    # p.map(pal_upload, lt)
    # p.close()
    # p.join()
    print(ll)


if __name__ == "__main__":
    # pic()

    get_links()

    upload('config', 'links.csv')
    upload('config', 'filter.csv')
    # upload('config', 'tse.csv')
