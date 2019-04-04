import os
from multiprocessing import Pool

import dropbox

from util import get_list

TOKEN = 'zKrtNUrN93AAAAAAAAAADdLM3ZHigfrm5bntL0vUR0pCXhKDWxGYaVIEsq8cLXRs'


def upload(basedir, fn):
    dbx = dropbox.Dropbox(TOKEN)

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

        raw_link = f'{link.url[:-4]}raw=1'
        print(raw_link)

        return raw_link


def pal_uplaod(items):
    sid, title = items
    print('{}, {}'.format(sid, title))

    pic_path = 'pic'
    with open('config/links.csv', 'a') as f:
        link = upload(pic_path, f'{sid}.svg')
        f.write(f'{sid}, {link}\n')


if __name__ == "__main__":
    os.remove('config/links.csv')

    l = get_list('filter')
    Pool(7).map(pal_uplaod, l)

    upload('config', 'links.csv')
    upload('config', 'tse.csv')
    upload('config', 'filter.csv')
