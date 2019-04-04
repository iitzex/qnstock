import os

import dropbox

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
        link = dbx.sharing_create_shared_link_with_settings(path)

        raw_link = f'{link.url[:-4]}raw=1'
        print(raw_link)

        return raw_link


def main():
    pic_path = 'pic'
    files = os.listdir(pic_path)
    with open('config/links.csv', 'w') as f:
        for i in sorted(files):
            link = upload(pic_path, i)
            f.write(f'{i[:-4]}, {link}\n')

    upload('config', 'links.csv')
    upload('config', 'tse.csv')
    upload('config', 'filter.csv')


if __name__ == "__main__":
    main()
