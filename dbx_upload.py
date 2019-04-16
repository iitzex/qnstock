import os
from multiprocessing import Pool
from shutil import copyfile

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


if __name__ == "__main__":
    get_links()

    copyfile('../kdtrace/filter.csv', 'config/filter.csv')
    upload('config', 'links.csv')
    upload('config', 'filter.csv')
    # upload('config', 'tse.csv')
